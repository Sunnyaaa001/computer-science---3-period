from common.db.session import DB,AsyncSession
from common.response.response_body import ResponseResult
from fastapi import Depends
from fastapi.routing import APIRouter
from admin.request.api_category_request import APICategoryParam
from admin.response.api_category_response import APICategoryResponse
from admin.service.api_category_service import category_insert,category_info


router = APIRouter(prefix="/api/category")

@router.post("/insert")
async def api_category_insert(parm:APICategoryParam)->ResponseResult:
    return await category_insert(param = parm)

@router.get("/detail/{id}")
async def category_detail(id:int,db:AsyncSession = Depends(DB.get_session))->ResponseResult[APICategoryResponse]:
    return await category_info(id=id,db=db)
