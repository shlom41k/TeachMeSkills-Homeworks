class BankAccount:

    def __init__(self, name: str, balance: (int, float)):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f"Client {self.name} with balance {self.balance}"

    def __add__(self, other: (int, float)):
        print(f"__add__ called")

        if isinstance(other, self.__class__):
            return self.balance + other.balance

        if isinstance(other, (int, float)):
            return self.balance + other

        raise NotImplemented

    def __radd__(self, other):
        print(f"__radd__ called")
        return self + other

    def __mul__(self, other: (int, float)):
        print(f"__mul__ called")

        if isinstance(other, self.__class__):
            return self.balance * other.balance

        if isinstance(other, (int, float)):
            return self.balance * other

        if isinstance(other, str):
            return self.name + other

        raise NotImplemented


class Vector:

    def __init__(self, *args: int):
        self.values = sorted([val for val in args if isinstance(val, int)])

    def __str__(self):
        return f"Вектор({', '.join(([str(n) for n in sorted(self.values)]))})" if self.values else "Пустой вектор"

    def __add__(self, other):
        if isinstance(other, int):
            return Vector(*[val + other for val in self.values])

        elif isinstance(other, self.__class__):
            if len(self.values) == len(other.values):
                return Vector(*[val + other.values[ind] for ind, val in enumerate(self.values)])
            else:
                print("Сложение векторов разной длины недопустимо")

        else:
            print(f"Вектор нельзя сложить с {other}")

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(*[val * other for val in self.values])

        elif isinstance(other, self.__class__):
            if len(self.values) == len(other.values):
                return Vector(*[val * other.values[ind] for ind, val in enumerate(self.values)])
            else:
                print("Умножение векторов разной длины недопустимо")

        else:
            print(f"Вектор нельзя умножать с {other}")


if __name__ == "__main__":
    # r = BankAccount("Misha", 12)
    # t = BankAccount("Anya", 56)
    #
    # print(r + 12)
    # print(r + t)
    # print(15 + r)
    #
    # print(r * 3)
    # print(r * "3")

    v1 = Vector(1, 2, 3)
    print(v1)  # печатает "Вектор(1, 2, 3)"

    v2 = Vector(3, 4, 5)
    print(v2)  # печатает "Вектор(3, 4, 5)"

    v3 = v1 + v2
    print(v3)  # печатает "Вектор(4, 6, 8)"

    v4 = v3 + 5
    print(v4)  # печатает "Вектор(9, 11, 13)"

    v5 = v1 * 2
    print(v5)  # печатает "Вектор(2, 4, 6)"

    v5 + 'hi'  # печатает "Вектор нельзя сложить с hi"

    print(v1.values)