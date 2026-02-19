from common.db.session import AsyncSession
from common.schedule.request_body.request_param import TaskInfoParam
from common.response.response_body import ResponseResult
from common.schedule.model.task_info import SysTaskInfo
from common.docerator.docerator import Transactional
from sqlalchemy import select

@Transactional
async def insert_schedule_data(task:TaskInfoParam,db:AsyncSession):
    param_data = task.model_dump()
    sys_task_info = SysTaskInfo(**param_data)
    db.add(sys_task_info)
    return ResponseResult.success()


async def task_list(db:AsyncSession)->list[SysTaskInfo]:
   result =  await db.scalars(select(SysTaskInfo).order_by(SysTaskInfo.update_time.desc()))
   return result.all()