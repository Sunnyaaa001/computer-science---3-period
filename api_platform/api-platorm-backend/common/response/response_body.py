from __future__ import annotations
from typing import TypeVar,Optional,Generic,Type, Callable,Any
from pydantic import BaseModel
from pydantic.generics import GenericModel
from pydantic import BaseModel,ConfigDict,field_serializer
from datetime import datetime
from typing_extensions import Annotated,get_args, get_origin
from common.db.session import AsyncSession
from sqlalchemy import select,func
from common.id_generator.id_util import SnowFlakeID,PlainSerializer

# define type variable
T = TypeVar("T")

class ResponseResult(BaseModel,Generic[T]):
    code:int
    data:Optional[T] = None
    message:str = None

    @classmethod    
    def success(cls,code:int = 200 ,data:Optional[T] = None, message:str = "success!") -> ResponseResult[T]:    
        return cls(code=code,data=data,message=message)
    
    @classmethod
    def fail(cls,code:int = 500, message:str = "failed!") -> ResponseResult[T]:
        return cls(code=code,message = message)
    
    @classmethod
    def response(cls, code:int, message:str,data: Optional[T] = None) -> ResponseResult[T]:
        return cls(code=code,data=data,message=message)
        

class BaseResponseBody(BaseModel):
    id: SnowFlakeID
    create_time: Annotated[datetime, DateFormat("%Y-%m-%d %H:%M:%S")]
    update_time: Annotated[datetime, DateFormat("%Y-%m-%d %H:%M:%S")]

    model_config = ConfigDict(from_attributes=True,populate_by_name=True,arbitrary_types_allowed=True)

    @field_serializer("*", mode="plain", when_used="always")
    def serialize_special_types(self, v: Any, info):
        field_info = self.model_fields.get(info.field_name)
        if not field_info:
            return v
            
        ann = field_info.annotation
        if ann is SnowFlakeID or isinstance(v, SnowFlakeID):
             return str(v)
        
        if isinstance(v, datetime):
            origin = get_origin(ann)
            if origin is Annotated:
                meta = get_args(ann)
                for m in meta:
                    if isinstance(m, DateFormat):
                        return v.strftime(m.fmt)
            return v.strftime("%Y-%m-%d %H:%M:%S")

        return v                         


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

BaseResponseBody.model_rebuild() 