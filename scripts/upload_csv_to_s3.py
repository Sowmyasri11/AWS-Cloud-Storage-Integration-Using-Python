import boto3
from botocore.exceptions import NoCredentialsError

bucket_name = "sowmya-python-storage"
file_path = "data/sample_data.csv"
object_name = "sample_data.csv"

s3 = boto3.client("s3")

try:
    s3.upload_file(file_path, bucket_name, object_name)
    print("File uploaded successfully!")

except FileNotFoundError:
    print("File not found.")

except NoCredentialsError:
    print("AWS credentials not available.")