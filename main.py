from sys import platform
from rebocap import download_sdk


class PlatformNotSupported(Exception):
    pass


if platform != "win32":
    raise PlatformNotSupported("This script is only supported on Windows.")


if __name__ == "__main__":
    # Check if the SDK is already downloaded, if not download it
    download_sdk.check_and_download_sdk()
