# homework 15
# shlom41k

"""
-> Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
-> Реализовать CRUD (создание, чтение, обновление по id, удаление по id) для продуктов.
-> Создать пользовательский интерфейс.

# Project structure:
# |- ui.py
# |   |- crud.py
# |      |- db_creator.py
# |- prod.db
"""

from crud import *


class UserInterface:

    def run(self):
        CRUD.connect_to_db()

        while True:

            tasks = {
                "1": CRUD.show_all,
                "2": self.create_product,
                "3": self.get_product,
                "4": self.update_product,
                "5": self.delete_product,
            }

            print("\n[1] Show table\n"
                  "[2] Create product\n"
                  "[3] Get product (by ID, by NAME)\n"
                  "[4] Update product (by ID)\n"
                  "[5] Delete product (by ID)\n"
                  "[0] Exit")

            op = input("Choose your operation: ")

            if op == "0":
                break

            tasks.get(op, lambda: print(f"ERROR: Unknown operation '{op}'"))()

    def create_product(self):
        while True:
            try:
                name = input("Input product name: ")
                price = float(input("Input product price: "))
                count = input("Input product quantity: ")
                comment = input("Input comment to product: ")
                CRUD.create(Product(name=name, price=price, count=int(count) if count else 1,
                                    comment=comment if comment else None))
                break
            except:
                print("ERROR: Invalid input data")
                continue

    def get_product(self):
        while True:

            id = input("Input product ID: ")

            if id != "":
                if not id.isdigit():
                    print("ERROR: Invalid ID")
                    continue
                else:
                    prod = CRUD.select(id=int(id))

                    if prod:
                        print(prod)
                    else:
                        print(f"ERROR: In DATABASE no product with ID={id}")
                    break

            name = input("Input product name: ")

            if name:
                prod = CRUD.select(name=name)

                if prod:
                    print(prod)
                else:
                    print(f"ERROR: In DATABASE no product with NAME={name}")
                break

            else:
                print("ERROR: Empty ID and NAME!")

    def update_product(self):
        while True:

            id = input("Input product ID: ")

            if not id.isdigit():
                print("ERROR: Invalid ID")
            else:
                prod = CRUD.select(id)
                if not prod:
                    print(f"ERROR: In DATABASE no product with ID={id}")
                    break

                while True:
                    try:

                        name = input(f"Input product name [old: {prod.name}]: ")
                        price = input(f"Input product price [old: {float(prod.price)}]: ")
                        count = input(f"Input product quantity [old: {prod.count}]: ")
                        comment = input(f"Input comment to product [old: {prod.comment}]: ")

                        CRUD.update_by_id(id=int(id), name=name if name else None, price=float(price) if price else None,
                                          count=int(count) if count else None, comment=comment if comment else None)

                        print("Updated >> {}".format(CRUD.select(id)))
                        break
                    except:
                        print("ERROR: Invalid input data")
                break

    def delete_product(self):
        while True:
            id = input("Input product ID: ")

            if not id.isdigit():
                print("ERROR: Invalid ID")
            else:
                if CRUD.select(id):
                    CRUD.delete_by_id(int(id))
                else:
                    print(f"ERROR: In DATABASE no product with ID={id}")
                break


if __name__ == "__main__":
    user = UserInterface()
    user.run()
