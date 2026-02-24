from fastapi import APIRouter,Depends
from common.response.response_body import ResponseResult,PageResult
from common.db.session import AsyncSession,DB
from common.schedule.response_body.task_response import TaskLogResponse
from common.schedule.service.schedule_log_service import task_log_detail,log_list_by_page

router = APIRouter(prefix="/schedule/log")


@router.get("/info/{log_id}")
async def log_info(log_id:int,db:AsyncSession = Depends(DB.get_session))->ResponseResult[TaskLogResponse]:
    log = await task_log_detail(log_id,db)
    return ResponseResult[TaskLogResponse].success(data=log,message="success!")

@router.get("/page/list/{task_id}")
async def log_page_list(task_id:int,page:int,size:int,db:AsyncSession = Depends(DB.get_session))->PageResult[TaskLogResponse]:
    return await log_list_by_page(task_id=task_id,page=page,size=size,db=db)