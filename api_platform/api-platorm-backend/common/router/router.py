from common.schedule.controller.schedule_api import router as task_router
from common.schedule.controller.schedule_log_api import router as task_log_router
from fastapi import FastAPI

def include_scheduled_task_router(app:FastAPI):
    app.include_router(task_router)
    app.include_router(task_log_router)
