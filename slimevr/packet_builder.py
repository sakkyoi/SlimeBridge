from io import BytesIO
import struct
from itertools import count
from enum import IntEnum

from .constants import PacketHeader, TrackerPosition, BoardType, IMUType, MCUType, SensorStatus, MagnetometerStatus, TrackerDataType


class Quaternion:
    def __init__(self, x: float, y: float, z: float, w: float):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __iter__(self):
        return iter([self.x, self.y, self.z, self.w])


class PacketBuilder:
    def __init__(self, tracker_id: int):
        self.fw_string = "SlimeBridge"
        self.protocol_version = 1
        self.tracker_id = tracker_id
        self.packet_id = count(0)
        self.adding_tracker_id = count(1)

    def build_handshake_packet(self) -> BytesIO:
        """
        slimevr server implementation:
        https://github.com/SlimeVR/SlimeVR-Server/blob/394c1dd43833e6ffc1f65ee4e9efa764f027391c/server/core/src/main/java/dev/slimevr/tracking/trackers/udp/UDPPacket.kt#L95-L148

        slimevr tracker implementation:
        https://github.com/SlimeVR/SlimeVR-Tracker-ESP/blob/6942e486ede6bb5b673e020eb9df8027d197b687/src/network/connection.cpp#L398-L424

        :return: packet containing the handshake data
        """
        # reset the packet id and tracker id
        self.packet_id = count(0)
        self.adding_tracker_id = count(1)

        packet = BytesIO()
        packet.write(struct.pack(">i", PacketHeader.HANDSHAKE))  # packet header
        packet.write(struct.pack(">q", next(self.packet_id)))  # packet id
        packet.write(struct.pack(">i", BoardType.UNKNOWN))  # board type
        packet.write(struct.pack(">i", IMUType.UNKNOWN))  # imu type
        packet.write(struct.pack(">i", MCUType.UNKNOWN))  # mcu type
        packet.write(struct.pack(">3i", 0, 0, 0))  # imu info (useless data)
        packet.write(struct.pack(">i", self.protocol_version))  # protocol version
        packet.write(struct.pack(">b", len(self.fw_string.encode())))  # firmware version length
        packet.write(self.fw_string.encode())  # firmware version
        # the first 255 is to make sure the mac address not be 00:00:00:00:00:00 (which will be set to null by server)
        # int(str(self.tracker_id), 16) ensures the hex representation matches its decimal version
        packet.write(struct.pack(">6B", 255, 0, 0, 0, 0, int(str(self.tracker_id), 16)))  # mac address

        return packet

    def build_sensor_info_packet(self, tracker_position: TrackerPosition) -> BytesIO:
        """
        slimevr server implementation:
        https://github.com/SlimeVR/SlimeVR-Server/blob/394c1dd43833e6ffc1f65ee4e9efa764f027391c/server/core/src/main/java/dev/slimevr/tracking/trackers/udp/UDPPacket.kt#L224-L254

        slimevr tracker implementation:
        https://github.com/SlimeVR/SlimeVR-Tracker-ESP/blob/6942e486ede6bb5b673e020eb9df8027d197b687/src/network/connection.cpp#L288-L302

        ** Not used in the current implementation since we are using separate UDP connections for each tracker **

        :param tracker_position: position of the tracker
        :return: packet containing the sensor info
        """
        packet = BytesIO()
        packet.write(struct.pack(">i", PacketHeader.SENSOR_INFO))  # packet header
        packet.write(struct.pack(">q", next(self.packet_id)))  # packet id
        packet.write(struct.pack(">b", next(self.adding_tracker_id)))  # sensor id
        packet.write(struct.pack(">b", SensorStatus.OK))  # sensor status
        packet.write(struct.pack(">b", IMUType.UNKNOWN))  # imu type
        packet.write(struct.pack(">h", MagnetometerStatus.NOT_SUPPORTED))  # magnetometer status
        packet.write(struct.pack(">b", tracker_position))  # tracker position
        packet.write(struct.pack(">b", TrackerDataType.ROTATION))  # tracker data type

        return packet

    def build_rotation_packet(self, tracker_id: int, rotation: Quaternion) -> BytesIO:
        """
        slimevr server implementation:
        https://github.com/SlimeVR/SlimeVR-Server/blob/394c1dd43833e6ffc1f65ee4e9efa764f027391c/server/core/src/main/java/dev/slimevr/tracking/trackers/udp/UDPPacket.kt#L265-L283

        slimevr tracker implementation:
        https://github.com/SlimeVR/SlimeVR-Tracker-ESP/blob/6942e486ede6bb5b673e020eb9df8027d197b687/src/network/connection.cpp#L304-L326

        :param tracker_id: id of the tracker to send the rotation data
        :param rotation: quaternion representing the rotation
        :return: packet containing the rotation data
        """
        class DataType(IntEnum):
            """
            The data type of the packet (note that only `NORMAL` is implemented in slimevr server for now)
            """
            NORMAL = 1
            CORRECTION = 2  # Not implemented in slimevr server

        packet = BytesIO()
        packet.write(struct.pack(">i", PacketHeader.ROTATION_DATA))  # packet header
        packet.write(struct.pack(">q", next(self.packet_id)))  # packet id
        packet.write(struct.pack(">b", tracker_id))  # sensor id
        packet.write(struct.pack(">b", DataType.NORMAL))  # data type
        packet.write(struct.pack(">4f", *rotation))  # rotation
        packet.write(struct.pack(">b", 0))  # calibration info (not implemented in slimevr server for now)

        return packet
