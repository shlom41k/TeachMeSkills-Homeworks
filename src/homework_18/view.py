# -*- coding: utf-8 -*-

# homework 18
# shlom41k

"""
# Module with views
"""


from flask import render_template, url_for, request, redirect
from datetime import datetime

from server import app
from db_crud import CRUD
from settings import LOCALHOST, URL_PRODUCT, URL_EDIT_PRODUCT, URL_DELETE_PRODUCT, URL_ADD_PRODUCT


@app.route("/")
def hello_world():
    total_sum, total_cnt = 0, 0
    products = CRUD.read_products_as_list()
    for product in products:
        *_, prod_price, prod_amount, _ = product
        total_sum += prod_price
        total_cnt += prod_amount
    return render_template('color_table.html',
                           products=products,
                           l=len(products),
                           total_sum=round(total_sum, 2),
                           total_cnt=total_cnt,
                           date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                           url_prod=LOCALHOST + URL_PRODUCT,
                           url_add=LOCALHOST + URL_ADD_PRODUCT)


@app.route(URL_PRODUCT + "<int:id>")
def product_info(id):
    product = CRUD.read_product_as_list(id=id)
    id, name, price, amount, comment = product
    return render_template('product_info.html',
                           id=str(id),
                           name=name,
                           price=price,
                           amount=amount,
                           comment=comment,
                           url_home=LOCALHOST,
                           url_edit=LOCALHOST + URL_EDIT_PRODUCT,
                           url_delete=LOCALHOST + URL_DELETE_PRODUCT)


@app.route(URL_EDIT_PRODUCT + "<int:id>", methods=["GET", "POST"])
def edit_product(id):
    if request.method == "GET":
        product = CRUD.read_product_as_list(id=id)
        id, name, price, amount, comment = product
        try:
            info_message = request.args["info_message"]
        except:
            info_message = f"INFO: You can edit parameters of product into a edit line"

        return render_template('edit_product.html',
                               id=str(id),
                               name=name,
                               price=price,
                               amount=amount,
                               comment=comment,
                               message=info_message,
                               url_home=LOCALHOST,
                               url_prod=LOCALHOST + URL_PRODUCT,
                               url_edit=LOCALHOST + URL_EDIT_PRODUCT)
    else:
        act, info_message = CRUD.update(id=id, name=request.form["name"], price=request.form["price"],
                                   amount=request.form["amount"], comment=request.form["comment"])
        print(info_message)
        return redirect(url_for("edit_product", id=id, info_message=info_message))


@app.route(URL_DELETE_PRODUCT + "<int:id>")
def delete_product(id):
    try:
        CRUD.delete(id=id)
        print(f"Product with ID={id} deleted!")
        return redirect(url_for("hello_world"))
    except:
        return "OOOOps. Some ERROR! Can not delete this product"


@app.route(URL_ADD_PRODUCT, methods=["GET", "POST"])
def add_product():
    if request.method == "GET":
        try:
            info_message = request.args["info_message"]
            name = request.args["name"]
            price = request.args["price"]
            amount = request.args["amount"]
            comment = request.args["comment"]
        except:
            info_message = f"Input product description and press 'Add'. ID generated automatically"
            name, price, amount, comment = "", "", "", ""
        return render_template("add_product.html",
                               name=name,
                               price=price,
                               amount=amount,
                               comment=comment,
                               message=info_message,
                               url_home=LOCALHOST,)
    else:
        try:
            ans, info_message, product = CRUD.validate_new_data(new_name=request.form["name"], new_price=request.form["price"],
                                                           new_amount=request.form["amount"], new_comment=request.form["comment"])
            if not ans:
                return redirect(url_for("add_product",
                                        info_message=info_message,
                                        name=request.form["name"],
                                        price=request.form["price"],
                                        amount=request.form["amount"],
                                        comment=request.form["comment"]))
            else:
                CRUD.create(product=product)
                return redirect(url_for("hello_world"))
        except:
            return "OOOOps. Some ERROR! Can not add this product"


if __name__ == "__main__":
    pass



