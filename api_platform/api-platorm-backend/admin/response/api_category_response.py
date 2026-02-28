from common.response.response_body import BaseResponseBody,Tree
from common.id_generator.id_util import SnowFlakeID

class APICategoryResponse(BaseResponseBody):
    parent_id:SnowFlakeID
    category_name:str
    sort:int

class APICategoryTree(Tree["APICategoryTree"]):
    category_name:str
    sort:int

APICategoryResponse.model_rebuild()
APICategoryTree.model_rebuild()