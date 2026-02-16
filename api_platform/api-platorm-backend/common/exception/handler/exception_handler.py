from fastapi import FastAPI,Request
from common.exception.base.base_exception import BusinessException
from common.response.response_body import ResponseResult


def register_exception(app:FastAPI):
    
    @app.exception_handler(BusinessException)
    async def exception_handdler(req:Request,exc:BusinessException):
        return ResponseResult.response(code=exc.code,message=exc.message)