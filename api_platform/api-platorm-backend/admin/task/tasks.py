from common.redis_util.redis_util import Redis
from common.db.session import DB
from admin.model.api_info import APIInfo
from admin.model.user import ClientUser
from sqlalchemy import select

redis_client = Redis._instance
user_common_key = "user_limited:"
api_common_key = "api_limited:"

async def user_limited():
    async for session in DB.get_session():
        apiList = (await session.scalars(select(APIInfo))).all()
        userList = (await session.scalars(select(ClientUser))).all()
        for user in userList:
            for api in apiList:
                key = user_common_key + user.id + "_" + api.id
                redis_client.set(key=key,value=100)


async def api_limited():
    async for session in DB.get_session():
        apiList = (await session.scalars(select(APIInfo))).all()
        for api in apiList:
            key = api_common_key + api.id
            redis_client.set(key=key,value=200)