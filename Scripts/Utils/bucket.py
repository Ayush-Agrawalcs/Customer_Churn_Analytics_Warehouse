import boto3
from dotenv import load_dotenv
import os
load_dotenv()
region = 'ap-south-1'  

s3 = boto3.client('s3', region_name=region)

bucket_name = os.getenv('bucket_name')

s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': region
    }
)

print("Bucket created successfully")