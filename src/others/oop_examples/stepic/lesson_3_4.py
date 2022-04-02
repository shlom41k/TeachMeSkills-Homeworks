class Rectangle:

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    @property
    def area(self) -> int:
        return self.a * self.b

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area

        elif isinstance(other, (int, float)):
            return self.area < other

    def __le__(self, other):
        return self == other or self < other


class ChessPlayer:

    def __init__(self, name: str, surname: str, rating: int):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, int):
            return self.rating == other
        elif isinstance(other, self.__class__):
            return self.rating == other.rating
        else:
            return "Невозможно выполнить сравнение"

    def __gt__(self, other):
        if isinstance(other, int):
            return self.rating > other
        elif isinstance(other, self.__class__):
            return self.rating > other.rating
        else:
            return "Невозможно выполнить сравнение"

    def __lt__(self, other):
        if isinstance(other, int):
            return self.rating < other
        elif isinstance(other, self.__class__):
            return self.rating < other.rating
        else:
            return "Невозможно выполнить сравнение"


if __name__ == '__main__':
    magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
    ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
    print(magnus == 4000)  # False
    print(ian == 2789)  # True
    print(magnus == ian)  # False
    print(magnus > ian)  # True
    print(magnus < ian)  # False
    print(magnus < [1, 2])  # печатает "Невозможно выполнить сравнениe"
    # r1 = Rectangle(3, 4)
    # r2 = Rectangle(3, 4)
    # r3 = Rectangle(4, 3)
    #
    # print(r1 == r2)
    # print(r1 < r2)
    # print(r1 < r3)
    # print(r1.area)
    # print(r3.area)
    #
    # print(r2 < 44)
    #
    # print(r3 <= r1)
