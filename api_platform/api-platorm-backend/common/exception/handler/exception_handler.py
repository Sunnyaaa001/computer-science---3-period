from fastapi import FastAPI,Request
from common.exception.base.base_exception import BusinessException
from common.response.response_body import ResponseResult
from fastapi.responses import JSONResponse

def register_exception(app:FastAPI):
    
    @app.exception_handler(BusinessException)
    async def exception_handler(req:Request,exc:BusinessException):
        content =  ResponseResult.response(code=exc.code,message=exc.message)
        return JSONResponse(status_code=200,content=content.model_dump())