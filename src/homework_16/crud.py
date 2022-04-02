# shom41k
# homework 16

"""
# Create CRUD class for homework #16
"""


from db_creator import Brand, Car, session
from tabulate import tabulate


class CRUD:

    _session = None

    def __init__(self, session):
        # При создании экземпляра класса автоматически создаем сессию
        self.connect_to_db(session)

    def connect_to_db(self, session):
        # Создание сессии
        self._session = session

    def is_brand_exists(self, id: int):
        # Проверка, существует ли Brand с таким id в БД --> (True or False)
        return True if (self._session.query(Brand).filter(Brand.id == id).first()) else False

    def is_brand_available(self, id: int):
        """
        # Проверка, существует ли Сar с таким brand_id в БД
        # Если существует - Brand занят --> (False)
        # Если не существует - Brand свободен --> (True)
        """
        return True if self._session.query(Car).filter(Car.brand_id == id).first() is None else False

    def create_brand(self, brand_name: str):
        """
        # Создание нового бренда.
        # Если в БД нет такого бренда - добавляем --> (True)
        # Если есть - игнорируем --> (False)
        """
        if self._session.query(Brand).filter(Brand.name == brand_name).first():
            # print(f"Brand {brand_name} already exists!")
            return False
        else:
            self._session.add(Brand(name=brand_name))
            self._session.commit()
            # print(f"Brand {brand_name} added to database")
            return True

    def update_brand(self, id: int, brand_name=None):
        """
        # Обновление бренда по id
        # Если такого id нет - игнорируем --> (False)
        # Если не указан новый brand_name - игнорируем --> (False)
        # Если все ОК - обновляем --> (True)
        """
        brand = self._session.query(Brand).filter(Brand.id == id).first()

        if brand is None or brand_name is None:
            return False

        self._session.query(Brand).filter(Brand.id == id).update(
            {Brand.name: brand_name}, synchronize_session=False)
        # print(f"Brand '{brand.name}' update to '{brand_name}'")
        self._session.commit()

        return True

    def delete_brand(self, id):
        # Удаление бренда по id
        self._session.query(Brand).filter(Brand.id == id).delete()
        self._session.commit()
        # print("Brand with ID [{}] deleted".format(id))

    def select_brand(self, id=None, name=None):
        # Получение записи из таблицы "brands" по id или по name
        if id:
            return self._session.query(Brand).filter(Brand.id == id).first()
        elif name:
            return self._session.query(Brand).filter(Brand.name == name).first()
        else:
            return None

    def select_all_brands(self):
        # Получение всех записей из таблицы "brands"
        return self._session.query(Brand).order_by(Brand.id)

    def show_all_brands(self):
        # Вывод в консоль всех записей из таблицы "brands"
        data = []
        headers = ["ID", "BRAND"]

        for brand in self.select_all_brands():
            data.append([brand.id, brand.name])

        print("\nData in table:\n", tabulate(data, headers=headers, stralign='left'))

    def is_car_exists(self, id: int):
        # Проверка, существует ли CAR с таким id в БД --> (True or False)
        return True if (self._session.query(Car).filter(Car.id == id).first()) else False

    def create_car(self, model: str, year: int, brand: Brand):
        # Создание новой машины
        self._session.add(Car(model=model, release_year=year, brand=brand))
        self._session.commit()

    def update_car(self, id:int, new_model=None, new_year=None):
        # Редактирование существующей машины
        car = self._session.query(Car).filter(Car.id == id).first()

        if car is None:
            return False

        if new_model is not None:
            car.model = new_model
        if new_year is not None:
            car.release_year = new_year

        self._session.query(Car).filter(Car.id == id).update(
            {
                Car.model: car.model,
                Car.release_year: car.release_year,
            },
            synchronize_session=False)

        self._session.commit()
        return True

    def delete_car(self, id):
        # Удаление машины
        self._session.query(Car).filter(Car.id == id).delete()
        self._session.commit()
        # print("Car with ID [{}] deleted".format(id))

    def select_car(self, id):
        # Получение записи из таблицы "cars" по id
        return self._session.query(Car).filter(Car.id == id).first()

    def select_all_cars(self):
        # Получение всех записей из таблицы "cars"
        return self._session.query(Car).order_by(Car.id)

    def show_all_cars(self):
        # Вывод в консоль всех записей из таблицы "cars"
        data = []
        headers = ["ID", "BRAND", "MODEL", "YEAR"]

        for car in self.select_all_cars():
            data.append([car.id, car.brand, car.model, car.release_year])

        print("\nData in table:\n", tabulate(data, headers=headers, stralign='left'))


if __name__ == "__main__":

    c = CRUD(session=session)

    brand = c.select_brand(name="Opel")
    if brand:
        print("Exists")



