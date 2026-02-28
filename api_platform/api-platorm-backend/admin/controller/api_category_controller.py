from common.db.session import DB,AsyncSession
from common.response.response_body import ResponseResult
from fastapi import Depends
from fastapi.routing import APIRouter
from admin.request.api_category_request import APICategoryParam
from admin.response.api_category_response import APICategoryResponse,APICategoryTree
from admin.service.api_category_service import category_insert,category_info,category_tree_list,update_category_info,delete_category_info


router = APIRouter(prefix="/api/category")

@router.post("/insert")
async def api_category_insert(parm:APICategoryParam)->ResponseResult:
    return await category_insert(param = parm)

@router.get("/tree")
async def category_list(db:AsyncSession=Depends(DB.get_session))->ResponseResult[list[APICategoryTree]]:
    result = await category_tree_list(param=None,db=db)
    return ResponseResult.success(data=result,message="success!")

@router.get("/detail/{id}")
async def category_detail(id:int,db:AsyncSession = Depends(DB.get_session))->ResponseResult[APICategoryResponse]:
    return await category_info(id=id,db=db)

@router.put("/update")
async def category_update(param:APICategoryParam)->ResponseResult:
    return await update_category_info(param=param)

@router.delete("/delete/{id}")
async def delete_category(id:int)->ResponseResult:
    return await delete_category_info(id=id)
