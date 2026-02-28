from sqlalchemy import select,func
from common.db.session import AsyncSession
from common.docerator.docerator import Transactional
from common.response.response_body import ResponseResult
from admin.request.api_category_request import APICategoryParam
from common.exception.base.base_exception import BusinessException
from admin.model.api_category import APICategory
from admin.model.api_info import APIInfo
from common.exception.error.error_code import ErrorCode
from admin.response.api_category_response import APICategoryResponse,APICategoryTree
from common.user.user_utils import get_current_user
from datetime import datetime

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

async def category_tree_list(param:APICategoryParam,db:AsyncSession)->list[APICategoryTree]:
    # get data in database
    # TODO: add find_in_set function
    data_list = (await db.scalars(select(APICategory))).all()
    if len(data_list) == 0:
        return []
    response_list = [APICategoryTree.model_validate(item) for item in data_list]
    return APICategoryTree.build_tree(data=response_list,order_by="sort",reverse=False)

async def category_info(id:int,db:AsyncSession)->ResponseResult[APICategoryResponse]:
    category = await db.scalar(select(APICategory).where(APICategory.id == id))
    if category is None:
        raise BusinessException(err=ErrorCode.CATEGORY_NOT_FOUND)
    result = APICategoryResponse.model_validate(category)
    return ResponseResult.success(data=result,message="success!")

@Transactional
async def update_category_info(param:APICategoryParam,db:AsyncSession)->ResponseResult:
    category = await db.scalar(select(APICategory).where(APICategory.id == param.id))
    if not category:
        raise BusinessException(err=ErrorCode.CATEGORY_NOT_FOUND)
    other = await db.scalar(select(APICategory).where(APICategory.parent_id == param.parent_id,
                                                      APICategory.id != param.id,
                                                      APICategory.category_name == param.category_name))
    if other:
        raise BusinessException(err=ErrorCode.CATEGORY_NAME_EXIST)
    if category.parent_id != param.parent_id:
        # get old ancestors
        old_ancestors = f"{category.ancestors},{category.id}"
        new_category = ""
        if param.parent_id == 0:
           new_category = "0"
        else:
            # find parent category
            parent_category = await db.scalar(select(APICategory).where(APICategory.id == param.parent_id))
            new_category = f"{parent_category.ancestors},{parent_category.id}"
        # update ancestors of all of children in current category
        children_list = (await db.scalars(select(APICategory).where(func.find_in_set(str(category.id),APICategory.ancestors)))).all()
        # loop children list
        for item in children_list:
           item.ancestors = item.ancestors.replace(old_ancestors,new_category)
        category.ancestors = new_category          
    category.parent_id = param.parent_id
    category.category_name = param.category_name
    category.sort = param.sort
    return ResponseResult.success(message="success!")        

@Transactional
async def delete_category_info(id:int,db:AsyncSession)->ResponseResult:
    category = await db.scalar(select(APICategory).where(APICategory.id == id))
    if not category:
        raise BusinessException(err=ErrorCode.CATEGORY_NOT_FOUND)
    #check this category whether has children
    children_list = (await db.scalars(select(APICategory).where(APICategory.parent_id == id))).all()
    if len(children_list) != 0:
        raise BusinessException(err=ErrorCode.SUB_CATEGORY_EXIST)
    else:
        # check whether this category has API
        api_list = (await db.scalars(select(APIInfo).where(APIInfo.category_id == category.id))).all()
        if len(api_list) != 0:
            raise BusinessException(err=ErrorCode.SUB_API_EXIST)
    # delete category
    await db.delete(category)
    return ResponseResult.success(message="success!")        
