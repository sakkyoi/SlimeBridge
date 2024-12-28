import requests
from io import BytesIO
from zipfile import ZipFile
from tqdm import tqdm


def check_and_download_sdk():
    # Check if the SDK is already downloaded
    try:
        import rebocap.rebocap_ws_sdk
    except ImportError:
        print("SDK not found. Downloading SDK...")
        # get sdk_url from file
        with open("rebocap/sdk_url", "r") as f:
            sdk_url = f.read().strip()

        # download the SDK
        sdk = BytesIO()
        response = requests.get(sdk_url, stream=True)
        total_size = int(response.headers.get("content-length", 0))
        block_size = 1024
        with tqdm(total=total_size, unit="B", unit_scale=True) as pbar:
            for data in response.iter_content(block_size):
                pbar.update(len(data))
                sdk.write(data)

        # extract the SDK
        with ZipFile(sdk) as zf:
            for file in [f for f in zf.filelist if f.filename.startswith("rebocap_ws_sdk/")]:
                zf.extract(file, "rebocap/rebocap_ws_sdk")

        print("SDK downloaded successfully.")


if __name__ == "__main__":
    check_and_download_sdk()
