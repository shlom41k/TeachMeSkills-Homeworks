# homework 15
# shlom41k


from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


DATABASE = "sqlite:///prod.db"
TABLE_NAME = 'products'

engine = create_engine(DATABASE, echo=False)
Base = declarative_base()


class Product(Base):
    __tablename__ = TABLE_NAME

    _id = Column(Integer, primary_key=True)
    _name = Column(String(150), unique=True)
    _price = Column(DECIMAL)
    _count = Column(Integer)
    _comment = Column(String)

    def __init__(self, name: str, price: float, count=1, comment=None):
        self._id = None
        self._name = name
        self._price = price
        self._count = count
        self._comment = comment
        pass

    def __iter__(self):
        return self

    def __repr__(self):
        return "ID: {:}, Product: {:}, price: {:}, quantity: {:}, comment: {:}".format(
            self._id, self._name, float(self._price), self._count, self._comment)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def count(self):
        return self._count

    @property
    def comment(self):
        return self._comment


Base.metadata.create_all(engine)


if __name__ == "__main__":
    pass



