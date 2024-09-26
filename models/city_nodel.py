from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship

from config.base import Base


class City(Base):
    __tablename__ = 'cities'

    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String(100), unique=True, nullable=False)
    country_id = Column(Integer, ForeignKey('countries.country_id'), nullable=False)
    latitude = Column(DECIMAL)
    longitude = Column(DECIMAL)

    targets = relationship("Target", back_populates="city")
    countries = relationship("Country", back_populates="city")
    def __repr__(self):
        return f"city_name={self.city_name}, latitude={self.latitude}, longitude={self.longitude}"
