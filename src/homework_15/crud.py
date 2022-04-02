# homework 15
# shlom41k


from sqlalchemy.orm import sessionmaker
from tabulate import tabulate
from db_creator import *


class CRUD:

    _session = None

    @classmethod
    def connect_to_db(cls):
        cls._session = sessionmaker(bind=engine)()
        print(f"Connected to database. Current session: {cls._session}")

    @classmethod
    def create(cls, product: Product):
        cls._session.add(product)
        cls._session.commit()
        print(f"Product [{product.name}] added to database")

    @classmethod
    def select(cls, id=None, name=None):
        if id:
            return cls._session.query(Product).filter(Product._id == id).first()
        elif name:
            return cls._session.query(Product).filter(Product._name == name).first()

    @classmethod
    def select_all(cls):
        return cls._session.query(Product).order_by(Product._id)

    @classmethod
    def show_all(cls):
        data = []
        headers = ["ID", "NAME", "PRICE", "COUNT", "COMMENT"]

        for prod in cls._session.query(Product).order_by(Product._id):
            data.append([prod._id, prod._name, float(prod._price), prod._count, prod._comment])

        print(tabulate(data, headers=headers, stralign='left'))

    @classmethod
    def update_by_id(cls, id: int, name=None, price=None, count=None, comment=None):

        product = cls._session.query(Product).filter(Product._id == id).first()

        if name:
            product._name = name
        if price:
            product._price = price
        if count:
            product._count = count
        if comment:
            product._comment = comment

        cls._session.query(Product).filter(Product._id == id).update(
            {
                Product._name: product._name,
                Product._price: product._price,
                Product._count: product._count,
                Product._comment: product._comment
            },
            synchronize_session=False)

        cls._session.commit()

        return "Updated >> {}".format(product)

    @classmethod
    def delete_by_id(cls, id: int):
        cls._session.query(Product).filter(Product._id == id).delete()
        cls._session.commit()
        print("Product with ID [{}] deleted".format(id))


if __name__ == "__main__":
    # Create connection to DB
    CRUD.connect_to_db()

    # Creating products
    # CRUD.create(Product(name="Cheese23", price=2.48, count=2, comment="Italian"))
    # CRUD.create(Product(name="Milk", price=1.25, count=14, comment="Zdravushka"))
    # CRUD.create(Product(name="Milk2", price=1.25, count=14, comment="Zdravushka"))
    # CRUD.create(Product(name="Milk2tgy", price=1.25, count=14, comment="Zdravushka"))

    # Select product by ID
    print(CRUD.select(id=2))

    # Select product by ID
    print(CRUD.select(name="Milk2"))

    # Select all products from DB
    for product in CRUD.select_all():
        print(product)

    # Update some product
    print(CRUD.select(id=1))
    print(CRUD.update_by_id(id=2, name="123456"))

    # Delete some product
    # CRUD.delete_by_id(id=4)

    CRUD.show_all()
    # CRUD.create(Product(name="Milkiway", price=1.25, count=14, comment="Zdravushka"))
    print(CRUD.update_by_id(id=2, name="Chto-to tam"))
    CRUD.show_all()



