from __future__ import annotations
from common.response.response_body import BaseResponseBody

class APICategoryResponse(BaseResponseBody):
    id:int
    parent_id:int
    category_name:str
    sort:int