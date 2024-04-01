from app.models import Base
from sqlalchemy.orm import Mapped

class Contract(Base):
    __tablename__ = "contracts"

    title: Mapped[str]