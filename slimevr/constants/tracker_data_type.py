from enum import IntEnum


class TrackerDataType(IntEnum):
    """
    https://github.com/SlimeVR/SlimeVR-Server/blob/394c1dd43833e6ffc1f65ee4e9efa764f027391c/server/core/src/main/java/dev/slimevr/tracking/trackers/udp/FirmwareConstants.kt#L112-L126
    """
    ROTATION = 0
    FLEX_RESISTANCE = 1
    FLEX_ANGLE = 2
