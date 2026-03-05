from common.response.response_body import BaseResponseBody
from common.response.response_body import Tree
from common.response.response_body import SnowFlakeID

class APIResponseExampleResponse(BaseResponseBody):
    api_id:SnowFlakeID
    json_examples:dict

class APIPluginResponse(BaseResponseBody):
    api_id:SnowFlakeID
    is_limited:str
    ip_control:str
    is_user_limited:str

class APIResponsePropertyResponse(Tree["APIResponsePropertyResponse"]):
    api_id:SnowFlakeID
    property_name:str
    data_type:str
    example:str

class APIParamResponse(BaseResponseBody):
    api_id:SnowFlakeID
    paramter_name:str
    type:str
    data_type:str
    is_required:str


class APIInfoResponse(BaseResponseBody):
    category_id:SnowFlakeID
    api_name:str
    api_host:str
    api_port:int
    api_method:str
    api_path:str
    endpoint:str
    is_https:str
    status:str
    params:list[APIParamResponse]
    plugins:APIPluginResponse
    response_examples:APIResponseExampleResponse
    response_properties:list[APIResponsePropertyResponse]

class APIInfoSimpleResponse(BaseResponseBody):
    category_id:SnowFlakeID
    api_name:str
    api_host:str
    api_port:int
    api_method:str
    api_path:str
    endpoint:str
    is_https:str
    status:str
    
APIResponsePropertyResponse.model_rebuild()