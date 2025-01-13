from enum import IntEnum


class MagnetometerStatus(IntEnum):
    """
    https://github.com/SlimeVR/SlimeVR-Server/blob/394c1dd43833e6ffc1f65ee4e9efa764f027391c/server/core/src/main/java/dev/slimevr/tracking/trackers/udp/FirmwareConstants.kt#L131-L145
    """
    NOT_SUPPORTED = 0
    DISABLED = 1
    ENABLED = 2
