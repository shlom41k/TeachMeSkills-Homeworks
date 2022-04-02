# -*- coding: utf-8 -*-

# homework 18
# shlom41k

"""
# Module for work with database (create, read, update and delete data)
"""


from models import db, Product


class CRUD:

    @classmethod
    def validate_new_data(cls, new_name: str, new_price, new_amount=None, new_comment=""):
        message = ""
        price, amount = 1.0, 1
        comment = new_comment if new_comment else "Some product"

        if db.session.query(Product).filter(Product.name == new_name).first():
            message = f"ERROR! Product with name {new_name} already exist!"
            return False, message, None
        if new_name == "":
            message = f"ERROR! Empty product name!"
            return False, message, None
        if new_price != "":
            try:
                price = float(new_price)
            except:
                message = f"ERROR! Wrong product price (must be float)!"
                return False, message, None
            if price <= 0:
                message = f"ERROR! Wrong product price (must be > 0)!"
                return False, message, None
        else:
            message = f"ERROR! Enter product price (must be float and > 0)!"
            return False, message, None

        if new_amount is not None and new_amount != "":
            try:
                amount = int(new_amount)
            except:
                message = f"ERROR! Wrong product amount (must be integer)!"
                return False, message, None

        message = f"INFO: Arguments validated successfully!"
        return True, message, Product(new_name, price, amount, comment)

    @classmethod
    def create(cls, product: Product):
        db.session.add(product)
        db.session.commit()
        return True

    @classmethod
    def read(cls, id: int):
        return db.session.query(Product).filter(Product.id == id).first()

    @classmethod
    def read_all(cls):
        return db.session.query(Product).order_by(Product.id)

    @classmethod
    def update(cls, id: int, name=None, price=None, amount=None, comment=None):

        message = ""
        product = db.session.query(Product).filter(Product.id == id).first()

        if not product:
            message = f"ERROR! No product with ID={id} in table!"
            return False, message

        if name is not None and name != "":
            product.name = name

        if price is not None and price != "":
            try:
                price = float(price)
                product.price = price
            except:
                message = f"ERROR! Wrong product price (must be float)!"
                return False, message

        if amount is not None and amount != "":
            try:
                amount = int(amount)
                product.amount = amount
            except:
                message = f"ERROR! Wrong product amount (must be integer)!"
                return False, message
        if comment is not None and comment != "":
            product.comment = comment

        db.session.query(Product).filter(Product.id == id).update(
            {
                Product.name: product.name,
                Product.price: product.price,
                Product.amount: product.amount,
                Product.comment: product.comment
            },
            synchronize_session=False)

        db.session.commit()
        message = f"INFO: Product description updated successfully"

        return True, message

    @classmethod
    def delete(cls, id: int):
        db.session.query(Product).filter(Product.id == id).delete()
        db.session.commit()

    @classmethod
    def read_product_as_list(cls, id: int):
        product = cls.read(id=id)
        return product.id, product.name, float(product.price), product.amount, product.comment

    @classmethod
    def read_products_as_list(cls):
        products = cls.read_all()
        data = []
        for ind, product in enumerate(products, 1):
            data.append([str(ind), str(product.id), product.name, float(product.price), product.amount, product.comment])
        return data


if __name__ == "__main__":
    products = CRUD.read_all()
    for product in products:
        print(product)

    print(CRUD.read_products_as_list())

