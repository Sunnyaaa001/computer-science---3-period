from fastapi import APIRouter,Depends
from common.response.response_body import ResponseResult,PageResult
from common.schedule.request_body.request_param import TaskInfoParam
from common.db.session import AsyncSession,DB
from common.schedule.service.schedule_service import insert_schedule_data,get_task_info,task_page_list,update_task,delete_task
from common.schedule.response_body.task_response import TaskResponse 

router = APIRouter(prefix="/schedule")

@router.post("/task/insert")
async def insert_task(task:TaskInfoParam,db:AsyncSession = Depends(DB.get_session)) -> ResponseResult:
    return await insert_schedule_data(task,db)

@router.get("/task/list")
async def select_task_pages(page:int,size:int,task:TaskInfoParam,db:AsyncSession = Depends(DB.get_session)) ->PageResult[TaskResponse]:
    return await task_page_list(page=page,size=size,task_param=task,db=db)


@router.get("/task/detail/{id}")
async def get_task_details(id:int,db:AsyncSession = Depends(DB.get_session)) ->ResponseResult[TaskResponse]:
    task_info = await get_task_info(id,db)
    result = TaskResponse.model_validate(task_info)
    return ResponseResult.success(data=result,message="success!")

@router.put("/task/update")
async def update_task_info(task:TaskInfoParam,db:AsyncSession = Depends(DB.get_session))->ResponseResult:
    return await update_task(task,db)


@router.delete("/task/delete/{id}")
async def delete_task_info(id:int,db:AsyncSession = Depends(DB.get_session)) -> ResponseResult:
    return await delete_task(id,db)

@router.get("/task/start/{id}")
async def start_task(id:int,db:AsyncSession = Depends(DB.get_session)) -> ResponseResult:
    ...
@router.get("/task/stop/{id}")
async def stop_task(id:int,db:AsyncSession = Depends(DB.get_session)) -> ResponseResult:
    ...
@router.get("/task/execute/once/{id}")
async def execute_once(id:int,db:AsyncSession = Depends(DB.get_session)) -> ResponseResult:
    ...
