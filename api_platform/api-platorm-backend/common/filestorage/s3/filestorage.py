import boto3
from mypy_boto3_s3 import S3Client
from botocore.config import Config
from botocore.exceptions import ClientError
from threading import Lock
from fastapi import UploadFile

class OSSStorage:
    _instance:S3Client = None
    _lock = Lock()

    @classmethod
    def init(cls,endpoint:str,access_key,secret_key:str,region: str = "eu-central-1"):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = boto3.client(
                        "s3",
                        endpoint_url=endpoint,
                        aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key,
                        config=Config(signature_version="s3v4"),
                        region_name=region
                    )
    @classmethod                
    def upload(cls, bucket_name:str,file:UploadFile,file_path:str)->bool:
        client = cls._instance
        try:
            client.upload_fileobj(
            Fileobj=file.file,
            Bucket=bucket_name,
            Key=file_path,
            ExtraArgs={
                "ContentType":file.content_type
            }
        )
        except ClientError as e:
            print(e)
            return False
        return True

    @classmethod    
    def preview(cls,bucket_name:str,file_path:str)->str:
        client = cls._instance
        try:
          response = client.generate_presigned_url(
            ClientMethod="get_object",
            Params={
                "Bucket":bucket_name,
                "Key":file_path,
                "ResponseContentDisposition": "inline"
            }
        )
        except ClientError as e:
            print(e)
            return None
        return response
    
    @classmethod
    def download_file(cls,bucket:str,file_path:str)->dict:
        client = cls._instance
        response = client.get_object(
            Bucket=bucket,
            Key=file_path
        )
        return response