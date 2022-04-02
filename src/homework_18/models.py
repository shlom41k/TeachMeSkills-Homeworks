# -*- coding: utf-8 -*-

# homework 18
# shlom41k

"""
# Module for creating database models
"""


from server import db


class Product(db.Model):
    __tablename__ = "Products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, index=True)
    price = db.Column(db.DECIMAL)
    amount = db.Column(db.Integer)
    comment = db.Column(db.String)

    def __init__(self, name: str, price=0.0, amount=1, comment="Some product"):
        self.name = name
        self.price = price
        self.amount = amount
        self.comment = comment

    def __repr__(self):
        return f"ID={self.id}: {self.name}, price={self.price}, amount={self.amount}, comment={self.comment}"

    @property
    def product_id(self):
        return self.id

    @property
    def product_name(self):
        return self.name

    @product_name.setter
    def product_name(self, name: str):
        self.name = name

    @property
    def product_price(self):
        return self.price

    @product_price.setter
    def product_price(self, price: float):
        self.price = price

    @property
    def product_amount(self):
        return self.amount

    @product_amount.setter
    def product_amount(self, amount: int):
        self.amount = amount

    @property
    def product_comment(self):
        return self.comment

    @product_comment.setter
    def product_comment(self, comment: str):
        self.comment = comment


if __name__ == "__main__":

    # db.create_all()

    # milk = Product(name="Milk", price=2.25, amount=12, comment="Zdravushka")
    # print(milk.product_name)
    #
    # cheese = Product(name="Cheese", price=4.25, amount=26, comment="Zdravushka")
    # mars = Product(name="Mars", price=2.12, amount=100, comment="Vkusnyahi")
    # twiks = Product(name="Twiks", price=2.45, amount=50, comment="Vkusnyahi")
    # dirol = Product(name="Dirol", price=1.05, amount=523, comment="Bubble gum")
    # chocolate = Product(name="Chocolate", price=3.89, amount=165, comment="Nestle")

    # db.session.add_all([milk, cheese, mars, twiks, dirol, chocolate])
    # db.session.commit()

    # sausages = Product(name="Sausages", price=6.13, amount=33, comment="Very tasty")
    # yogurt = Product(name="Yogurt", price=2.07, amount=245, comment="Activia")
    # banana = Product(name="Bananas", price=3.13, amount=22, comment="Bananaaaaaaaaaaaa")
    # persimmon = Product(name="Persimmon", price=2.25, amount=89)
    # juice = Product(name="Juice", price=3.32, amount=124, comment="Rich")
    # bread = Product(name="Bread", price=0.89, amount=235)
    # butter = Product(name="Butter", price=2.89, amount=145, comment="Grandmother Ann")
    # cookies = Product(name="Cookies", price=1.58, amount=45)
    # vine = Product(name="Vine", price=15.68, amount=145, comment="Saperavi (Georgian vines), semi-sweet")
    #
    # db.session.add_all([sausages, yogurt, banana, persimmon, juice, bread, butter, cookies, vine])
    # db.session.commit()
    #
    # beer = Product(name="Beer Pilsner", price=2.12, amount=143, comment="Alcohol")
    # beer2 = Product(name="Beer 'Lidskoe' (0.5)", price=1.89, amount=221, comment="Alcohol")
    # cola = Product(name="Coca-cola (0.5)", price=2.09, amount=156)
    # sprite = Product(name="Sprite (0.5)", price=2.09, amount=253)
    # fanta = Product(name="Fanta (0.5)", price=2.09, amount=128)
    # chocolate = Product(name="Chocolate 'Alenka'", price=3.15, amount=235)
    # db.session.add_all([beer, beer2, cola, sprite, fanta, chocolate])
    # db.session.commit()

    # bun = Product(name="Poppy seed bun", price=1.19, amount=18)
    # candy = Product(name="Candy 'Roshen'", price=3.69, amount=59)
    # cucumbers = Product(name="Cucumber 'Belarussian'", price=5.05, amount=59, comment="Minsk")
    #
    # db.session.add_all([bun, candy, cucumbers])
    # db.session.commit()


    pass
