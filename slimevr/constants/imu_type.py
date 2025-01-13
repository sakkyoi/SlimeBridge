from enum import IntEnum


class IMUType(IntEnum):
    """
    https://github.com/SlimeVR/SlimeVR-Server/blob/394c1dd43833e6ffc1f65ee4e9efa764f027391c/server/core/src/main/java/dev/slimevr/tracking/trackers/udp/FirmwareConstants.kt#L3-L31
    """
    UNKNOWN = 0
    MPU9250 = 1
    MPU6500 = 2
    BNO080 = 3
    BNO085 = 4
    BNO055 = 5
    MPU6050 = 6
    BNO086 = 7
    BMI160 = 8
    ICM20948 = 9
    ICM42688 = 10
    BMI270 = 11
    LSM6DS3TRC = 12
    LSM6DSV = 13
    LSM6DSO = 14
    LSM6DSR = 15
    DEV_RESERVED = 250
