# Наследование
# Делегирование


class Person:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Person {self.name} {self.surname}"

    def info(self):
        print(f"Parent class, self={self}")

    def breathe(self):
        print("Человек дышит")


class Doctor(Person):

    def __init__(self, name: str, surname: str, age: int):
        super().__init__(name, surname)
        self.age = age

    def __str__(self):
        return f"Doctor {self.name} {self.surname}"

    def breathe(self):
        print("Доктор дышит")
        super().breathe()


if __name__ == '__main__':

    p = Person("Ivan", "Ivanov")
    d = Doctor("Petr", "Petrovich", 22)

    print(p.name, p.surname)
    print(d.name, d.surname, d.age)

    d.info()
