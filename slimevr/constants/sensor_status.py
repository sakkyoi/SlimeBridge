from enum import IntEnum


class SensorStatus(IntEnum):
    """
    https://github.com/SlimeVR/SlimeVR-Server/blob/394c1dd43833e6ffc1f65ee4e9efa764f027391c/server/core/src/main/java/dev/slimevr/tracking/trackers/udp/UDPPacket.kt#L247-L252
    """
    DISCONNECTED = 0
    OK = 1
    ERROR = 2
