from pydantic import BaseModel,Field

class APICategoryParam(BaseModel):
    id:int = None
    parent_id: int = Field(description="parent id")
    category_name:str = Field(description="category name")
    sort:int = None
    
