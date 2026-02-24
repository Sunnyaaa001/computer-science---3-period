from common.db.session import AsyncSession
from common.schedule.request_body.request_param import TaskInfoParam
from common.response.response_body import ResponseResult,paginate
from common.schedule.model.task_info import SysTaskInfo
from common.docerator.docerator import Transactional
from sqlalchemy import select
from common.exception.base.base_exception import BusinessException
from common.schedule.response_body.task_response import TaskResponse
from common.schedule.scheduler.ap_scheduler import APScheduler

@Transactional
async def insert_schedule_data(task:TaskInfoParam,db:AsyncSession)->ResponseResult:
    param_data = task.model_dump()
    #check this func_name whether is unique
    taskInfo =  await db.scalar(select(SysTaskInfo).where(SysTaskInfo.func_name  == task.func_name))
    if taskInfo is not None:
        raise BusinessException("This function already exists!")
    sys_task_info = SysTaskInfo(**param_data)
    db.add(sys_task_info)
    return ResponseResult.success()


async def task_page_list(page:int,size:int,task_param:TaskInfoParam,db:AsyncSession):
    return await paginate(db=db,model=SysTaskInfo,response_model=TaskResponse,page=page,size=size)



async def get_task_info(task_id:int,db:AsyncSession)->SysTaskInfo:
    return await db.scalar(select(SysTaskInfo).where(SysTaskInfo.id == task_id))


async def task_list(db:AsyncSession)->list[SysTaskInfo]:
   result =  await db.scalars(select(SysTaskInfo).order_by(SysTaskInfo.update_time.desc()))
   return result.all()

@Transactional
async def update_task(task:TaskInfoParam, db:AsyncSession)->ResponseResult:
    #check function name
    taskInfo = await db.scalar(select(SysTaskInfo).where(SysTaskInfo.func_name == task.func_name,
                                                   SysTaskInfo.id != task.id))
    if taskInfo:
        raise BusinessException("This function already exists!")
    old_task = await db.scalar(select(SysTaskInfo).where(SysTaskInfo.id == task.id))
    if not old_task:
        raise BusinessException("Task not found!")
    # update task information
    task_dict = task.model_dump(exclude_unset=True,exclude={"id"})
    for key, value in task_dict.items():
        setattr(old_task, key, value)
    # TODO: update task in APscheduler    
    return ResponseResult.success(message="success!")


@Transactional
async def delete_task(id:int,db:AsyncSession) -> ResponseResult:
    #check task
    task = await db.scalar(select(SysTaskInfo).where(SysTaskInfo.id == id))
    if not task:
        raise BusinessException("Task not found!")
    db.delete(task)
    #TODO: remove task in APScheduler
    return ResponseResult.success(message="success!")

@Transactional
async def start(id:int,db:AsyncSession) ->ResponseResult:
    #get task info
    task = await db.scalar(select(SysTaskInfo).where(SysTaskInfo.id == id))
    if not task:
        raise BusinessException("Task not found!")
    task.status = "2"
    APScheduler.add_task(task_info=task._dict())
    return ResponseResult.success(message="success!")

@Transactional
async def stop(id:int,db:AsyncSession) ->ResponseResult:
    #get task info
    task = await db.scalar(select(SysTaskInfo).where(SysTaskInfo.id == id))
    if not task:
        raise BusinessException("Task not found!")
    task.status = "0"
    APScheduler.pause_task(task_id= task.id)
    return ResponseResult.success(message="success!")


async def execute_one_time(id:int, db:AsyncSession) -> ResponseResult:
    #get task info
    task = await db.scalar(select(SysTaskInfo).where(SysTaskInfo.id == id))
    if not task:
        raise BusinessException("Task not found!")
    APScheduler.execute_once(task._dict())
    return ResponseResult.success(message="success!")