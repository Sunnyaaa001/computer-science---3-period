from fastapi import APIRouter,Depends
from common.response.response_body import ResponseResult
from common.schedule.request_body.request_param import TaskInfoParam
from common.db.session import AsyncSession,DB

router = APIRouter(prefix="/schedule")

@router.post("/insert/task")
async def insert_task(task:TaskInfoParam,db:AsyncSession = Depends(DB.get_session)) -> ResponseResult:
    