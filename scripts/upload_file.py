from config import *
from s3_operations import upload_file

upload_file(
    BUCKET_NAME,
    UPLOAD_FILE,
    "sample_data.csv",
    AWS_REGION
)