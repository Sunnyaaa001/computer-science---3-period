from common.redis_util.redis_util import Redis
from common.user.user_utils import get_current_user
from functools import wraps
from common.db.session import DB

def debounce(wait_time:int = 1):
    def decorator(func:callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            redis_client = Redis.get_instance()
            #get current user id
            user = get_current_user()
            if user is None:
                # TODO: set global exception 
                raise PermissionError("Not login!")
            user_id = user["id"]
            #combine key
            key = f"debounce:{func.__module__}.{func.__name__}:{user_id}"
            #check whether current use this api
            if not await redis_client.set(key=key,value="1",expire=wait_time,nx=True):
                raise RuntimeError("please request later!")
            return await func(*args,**kwargs)
        return wrapper
    return decorator


def limitation():
    def decorator(func:callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            redis_client = Redis.get_instance()
            #combine the key
            key = f"limitation:{func.__module__}.{func.__name__}"
            if int(await redis_client.get(key=key)) <= 0 :
               raise RuntimeError("No request Numbers!")
            # reduce number of this api
            await redis_client.decrease(key=key)
            return func(*args,**kwargs)
        return wrapper
    return decorator


def Transactional(func:callable):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        # get async session
        async for session in DB.get_session():
            try:
                kwargs["session"] = session
                result = await func(*args,**kwargs)
                await session.commit()
                return result
            except Exception as e:
                await session.rollback()
                raise e
    return wrapper        

# TODO: write Log decorators

    
