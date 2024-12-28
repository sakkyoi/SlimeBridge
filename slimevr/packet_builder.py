from io import BytesIO
import struct
from itertools import count


class PacketBuilder:
    heartbeat_packet = b'\x00' * 28

    def __init__(self):
        self.fw_string = "SlimeBridge"
        self.protocol_version = 19
        self.packet_id = count(1)
        self.adding_tracker_id = count(0)

    def build_handshake_packet(self) -> BytesIO:
        self.adding_tracker_id = 0

        packet = BytesIO()
        packet.write(struct.pack(">I", 3))  # packet header
        packet.write(struct.pack(">Q", 0))  # packet counter
        packet.write(struct.pack(">I", 0))  # board type
        packet.write(struct.pack(">I", 0))  # IMU type
        packet.write(struct.pack(">I", 0))  # MCU type
        packet.write(struct.pack(">III", 0, 0, 0))  # IMU info
        packet.write(struct.pack(">I", self.protocol_version))  # protocol version
        packet.write(struct.pack(">I", len(self.fw_string)))  # firmware string length
        packet.write(self.fw_string.encode())  # firmware string
        packet.write(struct.pack(">6B", 0, 0, 0, 0, 0, 0))  # mac address

        return packet

    def build_sensor_info_packet(self, tracker_position: int) -> BytesIO:
        packet = BytesIO()
        packet.write(struct.pack(">I", 15))  # packet header
        packet.write(struct.pack(">Q", next(self.packet_id)))  # packet counter
        packet.write(struct.pack(">I", next(self.adding_tracker_id)))  # tracker id
        packet.write(struct.pack(">I", 0))  # sensor status
        packet.write(struct.pack(">I", 0))  # imu type
        packet.write(struct.pack(">H", 0))  # magnetometer support
        # https://github.com/SlimeVR/SlimeVR-Sender-Example/blob/1df342a0fcb18bd84c4103a10453d41ec9dfdcdc/src/main/kotlin/FirmwareConstants.kt#L142-L194
        packet.write(struct.pack(">I", tracker_position))  # tracker position
        packet.write(struct.pack(">I", 0))  # data type

        return packet

    def build_rotation_packet(self, tracker_id: int, rotation: list) -> BytesIO:
        packet = BytesIO()
        packet.write(struct.pack(">I", 17))  # packet header
        packet.write(struct.pack(">Q", next(self.packet_id)))  # packet counter
        packet.write(struct.pack(">I", tracker_id))  # tracker id
        packet.write(struct.pack(">I", 0))  # data type
        packet.write(struct.pack(">f", rotation[0]))  # quaternion x
        packet.write(struct.pack(">f", rotation[1]))  # quaternion y
        packet.write(struct.pack(">f", rotation[2]))  # quaternion z
        packet.write(struct.pack(">f", rotation[3]))  # quaternion w
        packet.write(struct.pack(">I", 0))  # calibration info

        return packet
