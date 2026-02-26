from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from common.user.user_utils import set_current_user,clear_current_user
from common.exception.base.base_exception import BusinessException
from common.exception.error.error_code import ErrorCode
from common.jwt.jwt_utils import TokenUtill
from common.redis_util.redis_util import Redis
from fastapi.responses import JSONResponse
from common.response.response_body import ResponseResult
import json

class APIFilter(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        # white API list : user request without token
        white_list = [
            "/system/user/login",
            "/system/user/register"
        ]
        # TODO: get static resource without token
        static_resource = []
        try:
            if request.url.path in white_list:
                return await call_next(request)
            #check token
            error= ErrorCode.INVALID_TOKEN
            token = request.headers.get("Authorization")
            if not token or not token.startswith("Bearer "):
                return JSONResponse(status_code=200,content=ResponseResult.response(code=error.code,message=error.msg).model_dump())
            user = TokenUtill.verify_token(token=token)
            if user is None:
                return JSONResponse(status_code=200,content=ResponseResult.response(code=error.code,message=error.msg).model_dump())
            #check token whether exists in Redis
            redis = Redis._instance
            user_info_key = f"user_token:{user['id']}"
            json_str =  await redis.get(user_info_key)
            if json_str is None:
                error_relogin = ErrorCode.RELOGIN
                return JSONResponse(status_code=200,content=ResponseResult.response(code=error_relogin.code,message=error_relogin.msg).model_dump())
            #refresh token in Redis
            await redis.set(key=user_info_key,value=json_str,expire=TokenUtill._expire_time*60)
            # set current user in Application context
            set_current_user(user=json.loads(json_str))
            return await call_next(request)
        finally:
            clear_current_user()