from sqlalchemy.orm import declarative_base,Mapped,mapped_column
from sqlalchemy import BigInteger,select,String

Base = declarative_base()


class VanityPlate(Base):
    __tablename__ = "vanity_plate"
    id:Mapped[int] = mapped_column("id",BigInteger,nullable=False,primary_key=True,autoincrement=True)
    license_plate_number:Mapped[str] = mapped_column("license_plate_number",String,nullable=False)
    owner:Mapped[str] = mapped_column("owner",String,nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "age": self.age}
