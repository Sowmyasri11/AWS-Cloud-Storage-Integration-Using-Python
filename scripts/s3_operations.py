import boto3
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_s3_client(region):
    return boto3.client(
        "s3",
        region_name=region
    )

def upload_file(bucket_name, file_path, object_name, region):

    s3 = get_s3_client(region)

    s3.upload_file(
        file_path,
        bucket_name,
        object_name
    )

    logging.info("Upload Successful")

def download_file(bucket_name, object_name, file_path, region):

    s3 = get_s3_client(region)

    s3.download_file(
        bucket_name,
        object_name,
        file_path
    )

    logging.info("Download Successful")

def list_files(bucket_name, region):

    s3 = get_s3_client(region)

    response = s3.list_objects_v2(
        Bucket=bucket_name
    )

    logging.info("Listing files in bucket")

    for obj in response.get("Contents", []):
        print(obj["Key"])