from common.db.base_model import Base,Mapped,mapped_column,String,CHAR,Text

class SysUser(Base):
    __tablename__ = "sys_user"
    username:Mapped[str] = mapped_column("username",String,nullable=False)
    password:Mapped[str] = mapped_column("password",String,nullable=False)
    avatar:Mapped[str] = mapped_column("avatar",Text)
    status:Mapped[str] = mapped_column("status",CHAR,nullable=False,default="0")