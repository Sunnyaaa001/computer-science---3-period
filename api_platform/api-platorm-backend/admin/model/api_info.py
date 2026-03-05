from common.db.base_model import Base,BigInteger,String,CHAR,Mapped,mapped_column,Integer,relationship
from sqlalchemy.dialects.mysql import JSON
from typing import Any,Optional

class APIInfo(Base):
    __tablename__ = "api_info"

    category_id:Mapped[int] = mapped_column("category_id",BigInteger,nullable=False)
    api_name:Mapped[str] = mapped_column("api_name",String,nullable=False)
    api_host:Mapped[str] = mapped_column("api_host",String,nullable=False)
    api_port:Mapped[int] = mapped_column("api_port",Integer,nullable=False)
    api_method:Mapped[str] = mapped_column("api_method",String,nullable=False)
    api_path:Mapped[str] = mapped_column("api_path",String,nullable=False)
    endpoint:Mapped[str] = mapped_column("endpoint",String,nullable=True)
    is_https:Mapped[str] = mapped_column("is_https",String,nullable=False)
    status:Mapped[str] = mapped_column("status",CHAR,nullable=False,default="1")
    creator:Mapped[int] = mapped_column("creator",BigInteger,nullable=False)

    params = relationship(
        "APIParamInfo",
        primaryjoin="APIInfo.id == APIParamInfo.api_id",
        foreign_keys="APIParamInfo.api_id",
        lazy= "selectin",
        viewonly=True
    )

    plugins = relationship(
        "APIPluginInfo",
        primaryjoin= "APIInfo.id == APIPluginInfo.api_id",
        foreign_keys="APIPluginInfo.api_id",
        lazy="joined",
        uselist=False,
        viewonly=True
    )

    response_examples = relationship(
        "APIResponseExample",
        primaryjoin="APIInfo.id == APIResponseExample.api_id",
        foreign_keys="APIResponseExample.api_id",
        lazy="joined",
        uselist=False,
        viewonly=True
    )
    
    response_properties = relationship(
        "APIResponsePropertyInfo",
        primaryjoin="APIInfo.id == APIResponsePropertyInfo.api_id",
        foreign_keys="APIResponsePropertyInfo.api_id",
        lazy="selectin",
        uselist=True, 
        viewonly=True
    )    

class APIParamInfo(Base):
    __tablename__ = "api_param_info"

    api_id:Mapped[int] = mapped_column("api_id",BigInteger,nullable=False)
    paramter_name:Mapped[str] = mapped_column("paramter_name",String,nullable=False)
    type:Mapped[str] = mapped_column("type",CHAR,nullable=False)
    data_type:Mapped[str] = mapped_column("data_type",String,nullable=False)
    is_required:Mapped[str] = mapped_column("is_required",String,nullable=False)

class APIPluginInfo(Base):
    __tablename__ = "api_plugin_info"

    api_id:Mapped[int] = mapped_column("api_id",BigInteger,nullable=False)
    is_limited:Mapped[str] = mapped_column("is_limited",CHAR,nullable=False)
    ip_control:Mapped[str] = mapped_column("ip_control",CHAR,nullable=False)
    is_user_limited:Mapped[str] = mapped_column("is_user_limited",CHAR,nullable=False)

class APIResponsePropertyInfo(Base):
    __tablename__ = "api_response_property_info"

    api_id:Mapped[int] = mapped_column("api_id",BigInteger,nullable=False)
    parent_id:Mapped[int] = mapped_column("parent_id",BigInteger,nullable=False)
    property_name:Mapped[str] = mapped_column("property_name",String,nullable=False)
    data_type:Mapped[str] = mapped_column("data_type",String,nullable=False)
    example:Mapped[str] = mapped_column("example",String,nullable=False)

class APIResponseExample(Base):
    __tablename__ = "api_response_examples"

    api_id:Mapped[int] = mapped_column("api_id",BigInteger,nullable=False)
    json_examples:Mapped[Optional[dict[str,Any]]] = mapped_column("json_examples",JSON,nullable=True)