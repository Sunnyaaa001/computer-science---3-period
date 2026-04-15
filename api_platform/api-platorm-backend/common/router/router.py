from common.schedule.controller.schedule_api import router as task_router
from common.schedule.controller.schedule_log_api import router as task_log_router
from common.filestorage.controller.file_storeage_controller import router as oss_router
from fastapi import FastAPI

def include_scheduled_task_router(app:FastAPI):
    # connect to APscheduler API
    app.include_router(task_router)
    app.include_router(task_log_router)
    # connect to OSS API
    app.include_router(oss_router)
