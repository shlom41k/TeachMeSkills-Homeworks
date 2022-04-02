# Task 11.1
# shlom41k

"""
# Создать пять классов описывающие реальные объекты.
# Каждый класс должен содержать минимум три приватных атрибута, конструктор,
# геттеры и сеттеры для каждого атрибута, два метода.
"""


class Cat:
    def __init__(self, name: str, age: int, color: str):
        self.__name = name
        self.__age = age
        self.__color = color

    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    @age.setter
    def age(self, age):
        if 1 < age < 25:
            self.__age = age
        else:
            print("Введен неверный возраст")

    @name.setter
    def name(self, name):
        self.__name = name

    @color.setter
    def color(self, color):
        self.__color = color

    def say_meow(self):
        print(f"{self.__name} say: meow-meow")

    def disp_info(self):
        print(f"Name: {self.__name}; age: {self.__age}; color: {self.__color}")


class Car:
    def __init__(self, brand, model, power, color):
        self.__brand = brand
        self.__model = model
        self.__power = power
        self.__color = color

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def power(self):
        return self.__power

    @property
    def color(self):
        return self.__color

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @model.setter
    def model(self, model):
        self.__model = model

    @power.setter
    def power(self, power):
        self.__power = power

    @color.setter
    def color(self, color):
        if color.lower() in ["red", "green", "blue", "yellow", "black", "white", "gray"]:
            self.__color = color
        else:
            print("Error: Forbidden color")

    def get_info(self):
        print(f"Brand: {self.__brand}, model: {self.__model}, power: {self.__power}, color: {self.__color}")

    def honk(self):
        print(f"{self.__brand} {self.__model} say: Beeeeep-beeeeeep")


class FPGA:
    def __init__(self, type: str, family: str, name: str, luts: int, package="FFVB900"):
        self.__type = type
        self.__family = family
        self.__name = name
        self.__luts = luts
        self.__available_loots = luts
        self.__package = package

    # Properties
    @property
    def type(self):
        return self.__type

    @property
    def family(self):
        return self.__family

    @property
    def name(self):
        return self.__name

    @property
    def luts(self):
        return self.__luts, self.__available_loots

    @property
    def package(self):
        return self.__package

    # Setters
    @type.setter
    def type(self, type: str):
        self.__type = type

    @name.setter
    def name(self, name: str):
        self.__name = name

    @family.setter
    def family(self, family):
        self.__family = family

    @luts.setter
    def luts(self, luts: int):
        self.__available_loots = self.__available_loots + (luts - self.__luts)
        self.__luts = luts

    @package.setter
    def package(self, package: str):
        if package in ["FFVB900", "FFVB1560", "FFVB676", "FFVT900", "FFVT1156", "BGA900"]:
            self.__package = package
        else:
            print("Error! This type of package doesn't exists")

    # Methods
    def hold_luts(self, luts: int):
        if self.__available_loots - luts < 0:
            print(f"Don't have {luts} free luts. Now {self.__available_loots} are available")
        else:
            self.__available_loots -= luts

    def reset_loots(self):
        self.__available_loots = self.__luts


class Computer:
    def __init__(self, type: str, processor: str, memory_size: int, video_adapter: str):
        self.__type = type
        self.__processor = processor
        self.__memory_size = memory_size
        self.__video_adapter = video_adapter
        self.__free_memory = memory_size

    @property
    def type(self):
        return self.__type

    @property
    def proc(self):
        return self.__processor

    @property
    def memory(self):
        return self.__memory_size

    @property
    def free_memory(self):
        return self.__free_memory

    @property
    def video_adapter(self):
        return self.__video_adapter

    @type.setter
    def type(self, type: str):
        self.__type = type

    @proc.setter
    def proc(self, proc: str):
        self.__processor = proc

    @memory.setter
    def memory(self, memory):
        self.__memory_size = memory

    def run_task(self, mem_size: int):
        if self.__free_memory < mem_size:
            print("Error: Not enough memory")
        else:
            self.__free_memory -= mem_size

    def close_task(self, mem_size: int):
        if self.__memory_size < mem_size:
            self.__free_memory = self.__memory_size
        elif self.__free_memory + mem_size > self.__memory_size:
            self.__free_memory = self.__memory_size
        else:
            self.__free_memory += mem_size

    def clear_memory(self):
        self.__free_memory = self.__memory_size

    def get_info(self):
        print(f"{self.__type}, processor: {self.__processor}, "
              f"total memory: {self.__memory_size} MB, free memory: {self.__free_memory} MB")


class Gun:
    def __init__(self, model: str, weight: float, distance: int, magazin=9):
        self.__model = model
        self.__magazin = magazin
        self.__shots = magazin
        self.__weight = weight
        self.__distance = distance

    @property
    def model(self):
        return self.__model

    @property
    def weight(self):
        return self.__weight

    @property
    def distance(self):
        return self.__distance

    @property
    def patrons(self):
        return self.__shots

    @property
    def magazin(self):
        return self.__magazin

    @model.setter
    def model(self, model: str):
        self.__model = model

    @weight.setter
    def weight(self, weight: float):
        self.__weight = weight

    @distance.setter
    def distance(self, len: int):
        self.__distance = len

    @magazin.setter
    def magazin(self, size: int):
        self.__magazin = size
        self.__shots = size

    def shot(self):
        if self.__shots > 0:
            self.__shots -= 1
            print("Pif-puf")
        else:
            print("No patrons! Reload right now!")

    def reload(self):
        self.__shots = self.__magazin

    def show_info(self):
        print(f"{self.__model}, patrons: {self.__shots}, distance = {self.__distance}")


if __name__ == "__main__":

    def testing_cat():
        print("Cat Testing")

        M = Cat("Tom", 4, "black")

        M.disp_info()
        M.age = 5
        M.say_meow()

        print(f"Cat {M.name}, age: {M.age}, color: {M.color}")

    def testing_car():
        print("Car Testing")

        C = Car("Honda", "Civik", 160, "red")

        C.honk()
        C.get_info()
        C.color = "cyan"
        C.get_info()
        C.color = "gray"
        C.get_info()

    def testing_fpga():
        print("FPGA Testing")

        kc410 = FPGA("FPGA", "Kintex-7", "KC410T", 5600, "BGA900")

        print(kc410.type, kc410.family, kc410.name, kc410.package)
        print(kc410.luts)
        kc410.hold_luts(5000)
        print(kc410.luts)
        kc410.hold_luts(500)
        print(kc410.luts)
        kc410.hold_luts(200)
        kc410.reset_loots()
        print(kc410.luts)
        kc410.hold_luts(500)
        print(kc410.luts)
        kc410.luts = 7000
        print(kc410.luts)

    def testing_comp():
        print("Computer Testing")

        my_pc = Computer("Notebook", "Core i7 10-th GEN", 16000, "Nvidia GForce MX250")

        my_pc.get_info()
        my_pc.run_task(500)
        my_pc.get_info()
        my_pc.run_task(1000)
        my_pc.get_info()
        my_pc.close_task(100)
        my_pc.get_info()
        my_pc.close_task(3000)
        my_pc.get_info()
        my_pc.run_task(2300)
        my_pc.get_info()
        my_pc.clear_memory()
        my_pc.get_info()

    def testing_gun():
        print("Gun Testing")

        gun = Gun("Makarov", 0.9, 100)

        gun.show_info()
        gun.shot()
        gun.shot()
        gun.show_info()
        gun.shot()
        gun.shot()
        gun.shot()
        gun.shot()
        gun.shot()
        gun.shot()
        gun.shot()
        gun.shot()
        gun.show_info()
        gun.reload()
        gun.show_info()
        gun.shot()
        print(gun.patrons, gun.magazin)

    # Testing
    testing_cat()
    print()
    testing_car()
    print()
    testing_fpga()
    print()
    testing_comp()
    print()
    testing_gun()

