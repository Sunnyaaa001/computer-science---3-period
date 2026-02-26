from contextlib import asynccontextmanager
from common.redis_util.redis_util import Redis
from common.config_read.config_read import ConfigReader
from common.jwt.jwt_utils import TokenUtill
from common.id_generator.id_util import Snowflake
from common.db.session import DB
from common.schedule.scheduler.ap_scheduler import APScheduler
from fastapi import FastAPI

def create_lifespan(module_name: str):
    @asynccontextmanager
    async def lifespan(app:FastAPI):
        config_reader = ConfigReader(module_name)
        config_data = config_reader.load()

        await Redis.initialize(
            host=config_data["redis"]["host"],
            port=config_data["redis"]["port"],
            db=config_data["redis"]["db"],
            password=config_data["redis"]["password"]
        )

        TokenUtill.init(secret_key=config_data["token"]["secret_key"],expire_time=config_data["token"]["expire_time"])
        Snowflake.init(instance=int(config_data["snowflake"]["instance"]))
        DB.init(
            database_driver=config_data["database"]["driver"],
            ip=config_data["database"]["ip"],
            port=int(config_data["database"]["port"]),
            db_name=config_data["database"]["db"],
            username=config_data["database"]["username"],
            password=config_data["database"]["password"],
            config=config_data["database"]["config"],
            sql_log=bool(config_data["database"]["sql_log"])
        )

        APScheduler.init(
            pool=config_data["apscheduler"]["pool"],
            max_instance=config_data["apscheduler"]["max_instance"],
            coalesce=config_data["apscheduler"]["coalesce"],
            timezone=config_data["apscheduler"]["timezone"]
        )
        APScheduler.add_listener()
        APScheduler.start()

        print(f"{config_data['app']['name']} application started........")

        yield

        instance = Redis.get_instance()
        if instance:
            await instance.close()
        print(f"{config_data['app']['name']} application closed........")
    
    return lifespan