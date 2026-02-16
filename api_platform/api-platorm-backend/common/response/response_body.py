from typing import TypeVar,Optional,Generic
from pydantic import BaseModel
from __future__ import annotations
# define type variable
T = TypeVar("T")

class ResponseResult(BaseModel,Generic[T]):

    def __init__(self,code:int,message:str,data:Optional[T] = None):
        self.code = code
        self.message = message
        self._data_type = None

        if hasattr(self,"__orig_class__"):
            self._data_type = self.__orig_class__.__args__[0]

        if data is not None and self._data_type is not None and isinstance(data,self._data_type):
            raise TypeError(f"data must be of type {self._data_type}, got {type(data)}")
          
        self.data = data

    @classmethod    
    def success(cls,code:int = 200 ,data:Optional[T] = None, message:str = "success!") -> ResponseResult[T]:    
        return cls(code=code,data=data,message=message)
    
    @classmethod
    def fail(cls,code:int = 500, message:str = "failed!") -> ResponseResult[T]:
        return cls(code=code,message = message)
    
    @classmethod
    def response(cls, code:int, message:str,data: Optional[T] = None) -> ResponseResult[T]:
        return cls(code,data=data,message=message)
    