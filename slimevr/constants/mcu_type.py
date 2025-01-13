from enum import IntEnum


class MCUType(IntEnum):
    """
    https://github.com/SlimeVR/SlimeVR-Server/blob/394c1dd43833e6ffc1f65ee4e9efa764f027391c/server/core/src/main/java/dev/slimevr/tracking/trackers/udp/FirmwareConstants.kt#L89-L110
    """
    UNKNOWN = 0
    ESP8266 = 1
    ESP32 = 2
    OWOTRACK_ANDROID = 3
    WRANGLER = 4
    OWOTRACK_IOS = 5
    ESP32_C3 = 6
    MOCOPI = 7
    HARITORA = 8
    DEV_RESERVED = 250
