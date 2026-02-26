from pydantic import BaseModel,Field
from typing import Optional

class UserParam(BaseModel):
    username:str = Field(...,description="user name")
    password:str = Field(...,description="password")
    avatar:Optional[str] = Field(None,description="avatar")
    status:Optional[str] = Field(None,description="user account status")


class LoginUser(BaseModel):
    username:str = Field(...,description="user name")
    password:str = Field(...,description="password")