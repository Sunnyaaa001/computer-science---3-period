from common.db.session import AsyncSession
from common.schedule.response_body.task_response import TaskLogResponse
from common.schedule.model.task_info import SysTaskLog
from common.exception.base.base_exception import BusinessException
from common.response.response_body import PageResult,paginate
from sqlalchemy import select

async def task_log_detail(log_id:int,db:AsyncSession)->TaskLogResponse:
    task_log = await db.scalar(select(SysTaskLog).where(SysTaskLog.id == log_id))
    if not task_log:
        raise BusinessException("log detail not found!")
    task_response = TaskLogResponse.model_validate(task_log)
    return task_response

async def log_list_by_page(task_id:int,page:int,size:int,db:AsyncSession)->PageResult[TaskLogResponse]:
    return await paginate(db=db,
                          page=page,
                          size=size,
                          model=SysTaskLog,
                          response_model=TaskLogResponse,
                          filters=lambda m: [m.task_id == task_id],
                          order_by=SysTaskLog.create_time.desc())