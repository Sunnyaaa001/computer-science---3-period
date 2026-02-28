from sqlalchemy import select,func
from common.db.session import AsyncSession
from common.docerator.docerator import Transactional
from common.response.response_body import ResponseResult
from admin.request.api_category_request import APICategoryParam
from common.exception.base.base_exception import BusinessException
from admin.model.api_category import APICategory
from common.exception.error.error_code import ErrorCode
from admin.response.api_category_response import APICategoryResponse
from common.user.user_utils import get_current_user
from datetime import datetime
from fastapi.encoders import jsonable_encoder

@Transactional
async def category_insert(param:APICategoryParam,db:AsyncSession)->ResponseResult:
    #check the name in same parent category
    category = await db.scalar(select(APICategory).where(APICategory.parent_id == param.parent_id,APICategory.category_name == param.category_name))
    if category:
        raise BusinessException(err=ErrorCode.NOT_UNIQUE_CATEGORY_NAME)
    #find parent category
    ancestors = ""
    parent_category = None
    if param.parent_id == 0:
        ancestors = "0"
    else:
        parent_category = await db.scalar(select(APICategory).where(APICategory.id == param.parent_id))
        if not parent_category:
           raise BusinessException(err=ErrorCode.CATEGORY_PARENT_NOT_FOUND)
        else:
            ancestors = f"{parent_category.ancestors},{param.parent_id}"
    #get max sort in parent category
    stmt = (select(func.max(APICategory.sort)).where(APICategory.parent_id == param.parent_id).with_for_update())
    result = await db.execute(stmt)
    max_sort =  result.scalar() or 0
    #get current user
    user = get_current_user()
    create_time = datetime.now()
    update_time = create_time
    api_category = APICategory(
        parent_id = param.parent_id,
        category_name = param.category_name,
        sort = max_sort + 1,
        ancestors = ancestors,
        creator_id = int(user["id"]),
        create_time = create_time,
        update_time = update_time
    )
    db.add(api_category)
    return ResponseResult.success(message="success!")

async def category_info(id:int,db:AsyncSession)->ResponseResult[APICategoryResponse]:
    category = await db.scalar(select(APICategory).where(APICategory.id == id))
    if category is None:
        raise BusinessException(err=ErrorCode.CATEGORY_NOT_FOUND)
    result = APICategoryResponse.model_validate(category)
    return ResponseResult.success(data=result,message="success!")
