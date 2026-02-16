from snowflake import SnowflakeGenerator
import threading
from typing import Optional

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

