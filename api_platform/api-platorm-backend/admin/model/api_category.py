from common.db.base_model import Base,Mapped,mapped_column,BigInteger,Integer,String,Text

class APICategory(Base):
    __tablename__ = "api_category"

    parent_id:Mapped[int] = mapped_column("parent_id",BigInteger,nullable=False)
    category_name:Mapped[str] = mapped_column("category_name",String,nullable=False)
    sort:Mapped[int] = mapped_column("sort",Integer,nullable=False)
    ancestors:Mapped[str] = mapped_column("ancestors",Text,nullable=False)
    creator_id:Mapped[int] = mapped_column("creator_id",BigInteger,nullable=False)
    