from fastapi import FastAPI
from contextlib import asynccontextmanager
from common.redis_util.redis_util import Redis
from common.config_read.config_read import ConfigReader
from common.jwt.jwt_utils import TokenUtill
from common.id_generator.id_util import Snowflake
from common.db.session import DB


@asynccontextmanager
async def lifespan(app:FastAPI):
    # load application.yaml file
    config_reader = ConfigReader()
    config_data = config_reader.load()
    #intilaize Redis
    await Redis.initialize(host=config_data["redis"]["host"],port=config_data["redis"]["port"],
                     db=config_data["redis"]["db"],password=config_data["redis"]["password"])
    #intialize token utils
    TokenUtill.init(secret_key=config_data["token"]["secret_key"])
    #initilize snowflake id util
    Snowflake.init(instance=int(config_data["snowflake"]["instance"]))
    #initialize DB
    DB.init(database_driver=config_data["database"]["driver"],ip=config_data["database"]["ip"],
            port=int(config_data["database"]["port"]),db_name=config_data["database"]["db"],
            username=config_data["database"]["username"],password=config_data["database"]["password"],
            config=config_data["database"]["config"],sql_log=bool(config_data["database"]["sql_log"]))
    print(f"{config_data['app']['name']} application started........")
    yield
    Redis.get_instance().close()
    print(f"{config_data['app']['name']} application closed........")
