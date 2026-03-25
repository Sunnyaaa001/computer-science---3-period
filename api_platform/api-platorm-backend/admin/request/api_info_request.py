from pydantic import BaseModel,Field
from typing import Any,Optional

class APIResponseExampleParam(BaseModel):
    id:Optional[int] = None
    api_id:Optional[int] = None
    json_examples:Optional[dict[str,Any]]

class APIPluginParam(BaseModel):
    id:Optional[int] = None
    api_id:Optional[int] = None
    is_limited:Optional[str] = None
    ip_control:Optional[str] = None
    is_user_limited:Optional[str] = None

class APIResponsePropertyParam(BaseModel):
    id:Optional[int] = None
    api_id:Optional[int] = None
    parent_id:Optional[int] = None
    property_name:str =Field(extra={"error_msg":"response property name is empty"})
    data_type:str = Field(extra={"error_msg":"data type of response property is empty"})
    example:Optional[str] = None
    children:Optional[list["APIResponsePropertyParam"]] = None

class APIParamReq(BaseModel):
    id:Optional[int] = None
    api_id:Optional[int] = None
    paramter_name:str = Field(extra={"error_msg":"api id is empty"})
    type:Optional[str] = None
    data_type:str = Field(extra={"error_msg":"paramter data type is empty"})
    is_required:Optional[str] = None


class APIInfoParam(BaseModel):
    id:Optional[int] = None
    category_id:int = Field(extra={"error_msg":"category id is empty"})
    api_name:str = Field(extra={"error_msg":"api name is empty"})
    api_host:str = Field(extra={"error_msg":"api host is empty"})
    api_port:int = Field(extra={"error_msg":"port is empty"})
    api_method:str =Field(extra={"error_msg":"api method is empty"})
    api_path:str = Field(extra={"error_msg":"api path is empty"})
    endpoint:Optional[str] = None
    is_https:Optional[str] = None
    status:Optional[str] = None
    params:Optional[list[APIParamReq]] = None
    plugins:Optional[APIPluginParam] = None
    response_examples:Optional[APIResponseExampleParam] = None
    response_properties:Optional[list[APIResponsePropertyParam]] = None
    
APIResponsePropertyParam.model_rebuild()