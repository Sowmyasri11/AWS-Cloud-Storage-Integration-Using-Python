import boto3
import os

bucket_name = "sowmya-python-storage"

os.makedirs("downloads", exist_ok=True)

s3 = boto3.client("s3")

s3.download_file(
    bucket_name,
    "sample_data.csv",
    "downloads/sample_data.csv"
)

print("File downloaded successfully")