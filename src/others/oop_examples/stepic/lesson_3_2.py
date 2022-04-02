class Person:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __len__(self) -> int:
        return len(self.name + self.surname)


class Otrezok:

    def __init__(self, point1: int, point2: int):
        self.x1 = point1
        self.x2 = point2

    def __len__(self) -> int:
        return abs(self)

    def __abs__(self):
        return abs(self.x2 - self.x1)


if __name__ == "__main__":
    b = Person("aaa", "12345")
    print(len(b))

    b2 = Person("1", "23")
    print(len(b2))

    q = Otrezok(3, 9)
    print(len(q))

    q2 = Otrezok(9, 4)
    print(len(q2))