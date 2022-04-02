# Task 11.2
# shlom41k

"""
# Создать класс Car.
# Атрибуты: марка, модель, год выпуска, скорость(по умолчанию 0).
# Методы: увеличить скорости(скорость + 5), уменьшение скорости(скорость - 5), стоп(сброс скорости на 0),
# отображение скорости, разворот(изменение знака скорости).
# Все атрибуты приватные.
"""


class Car:
    def __init__(self, brand: str, model: str, year: int, speed=0):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    @property
    def name(self):
        return self.__brand, self.__model

    def speed_up(self):
        self.__speed += 5

    def speed_down(self):
        self.__speed -= 5

    def stop(self):
        self.__speed = 0

    def reverse(self):
        self.__speed = -self.__speed

    def get_info(self):
        print(f"Car: {self.__brand} {self.__model}, {self.__year} year, speed = {self.__speed} km/h")


if __name__ == "__main__":
    car = Car("WW", "Polo", 2017, 55)
    car.get_info()
    print(*car.name, car.speed)
    car.get_info()
    car.speed_up()
    car.get_info()
    car.speed_down()
    car.speed_down()
    car.get_info()
    car.reverse()
    car.get_info()
    car.stop()
    car.get_info()

    car.__model = "11111111111"
    print(car.__model)
    car.get_info()



