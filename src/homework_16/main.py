# shom41k
# homework 16

"""
-> Создать таблицы Brand(name), Car(model, release_year, brand (foreing key на таблицу Brand)).
-> Реализовать CRUD(создание, чтение, обновление по id, удаление по id) для бренда и машины.
-> Создать пользовательский интерфейс.

# Create main file for homework #16 (User Interface)

# project structure:
# |- main.py
# |   |- crud.py
# |      |- db_creator.py
# |         |- models.py
"""


from crud import CRUD, session


class User:

    _crud = CRUD(session=session)

    def run(self):
        # main loop
        tasks = {
            "1": self._crud.show_all_brands,
            "2": self._crud.show_all_cars,
            "3": self.create_brand,
            "4": self.create_car,
            "5": self.read_brand,
            "6": self.read_car,
            "7": self.update_brand,
            "8": self.update_car,
            "9": self.delete_brand,
            "10": self.delete_car,
        }

        while True:
            print("\n[1] Show table 'Brands'\n"
                  "[2] Show table 'Cars'\n"
                  "[3] Create brand\n"
                  "[4] Create car\n"
                  "[5] Get brand (by ID)\n"
                  "[6] Get car (by ID)\n"
                  "[7] Update brand (by ID)\n"
                  "[8] Update car (by ID)\n"
                  "[9] Delete brand (by ID)\n"
                  "[10] Delete car (by ID)\n"
                  "[0] Exit")

            op = input("Choose your operation: ")

            if op == "0":
                break

            tasks.get(op, lambda: print(f"ERROR: Unknown operation '{op}'"))()

    def create_brand(self):
        while True:

            name = input("Input car brand [0=break]: ")

            if name == "0":
                break

            if not name:
                print("ERROR: Empty brand name!")
                continue

            if self._crud.select_brand(name=name):
                print(f"Brand {name} already exists!")
                continue

            self._crud.create_brand(brand_name=name)
            print(f"Brand {name} added to database")
            break

    def read_brand(self):
        while True:

            id = input("Input brand ID [0=break]: ")

            if id == "0":
                break

            try:
                id = int(id)
            except:
                print(f"ERROR: Invalid brand ID='{id}' (must be INTEGER type)")
                continue

            brand = self._crud.select_brand(id=id)

            if brand is None:
                print(f"ERROR: Brand with ID='{id}' does not exist!")
            else:
                print(f"ID={id}, brand: '{brand}'")
                break

    def update_brand(self):
        while True:

            id = input("Input brand ID [0=break]: ")

            if id == "0":
                break

            try:
                id = int(id)
            except:
                print(f"ERROR: Invalid brand ID='{id}' (must be INTEGER type)")
                continue

            brand = self._crud.select_brand(id=id)

            if brand is None:
                print(f"ERROR: Brand with ID='{id}' does not exist!")
                continue

            while True:
                name = input(f"Input brand name [old: {brand.name}]: ")

                if not name:
                    print("ERROR: Empty brand name!")
                    continue

                if self._crud.select_brand(name=name) is not None:
                    print(f"ERROR: Brand {name} already exists!")
                    continue

                if self._crud.update_brand(id=id, brand_name=name):
                    print(f"Brand '{brand.name}' update to '{name}'")
                    break
            break

    def delete_brand(self):
        while True:

            id = input("Input brand ID [0=break]: ")

            if id == "0":
                break

            try:
                id = int(id)
            except:
                print(f"ERROR: Invalid brand ID='{id}' (must be INTEGER type)")
                continue

            if not self._crud.is_brand_exists(id=id):
                print(f"ERROR: Brand with ID='{id}' does not exist!")
                continue

            if not self._crud.is_brand_available(id=id):
                print(f"ERROR: Brand with ID='{id}' busy! See 'Cars' table")
                continue

            self._crud.delete_brand(id=id)
            print(f"Brand with ID={id} deleted")
            break

    def create_car(self):
        while True:
            car_brand = input("Input car brand (see table 'Brands'): ").title()

            brand = self._crud.select_brand(name=car_brand)

            if not brand:
                print(f"ERROR: No brand '{car_brand}' in tables 'Brands'! Create brand '{car_brand}' at first!")
                break

            car_model = input("Input car model: ")

            try:
                car_year = int(input("Input car year of release: "))
            except:
                print("ERROR: Invalid input data ('year' must be INTEGER type)")
                continue

            self._crud.create_car(model=car_model, year=car_year, brand=brand)
            print(f"Car '{brand.name} {car_model} {car_year}' created")
            break

    def read_car(self):
        while True:

            id = input("Input car ID [0=break]: ")

            if id == "0":
                break

            try:
                id = int(id)
            except:
                print(f"ERROR: Invalid car ID='{id}' (must be INTEGER type)")
                continue

            car = self._crud.select_car(id=id)

            if car is None:
                print(f"ERROR: Car with ID='{id}' does not exist!")
            else:
                print(f"ID={id}, car: '{car}'")
                break

    def update_car(self):
        while True:

            id = input("Input car ID [0=break]: ")

            if id == "0":
                break

            try:
                id = int(id)
            except:
                print(f"ERROR: Invalid brand ID='{id}' (must be INTEGER type)")
                continue

            car = self._crud.select_car(id=id)

            if car is None:
                print(f"ERROR: Car with ID='{id}' does not exist!")
                continue

            while True:

                car_model = input(f"Input car model [old: '{car.model}']: ")
                car_year = input(f"Input car year of release [old: '{car.release_year}']: ")

                if car_year == "":
                    car_year = None
                else:
                    try:
                        car_year = int(car_year)
                    except:
                        print("ERROR: Invalid input data ('year' must be INTEGER type)")
                        continue

                print(f"'{car}' updated to '{car.brand} {car_model if car_model else car.model}, "
                      f"{car_year if car_year else car.release_year}'")

                self._crud.update_car(id=id, new_model=car_model if car_model else None, new_year=car_year)
                break

            break

    def delete_car(self):
        while True:

            id = input("Input car ID [0=break]: ")

            if id == "0":
                break

            try:
                id = int(id)
            except:
                print(f"ERROR: Invalid car ID='{id}' (must be INTEGER type)")
                continue

            if not self._crud.is_car_exists(id=id):
                print(f"ERROR: Car with ID='{id}' does not exist!")
                continue

            self._crud.delete_car(id=id)
            print(f"Car with ID={id} deleted")
            break


if __name__ == '__main__':
    user = User()
    user.run()
