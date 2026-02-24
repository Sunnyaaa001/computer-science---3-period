from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import BigInteger,DateTime,func,String,CHAR,Float,Text,inspect
from datetime import datetime
from common.id_generator.id_util import Snowflake

class Base(DeclarativeBase):
    
    __abstract__ = True

    id:Mapped[int] = mapped_column("id",BigInteger,nullable=False,primary_key=True,default = Snowflake.get_id)
    create_time:Mapped[datetime] = mapped_column("create_time",DateTime,nullable=False,default=func.now())
    update_time:Mapped[datetime] = mapped_column("update_time",DateTime,nullable=False)
    
    def _dict(self,exclude:set = None):
        exclude = exclude or set()
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs
                if c.key not in exclude}
