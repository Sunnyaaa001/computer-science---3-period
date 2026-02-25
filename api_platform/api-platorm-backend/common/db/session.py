from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from threading import Lock
from typing import AsyncGenerator
import sys

class DB:
    _instance = None
    _lock = Lock() #keep thread safe
    _supported_drivers = {"sqlite", "mysql", "postgresql","mysql+asyncmy"}

    @classmethod
    def init(cls,database_driver:str,ip:str,port:int,db_name:str,username:str,password:str,config:str,sql_log:bool):
        #check database arguements
        try:
            driver = database_driver.lower()
            if driver not in cls._supported_drivers:
                raise ValueError(f"Unsupported database driver: {database_driver}. Supported: {cls._supported_drivers}")
            if driver != "sqlite":
                #check db name
                if not db_name:
                    raise ValueError("Database name cannot be empty for non-sqlite databases!")
                #check IP
                if not ip:
                    raise ValueError("IP cannot be empty for non-sqlite databases!")
                #check database port
                if not port:
                    raise ValueError("Port cannot be empty for non-sqlite databases!")
                else:
                    if port < 1024 or port > 49151:
                        raise ValueError("database port should between 1024 and 49151!")
                #check username and password
                if not username or not password:
                    raise ValueError("username and password cannot be empty for non-sqlite databases!")
            else:
                if not db_name:
                    raise ValueError("db_name cannot be empty!")
            # initialize SQLAlchemy
            if cls._instance is None:
                with cls._lock:
                    if cls._instance is None and not getattr(cls._instance, "_initialized", False):
                        # init DB class
                        cls._instance = super().__new__(cls)
                        if driver == "sqlite":
                            db_url = f"sqlite+aiosqlite:///{db_name}"
                        else:
                            db_url = f"{driver}://{username}:{password}@{ip}:{port}/{db_name}?{config}"

                        cls._instance.engine = create_async_engine(db_url,echo=sql_log)
                        cls._instance.SessionLocal = sessionmaker(
                            bind=cls._instance.engine,autoflush=False,expire_on_commit=False,class_=AsyncSession
                        )
                        cls._instance._initialized = True
            return cls._instance
        except Exception as e:
            print(f"[ERROR] Failed to initialize DB: {e}", file=sys.stderr)
            sys.exit(1)

    @classmethod
    async def get_session(cls) -> AsyncGenerator[AsyncSession,None]:
        async with cls._instance.SessionLocal() as session:
            yield session
