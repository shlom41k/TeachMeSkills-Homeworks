class Lion:

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"The object Lion - {self.name}"

    def __str__(self):
        return f"Lion - {self.name}"


class Person:

    def __init__(self, name: str, surname: str, gender: str = "male"):
        self.name = name
        self.surname = surname

        if gender not in ["male", "female"]:
            print(f"Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            self.gender = "male"
        else:
            self.gender = gender

    def __str__(self):
        return f"{'Гражданин' if self.gender == 'male' else 'Гражданка'} {self.surname} {self.name}"


class Vector:

    def __init__(self, *args):
        self.values = [val for val in args if isinstance(val, int)]

    def __str__(self):
        return f"Вектор({', '.join(sorted([str(n) for n in self.values]))})" if self.values else "Пустой вектор"


if __name__ == "__main__":

    # q = Lion("Bob")
    # print(q)
    # print(q)

    # p1 = Person('Chuck', 'Norris')
    # print(p1)  # печатает "Гражданин Norris Chuck"
    # p2 = Person('Mila', 'Kunis', 'female')
    # print(p2)  # печатает "Гражданка Kunis Mila"
    # p3 = Person('Оби-Ван', 'Кеноби', True)  # печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
    # print(p3)  # печатает "Гражданин Кеноби Оби-Ван"

    v1 = Vector(2, 1, 3)
    print(v1)  # печатает "Вектор(1, 2, 3)"
    v2 = Vector()
    print(v2)  # печатает "Пустой вектор"