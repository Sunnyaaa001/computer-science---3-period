from typing import TypeVar,Optional,Generic
from typing import Type, Callable
from pydantic import BaseModel
from __future__ import annotations
from pydantic.generics import GenericModel
from pydantic import BaseModel,ConfigDict,field_serializer
from datetime import datetime
from typing_extensions import Annotated,get_args, get_origin
from common.db.session import AsyncSession
from sqlalchemy import select,func
# define type variable
T = TypeVar("T")

class ResponseResult(BaseModel,Generic[T]):

    def __init__(self,code:int,message:str,data:Optional[T] = None):
        self.code = code
        self.message = message
        self._data_type = None

        if hasattr(self,"__orig_class__"):
            self._data_type = self.__orig_class__.__args__[0]

        if data is not None and self._data_type is not None and not isinstance(data,self._data_type):
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



class BaseResponseBody(BaseModel):
    id: int
    create_time:Annotated[datetime, DateFormat("%Y-%m-%d %H:%M:%S")]
    update_time:Annotated[datetime, DateFormat("%Y-%m-%d %H:%M:%S")]

    model_config = ConfigDict(
        from_attributes=True
    )

    @field_serializer("id")
    def serialize_id(self, v: int):
        return str(v)
    
    def __init_subclass__(cls):
        super().__init_subclass__()

        for name, field in cls.model_fields.items():

            ann = field.annotation

            if get_origin(ann) is Annotated:
                _, *meta = get_args(ann)

                for m in meta:
                    if isinstance(m, DateFormat):

                        fmt = m.fmt

                        @field_serializer(name)
                        def ser(self, v, fmt=fmt):
                            return v.strftime(fmt)

                        setattr(cls, f"_ser_{name}", ser)



class DateFormat:
    def __init__(self, fmt: str):
        self.fmt = fmt



class PageResult(GenericModel,Generic[T]):
    total:int
    page:int
    size:int
    items:list[T]


async def paginate(db:AsyncSession,
             model:Type,
             response_model:Type[T],
             page: int = 1,
             size: int = 10,
             filters: Callable[[Type], list] | None = None,
             order_by=None
             ) ->PageResult[T]:
    query = select(model)

    if filters:
        condition = filters(model)
        if condition:
            query = query.where(*condition)

    if order_by:
        query.order_by(order_by)

    total = await db.scalar(select(func.count()).select_from(model))
    offset = (page - 1) * size
    rows = await db.scalars(query.offset(offset).limit(size)).all()
    items = [response_model.model_validate(r) for r in rows]
    return PageResult[T](
        total=total,
        page=page,
        size=size,
        items=items
    )

