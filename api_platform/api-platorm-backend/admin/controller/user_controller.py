from common.db.session import DB,AsyncSession
from common.response.response_body import ResponseResult
from fastapi.routing import APIRouter
from fastapi import Depends
from admin.request.user_request import UserParam,LoginUser
from admin.service.user_service import sys_user_register,sys_user_login


router = APIRouter(prefix="/system/user")

@router.post("/register")
async def register(user:UserParam) -> ResponseResult:
    return await sys_user_register(user)

@router.post("/login")
async def login(login_user:LoginUser,db:AsyncSession = Depends(DB.get_session))-> ResponseResult:
    return await sys_user_login(user=login_user,db=db)