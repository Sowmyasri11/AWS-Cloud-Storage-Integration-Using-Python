from scripts.config import *

from scripts.s3_operations import list_files

list_files(
    BUCKET_NAME,
    AWS_REGION
)