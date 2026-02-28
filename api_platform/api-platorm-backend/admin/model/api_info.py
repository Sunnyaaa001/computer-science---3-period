from common.db.base_model import Base,BigInteger,String,CHAR,Mapped,mapped_column,Integer


class APIInfo(Base):
    __tablename__ = "api_info"

    category_id:Mapped[int] = mapped_column("category_id",BigInteger,nullable=False)
    api_name:Mapped[str] = mapped_column("api_name",String,nullable=False)
    api_host:Mapped[str] = mapped_column("api_host",String,nullable=False)
    api_port:Mapped[int] = mapped_column("api_port",Integer,nullable=False)
    api_method:Mapped[str] = mapped_column("api_method",String,nullable=False)
    status:Mapped[str] = mapped_column("status",CHAR,nullable=False,default="1")
    creator:Mapped[int] = mapped_column("creator",BigInteger,nullable=False)