from accessify import protected, private


class Car:

    def __init__(self, brand: str, model: str):
        self.__brand = brand
        self.__model = model

    @protected
    def __print_data(self):
        print(f"Car: {self.__brand} {self.__model}")


car = Car("Opel", "Corsa")

car._Car__print_data()

