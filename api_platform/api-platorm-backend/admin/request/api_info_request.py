from pydantic import BaseModel
from typing import Any,Optional

class APIResponseExampleParam(BaseModel):
    id:int
    api_id:int
    json_examples:Optional[dict[str,Any]]

class APIPluginParam(BaseModel):
    id:int
    api_id:int
    is_limated:str
    ip_control:str
    is_user_limated:str

class APIResponsePropertyParam(BaseModel):
    id:int
    api_id:int
    parent_id:int
    property_name:str
    data_type:str
    children:list["APIResponsePropertyParam"]

class APIParamReq(BaseModel):
    id:int
    api_id:int
    paramter_name:str
    type:str
    data_type:str
    is_required:str


class APIInfoParam(BaseModel):
    id:int
    category_id:int
    api_name:str
    api_host:str
    api_port:int
    api_method:str
    status:str
    params:list[APIParamReq]
    plugins:list[APIPluginParam]
    response_examples:APIResponseExampleParam
    response_properties:list[APIResponsePropertyParam]
    
APIResponsePropertyParam.model_rebuild()