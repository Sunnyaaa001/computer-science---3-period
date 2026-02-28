from snowflake import SnowflakeGenerator
import threading
from typing import Optional,Any
from pydantic_core import core_schema
from pydantic import PlainSerializer,GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema

class Snowflake:

    _instance = None
    _instance_lock = threading.Lock()
    _generator: Optional[SnowflakeGenerator] = None

    @classmethod
    def init (cls,instance: int, seq: int = 0, epoch: int = 0, timestamp: Optional[int] = None):
        if not cls._instance:
            with cls._instance_lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._generator = SnowflakeGenerator(instance=instance,seq=seq,epoch=epoch,timestamp=timestamp)
        return cls._instance

    @classmethod
    def get_id(cls) -> int:
        return next(cls._generator)
      

class SnowFlakeID:
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(),
            python_schema=core_schema.union_schema([
                core_schema.int_schema(),
                core_schema.str_schema(),
            ]),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda v: str(v), when_used="always"
            ),
        )