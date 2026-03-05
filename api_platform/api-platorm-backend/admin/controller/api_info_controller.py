from common.db.session import DB,AsyncSession
from fastapi.routing import APIRouter
from fastapi import Depends
from common.response.response_body import ResponseResult,PageResult
from admin.request.api_info_request import APIInfoParam
from admin.service.api_info_service import insert_api,api_details,delete_api,page_api_info,update_api
from admin.response.api_info_response import APIInfoResponse,APIInfoSimpleResponse

router = APIRouter(prefix="/api/info")

@router.post("/insert")
async def insert_api_info(param:APIInfoParam)->ResponseResult:
    return await insert_api(param=param)


@router.get("/pagelist")
async def page_list(page:int,size:int, db:AsyncSession = Depends(DB.get_session)) -> ResponseResult[PageResult[APIInfoSimpleResponse]]:
    return await page_api_info(page=page,size=size,db=db)

@router.put("/update")
async def update_api_info(param:APIInfoParam)->ResponseResult:
    return await update_api(param = param)

@router.get("/{id}")
async def api_info(id:int,db:AsyncSession = Depends(DB.get_session)) -> ResponseResult[APIInfoResponse]:
    return await api_details(id=id,db=db)


@router.delete("/delete/{id}")
async def delete_api_info(id:int)->ResponseResult:
    return await delete_api(id=id)
