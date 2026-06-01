from scripts.config import *

from scripts.s3_operations import download_file

download_file(
    BUCKET_NAME,
    "sample_data.csv",
    DOWNLOAD_FILE,
    AWS_REGION
)