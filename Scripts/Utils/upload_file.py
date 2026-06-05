import boto3
from dotenv import load_dotenv
import os
load_dotenv()

s3=boto3.client('s3')

bucket_name = os.getenv('bucket_name')
s3_key=os.getenv('s3_key')
s3_keys=os.getenv('s3_keys')
file_path=os.getenv('file_path')
file_path1=os.getenv('file_path1')

s3.upload_file(file_path,bucket_name,s3_key)
s3.upload_file(file_path1,bucket_name,s3_keys)