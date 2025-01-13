from enum import IntEnum


class BoardType(IntEnum):
    """
    https://github.com/SlimeVR/SlimeVR-Server/blob/394c1dd43833e6ffc1f65ee4e9efa764f027391c/server/core/src/main/java/dev/slimevr/tracking/trackers/udp/FirmwareConstants.kt#L33-L87
    """
    UNKNOWN = 0
    SLIMEVR_LEGACY = 1
    SLIMEVR_DEV = 2
    NODEMCU = 3
    CUSTOM = 4
    WROOM32 = 5
    WEMOSD1MINI = 6
    TTGO_TBASE = 7
    ESP01 = 8
    SLIMEVR = 9
    LOLIN_C3_MINI = 10
    BEETLE32C3 = 11
    ES32C3DEVKITM1 = 12
    OWOTRACK = 13
    WRANGLER = 14
    MOCOPI = 15
    WEMOSWROOM02 = 16
    XIAO_ESP32C3 = 17
    HARITORA = 18
    DEV_RESERVED = 250
