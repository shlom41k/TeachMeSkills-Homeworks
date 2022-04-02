# Полиморфизм

from math import pi


class Rectangle:

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Rectangle {self.a}x{self.b}"

    def get_area(self):
        return self.a * self.b


class Square:

    def __init__(self, a: int):
        self.a = a

    def __str__(self):
        return f"Square {self.a}x{self.a}"

    def get_area(self):
        return self.a ** 2


class Circle:
    def __init__(self, r: int):
        self.r = r

    def __str__(self):
        return f"Circle radius={self.r}"

    def get_area(self):
        return self.r ** 2 * pi
