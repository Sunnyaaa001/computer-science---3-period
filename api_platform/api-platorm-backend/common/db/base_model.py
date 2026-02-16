from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import BigInteger,DateTime,func
from datetime import datetime
from common.id_generator.id_util import Snowflake

class Base(DeclarativeBase):
    id:Mapped[int] = mapped_column("id",BigInteger,nullable=False,primary_key=True,default = Snowflake.get_id)
    create_time:Mapped[datetime] = mapped_column("create_time",DateTime,nullable=False,default=func.now())