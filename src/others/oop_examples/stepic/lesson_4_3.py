# Наследование
# Переопределение методов

class Person:   # parent

    def __init__(self, name: str):
        print("Person init")
        self.name = name

    def breathe(self):
        print("Человек дышит")

    def walk(self):
        print("Человек идет")

    def sleep(self):
        print("Человек спит")

    def comdo(self):
        self.breathe()
        self.walk()
        self.sleep()

    def __str__(self):
        return f"Human {self.name}"


class Doctor(Person):
    def breathe(self):
        print("Доктор тоже дышит")

    def __str__(self):
        return f"Doctor {self.name}"


if __name__ == '__main__':

    name = "Ivan"

    p = Person("John")
    d = Doctor("Adam")

    d.breathe()
    d.walk()

    p.walk()
    p.breathe()

    print(p.name)
    print(d.name)

    print(d)
    print(p)

    p.comdo()
    d.comdo()