from enum import IntEnum


class PacketHeader(IntEnum):
    """
    https://github.com/SlimeVR/SlimeVR-Server/blob/181ba089c27e77f1c1496936d14977c5b2242eee/server/core/src/main/java/dev/slimevr/tracking/trackers/udp/UDPProtocolParser.kt#L124-L159
    """
    HEARTBEAT = 0
    ROTATION = 1  # Deprecated
    GYRO = 2  # Deprecated
    HANDSHAKE = 3
    ACCEL = 4
    MAG = 5  # Deprecated
    RAW_CALIBRATION_DATA = 6  # Not parsed by server
    CALIBRATION_FINISHED = 7  # Not parsed by server
    CONFIG = 8  # Not parsed by server
    RAW_MAGNETOMETER = 9  # Deprecated
    PING_PONG = 10
    SERIAL = 11
    BATTERY_LEVEL = 12
    TAP = 13
    ERROR = 14
    SENSOR_INFO = 15
    ROTATION_2 = 16  # Deprecated
    ROTATION_DATA = 17
    MAGNETOMETER_ACCURACY = 18
    SIGNAL_STRENGTH = 19
    TEMPERATURE = 20
    USER_ACTION = 21
    FEATURE_FLAGS = 22
    ROTATION_AND_ACCELERATION = 23
    ACK_CONFIG_CHANGE = 24
    SET_CONFIG_FLAG = 25
    FLEX_DATA = 26
    BUNDLE = 100
    BUNDLE_COMPACT = 101
    PROTOCOL_CHANGE = 200
