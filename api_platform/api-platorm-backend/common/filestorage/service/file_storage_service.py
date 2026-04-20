from fastapi import UploadFile
from common.filestorage.s3.filestorage import OSSStorage
import uuid
from pathlib import Path
from fastapi.responses import StreamingResponse
from urllib.parse import quote

async def file_upload(bucket_name:str,folder:str,file:UploadFile)->str:
    original_file_name = file.filename
    extension = Path(original_file_name).suffix
    new_file_path = f"{folder}{uuid.uuid4().hex}{extension}"
    OSSStorage.upload(bucket_name=bucket_name,file=file,file_path=new_file_path)
    return new_file_path


async def preview_file(bucket_name:str,file_path:str)->str:
    return OSSStorage.preview(bucket_name=bucket_name,file_path=file_path)

async def download_file(bucket_name:str,file_path:str)->StreamingResponse:
    res =  OSSStorage.download_file(bucket=bucket_name,file_path=file_path)
    file_stream = res["Body"]
    mime_type = res.get("ContentType","application/octet-stream")
    filename = file_path.split("/")[-1]
    encoded_file_name = quote(filename)
    return StreamingResponse(
        content = file_stream,
        media_type=mime_type,
        headers={
            "Content-Disposition": f"attachment; filename={encoded_file_name}; filename*=utf-8''{encoded_file_name}"
        }
    )

async def delete_file(bucket_name:str,file_path:str):
    OSSStorage.delete_file(bucket_name=bucket_name,file_path=file_path)

