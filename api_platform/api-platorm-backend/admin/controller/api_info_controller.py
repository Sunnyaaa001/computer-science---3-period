from common.db.session import DB,AsyncSession
from fastapi.routing import APIRouter
from fastapi import Depends
from common.response.response_body import ResponseResult
from admin.request.api_info_request import APIInfoParam

router = APIRouter(prefix="/api/info")

@router.post("/insert")
async def insert_api_info(param:APIInfoParam)->ResponseResult:
    ...

@router.get("/{id}")
async def api_info(id:int,db:AsyncSession = Depends(DB.get_session)) -> ResponseResult:
    ...
@router.put("/update")
async def update_api_info(param:APIInfoParam)->ResponseResult:
    ...

@router.delete("/delete/{id}")
async def delete_api_info(id:int)->ResponseResult:
    ...
