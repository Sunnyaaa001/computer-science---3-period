from fastapi import FastAPI,Request
from common.exception.base.base_exception import BusinessException
from common.response.response_body import ResponseResult
from fastapi.responses import JSONResponse
from pydantic import ValidationError

def register_exception(app:FastAPI):
    
    @app.exception_handler(BusinessException)
    async def exception_handler(req:Request,exc:BusinessException):
        content =  ResponseResult.response(code=exc.code,message=exc.message)
        return JSONResponse(status_code=200,content=content.model_dump())
    
    @app.exception_handler(ValidationError)
    async def validation_handler(req:Request,exc:ValidationError):
        errors = []
        for error in exc.errors():
            ctx = error.get("ctx",{})
            error_msg = ctx.get("error_msg") if isinstance(ctx,dict) else None
            final_msg = error_msg or error.get("msg")
            errors.append(final_msg)
        result = ResponseResult.response(code=422,message=errors[0])
        return JSONResponse(status_code=200,content=result.model_dump())    
          
                