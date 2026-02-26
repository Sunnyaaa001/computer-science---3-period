from common.db.session import AsyncSession
from common.redis_util.redis_util import Redis
from admin.request.user_request import UserParam,LoginUser
from common.response.response_body import ResponseResult
from common.docerator.docerator import Transactional
from common.exception.base.base_exception import BusinessException
from admin.model.user import SysUser
from common.password.security import PasswordManager
from sqlalchemy import select
from common.jwt.jwt_utils import TokenUtill
from common.exception.error.error_code import ErrorCode
from datetime import datetime
from common.user.user_utils import get_current_user,clear_current_user
import json
import uuid

key = "sys_user_account"

@Transactional
async def sys_user_register(sys_user:UserParam,db:AsyncSession) -> ResponseResult:
    redis_client = Redis._instance
    if await redis_client.set_exist(key=key,value=sys_user.username):
        raise BusinessException(ErrorCode.ACCOUNT_EXIST)
    hashed_password =  PasswordManager.hash(sys_user.password)
    create_time = datetime.now()
    update_time = create_time
    user = SysUser(
        username = sys_user.username,
        password = hashed_password,
        avatar = sys_user.avatar,
        create_time = create_time,
        update_time = update_time
    )
    db.add(user)
    await redis_client.add_set(key=key,value=sys_user.username)
    return ResponseResult.success(message="success!")


async def sys_user_login(user:LoginUser,db:AsyncSession)->ResponseResult:
    redis_client = Redis._instance
    if  not await redis_client.set_exist(key=key,value=user.username):
        raise BusinessException(err=ErrorCode.ACCOUNT_NOT_EXIST)
    ## get user hashed password in Database
    current_user = await db.scalar(select(SysUser).where(SysUser.username == user.username))
    # check password
    result = PasswordManager.vertify(user.password,current_user.password) 
    if not result:
        raise BusinessException(err=ErrorCode.INCORRECT_ACCOUNT_OR_PASSWORD)
    # generate jwt token
    info={}
    info["id"] = current_user.id
    info["username"] = current_user.username
    info["avatar"] = current_user.avatar
    info["signature"] = datetime.now().timestamp()
    info["uuid"] = str(uuid.uuid4())
    token = TokenUtill.create_token(info)
    # put token into redis
    user_info_key = f"user_token:{current_user.id}"
    await redis_client.set(key = user_info_key,value = json.dumps(info),expire=TokenUtill._expire_time*60)
    token_dict = {
        "token":token
    }
    return ResponseResult.success(data=token_dict,message="login successfully!")


async def user_logout() -> ResponseResult:
    current_user = get_current_user()
    redis_client = Redis.get_instance()
    user_info_key = f"user_token:{current_user['id']}"
    await redis_client.delete(key=user_info_key)
    clear_current_user()
    return ResponseResult.success(message="log out successfully!")

async def user_profile()->ResponseResult[dict]:
    user = get_current_user()
    return ResponseResult.success(message="success!",data=user)