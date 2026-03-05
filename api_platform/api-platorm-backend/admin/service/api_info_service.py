from common.db.session import AsyncSession
from common.response.response_body import ResponseResult,paginate,PageResult
from admin.request.api_info_request import APIInfoParam,APIResponsePropertyParam
from common.docerator.docerator import Transactional
from admin.model.api_info import APIInfo,APIParamInfo,APIPluginInfo,APIResponseExample,APIResponsePropertyInfo
from common.exception.base.base_exception import BusinessException
from common.exception.error.error_code import ErrorCode
from sqlalchemy import select,delete,update
from sqlalchemy.orm import selectinload, joinedload,noload
from datetime import datetime
from common.user.user_utils import get_current_user
from common.id_generator.id_util import Snowflake
from admin.response.api_info_response import APIInfoResponse,APIResponsePropertyResponse,APIInfoSimpleResponse


@Transactional
async def insert_api(param:APIInfoParam,db:AsyncSession)->ResponseResult:
    # check api name wether exists
    api = await db.scalar(select(APIInfo).where(APIInfo.api_name == param.api_name, APIInfo.category_id == param.category_id))
    if api:
        raise BusinessException(err=ErrorCode.API_NAME_EXIST)
    #check api whether exists
    origin = await db.scalar(select(APIInfo).where(APIInfo.api_host == param.api_host,APIInfo.api_port == param.api_port,
                                             APIInfo.api_method == param.api_method,APIInfo.api_path == param.api_path))
    if origin:
        raise BusinessException(err=ErrorCode.API_EXIST)
    # add api information into database
    db_columns = APIInfo.__table__.columns.keys()
    full_data = param.model_dump()
    api_data = {k: v for k, v in full_data.items() if k in db_columns}
    api_info = APIInfo(**api_data)
    create_time = datetime.now()
    update_time = create_time
    api_info.create_time =create_time
    api_info.update_time = update_time
    api_info.id = Snowflake.get_id()
    # get current user
    user = get_current_user()
    api_info.creator = user["id"]
    db.add(api_info)
    add_api_components(param=param,create_time=create_time,update_time=update_time,api_id=api_info.id,db=db)
    return ResponseResult.success(message="success!")    


async def page_api_info(page:int,size:int,db:AsyncSession)->ResponseResult[PageResult[APIInfoSimpleResponse]]:
    user = get_current_user()
    my_options = [noload(APIInfo.params), noload(APIInfo.plugins),noload(APIInfo.response_examples),noload(APIInfo.response_properties)]
    result = await paginate(db=db,
                            model=APIInfo,
                            response_model=APIInfoSimpleResponse,
                            page=page,
                            size=size,
                            filters=APIInfo.creator == user["id"],
                            order_by=None,
                            options=my_options)
    return ResponseResult.success(data=result,message="success!")

def build_response_property_list(param:APIResponsePropertyParam,result:list[APIResponsePropertyInfo],api_id:int,time:datetime)->list[APIResponsePropertyInfo]:
    if not param.api_id or not param.children:
        return result
    for child in param.children:
        response_info = APIResponsePropertyInfo(
            id = Snowflake.get_id(),
            api_id = api_id,
            parent_id = param.id,
            property_name = child.property_name,
            data_type = child.data_type,
            example = child.example
        )
        child.id = response_info.id
        child.api_id = api_id
        response_info.create_time = time
        response_info.update_time = time
        result.append(response_info)
        build_response_property_list(param=child,result=result,api_id=api_id,time=time)


async def api_details(id:int, db:AsyncSession)->ResponseResult[APIInfoResponse]:
    sql = (select(APIInfo).options(
        selectinload(APIInfo.params),
        joinedload(APIInfo.plugins),
        joinedload(APIInfo.response_examples),
        selectinload(APIInfo.response_properties)
    ).where(APIInfo.id == id))

    api = await db.scalar(sql)
    if not api:
        raise BusinessException(err=ErrorCode.ACCOUNT_NOT_EXIST)
    result = APIInfoResponse.model_validate(api)
    response_properties_tree = APIResponsePropertyResponse.build_tree(data=result.response_properties,
                                                                      root_id=0,order_by=None,reverse=False)
    result.response_properties = response_properties_tree
    return ResponseResult.success(data=result,message="success!")


@Transactional
async def update_api(param:APIInfoParam,db:AsyncSession)->ResponseResult:
    sql_update = (update(APIInfo).where(APIInfo.id == param.id)
                  .values(category_id = param.category_id,
                          api_host = param.api_host,
                          api_name = param.api_name,
                          api_port = param.api_port,
                          api_method = param.api_method,
                          api_path = param.api_path,
                          endpoint = param.endpoint,
                          is_https = param.is_https,
                          status = param.status
                          ))
    await db.execute(sql_update)
    create_time = datetime.now()
    update_time = create_time
    delete_api_components(id=param.id,db=db)
    add_api_components(param=param,create_time=create_time,update_time=update_time,api_id=param.id,db=db)
    return ResponseResult.success(message="success!")



@Transactional
async def delete_api(id:int,db:AsyncSession)->ResponseResult:
    # select API info
    api = await db.scalar(select(APIInfo).where(APIInfo.id == id))
    if not api:
        raise BusinessException(err=ErrorCode.API_MOT_EXIST)
    await delete_api_components(id=id,db=db)
    # delete API information
    await db.delete(api)
    return ResponseResult.success(message="success!")


async def add_api_components(param:APIInfoParam,create_time:datetime,update_time:datetime,api_id:int,db:AsyncSession):
    # add api plugin information into database
    plugin_info = APIPluginInfo(**param.plugins.model_dump())
    plugin_info.api_id = api_id
    plugin_info.create_time = create_time
    plugin_info.update_time = update_time
    db.add(plugin_info)
    # add api arguments into database
    param_list = []
    for param_req in param.params:
        param_info = APIParamInfo(**param_req.model_dump())
        param_info.api_id = api_id
        param_info.create_time = create_time
        param_info.update_time = update_time
        param_list.append(param_info)
    db.add_all(param_list)
    # add api response properties into database
    response_property_list = []
    for response in param.response_properties:
        response_info = APIResponsePropertyInfo(
            id = Snowflake.get_id(),
            api_id = api_id,
            parent_id = 0,
            property_name = response.property_name,
            example = response.example,
            data_type = response.data_type
        )
        response.api_id = api_id
        response_info.create_time = create_time
        response_info.update_time = update_time
        response.id = response_info.id
        response_property_list.append(response_info)
        build_response_property_list(param=response,result=response_property_list,api_id=api_id,time=create_time)
    db.add_all(response_property_list)
    # add api response result examples into database
    response_example = APIResponseExample(**param.response_examples.model_dump())
    response_example.api_id = api_id
    response_example.create_time = create_time
    response_example.update_time = update_time
    db.add(response_example)


async def delete_api_components(id:int,db:AsyncSession):
    #delelet response example info
    sql_examples = (delete(APIResponseExample).where(APIResponseExample.api_id == id))
    await db.execute(sql_examples)
    # delete api response properties
    sql_response_properties = (delete(APIResponsePropertyInfo).where(APIResponsePropertyInfo.api_id == id))
    await db.execute(sql_response_properties)
    #delete api plugins
    sql_plugin = (delete(APIPluginInfo).where(APIPluginInfo.api_id == id))
    await db.execute(sql_plugin)
    # delete api params
    sql_params = (delete(APIParamInfo).where(APIParamInfo.api_id == id))
    await db.execute(sql_params)