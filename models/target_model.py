from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.base import Base


class Target(Base):
    __tablename__ = 'targets'

    target_id = Column(Integer, primary_key=True, autoincrement=True)
    target_industry = Column(String(255), unique=True, nullable=False)
    city_id = Column(Integer, ForeignKey("cities.city_id"), nullable=False)
    target_type_id = Column(Integer, ForeignKey("target_types.target_type_id"))
    target_priority = Column(Integer)

    tipe = relationship("Type", back_populates="targets")
    city = relationship("City", back_populates="targets")

    def __repr__(self):
        return f"target_industry={self.target_industry}, target_priority={self.target_priority}"
