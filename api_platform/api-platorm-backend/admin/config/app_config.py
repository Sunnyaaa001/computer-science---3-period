from fastapi import FastAPI
from common.config.application_config import create_lifespan
from common.exception.handler.exception_handler import register_exception
from common.router.router import include_scheduled_task_router

app = FastAPI(lifespan=create_lifespan("admin"))

register_exception(app=app)

include_scheduled_task_router(app=app)