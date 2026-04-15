from fastapi import APIRouter,UploadFile, File, Form
from common.response.response_body import ResponseResult
from typing import Optional
from common.filestorage.service.file_storage_service import file_upload,download_file,preview_file
from fastapi.responses import StreamingResponse

router = APIRouter(prefix="/oss")

@router.post("/upload")
async def upload_file(bucket_name:str = Form(...)
                      ,folder:Optional[str] = Form(None),
                      file:UploadFile = File(...))->ResponseResult:
    url = await file_upload(bucket_name=bucket_name,folder=folder,file=file)
    return ResponseResult.success(data=url,message="upload successfully!")

@router.get("/preview")
async def preview_url(bucket_name:str,file_path:str)->ResponseResult:
    url = await preview_file(bucket_name=bucket_name,file_path=file_path)
    return ResponseResult.success(data=url)

@router.get("/download")
async def download(bucket_name:str,file_path:str)->StreamingResponse:
    return await download_file(bucket_name=bucket_name,file_path=file_path)
