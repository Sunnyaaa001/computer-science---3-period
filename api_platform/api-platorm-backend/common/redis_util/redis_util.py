from typing import Any
import redis.asyncio as redis

class RedisClient:

    def __init__(self,host:str = "localhost",port:int=6379,db:int = 0, password:str | None = None):
        self._client= redis.Redis(
            host=host,
            port = port,
            db=db,
            password=password,
            decode_responses=True
        )

    async def set(self,key:str, value: Any, expire:int | None = None):
        return await self._client.set(name=key,value=value,ex=expire)

    async def get(self,key:str)->Any:
        return await self._client.get(name=key)
    
    async def delete(self,key:str):
        return await self._client.delete(key)
    
    async def exist(self,key:str)->bool:
        return await self._client.exists(key) > 0
    
    async def close(self):
        await self._client.close()
