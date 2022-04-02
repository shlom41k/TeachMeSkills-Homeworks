# shom41k
# homework 16

"""
# Create models for homework #16
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()


class Brand(Base):
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __repr__(self):
        return f"{self.name}"

    def __iter__(self):
        return self


class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    model = Column(String(100))
    release_year = Column(Integer)
    brand_id = Column(Integer, ForeignKey('brands.id'), nullable=False)

    brand = relationship('Brand', foreign_keys='Car.brand_id')

    def __repr__(self):
        return f"{self.brand} {self.model}, {self.release_year}"
