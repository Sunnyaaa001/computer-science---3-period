from __future__ import annotations
from typing import Any
import redis.asyncio as redis

class Redis:
    _instance : RedisClient | None = None

    @classmethod
    def get_instance(cls)->RedisClient:
        if cls._instance is None:
            raise RuntimeError("Redis doesn't initialize..")
        return cls._instance
    
    @classmethod
    async def initialize(cls,host:str = "localhost",port:int=6379,db:int = 0, password:str | None = None):
        if cls._instance is None:
            cls._instance = RedisClient(host=host,port=port,db=db,password=password)

        if not await cls._instance.ping():
            raise ConnectionError("Redis connection failed")

    @classmethod
    async def close(cls):
        await cls._instance.close()    



        


class RedisClient:

    def __init__(self,host:str = "localhost",port:int=6379,db:int = 0, password:str | None = None):
        self._client= redis.Redis(
            host=host,
            port = port,
            db=db,
            password=password,
            decode_responses=True
        )

    async def set(self,key:str, value: Any, expire:int | None = None,nx:bool = False):
        return bool(await self._client.set(name=key,value=value,ex=expire,nx=nx))

    async def get(self,key:str)->Any:
        return await self._client.get(name=key)
    
    async def delete(self,key:str):
        return await self._client.delete(key)
    
    async def exist(self,key:str)->bool:
        return await self._client.exists(key) > 0
    
    async def decrease(self,key:str, count:int = 1):
        return await self._client.decrby(key,count)
    
    async def increase(self,key:str,count:int = 1):
        return await self._client.incrby(key,count)
    
    async def close(self):
        await self._client.close()

    async def ping(self) -> bool:
        try:
            return await self._client.ping()
        except redis.ConnectionError:
            return False 

    async def add_set(self,key:str,value:str):
        await self._client.sadd(key,value)

    async def set_exist(self,key:str,value:str)->bool:
        result =  await self._client.sismember(key,value)
        return bool(result)

    async def remove_item_set(self,key:str,value:str)->bool:
        result =  await self._client.srem(key,value)
        return bool(result)               
