import boto3

bucket_name = "sowmya-python-storage"

s3 = boto3.client("s3")

s3.upload_file(
    "data/large_data.csv",
    bucket_name,
    "large_data.csv"
)

print("Large CSV file uploaded successfully")