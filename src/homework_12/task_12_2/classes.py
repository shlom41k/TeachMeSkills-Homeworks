# Task 12.2
# shlom41k

"""
# Создать класс Point, описывающий точку(атрибуты: x, y).
# Создать класс Figure. Создать три дочерних класса:
# -> Circle(атрибуты: координаты центра(тип Point), длина радиуса; методы: нахождение периметра и площади окружности);
# -> Triangle(атрибуты: три точки, методы: нахождение площади и периметра);
# -> Square(атрибуты: две точки, методы: нахождение площади и периметра).
# При потребности создавать все необходимые методы не описанные в задании.
"""


from math import pi, sqrt
from abc import abstractmethod


class Point:

    __point_cnt = 0

    def __init__(self, x: int ,y: int):
        self.__x = x
        self.__y = y

        # Point.__point_cnt += 1
        self.__class__.__point_cnt += 1

    def __del__(self):
        # Point.__point_cnt -= 1
        self.__class__.__point_cnt -= 1

    def __str__(self):
        return f"({self.__x}; {self.__y})"

    @classmethod
    def get_points_cnt(cls):
        return cls.__point_cnt

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x: int):
        self.__x = x

    @y.setter
    def y(self, y: int):
        self.__y = y

    def get_info(self):
        return f"Point ({self.__x}; {self.__y})"


class Figure:

    _figures_cnt = 0

    @abstractmethod
    def perimetr(self):
        raise NotImplemented("ERROR! Abstract method")

    @abstractmethod
    def square(self):
        raise NotImplemented("ERROR! Abstract method")

    @classmethod
    def figures_cnt(cls):
        return cls._figures_cnt


class Circle(Figure):

    __circles_cnt = 0

    def __init__(self, center: Point, r: int):
        self.__center = center
        self.__radius = r

        # Circle.__circles_cnt += 1
        self.__class__.__circles_cnt += 1
        Figure._figures_cnt += 1
        # self.__class__._figures_cnt += 1

    def __del__(self):
        # Circle.__circles_cnt -= 1
        self.__class__.__circles_cnt -= 1
        Figure._figures_cnt -= 1

    def __str__(self):
        return f"({self.__center.x}, {self.__center.y}), {self.__radius}"

    @classmethod
    def get_circles_cnt(cls):
        return cls.__circles_cnt

    @property
    def radius(self):
        return self.__radius

    @property
    def center(self):
        return self.__center

    @radius.setter
    def radius(self, r: int):
        self.__radius = r

    @center.setter
    def center(self, c: Point):
        self.__center = c

    # l = 2*pi*r
    def perimetr(self):
        return round(2 * pi * self.__radius, 3)

    # s = pi*r^2
    def square(self):
        return round(pi * self.__radius ** 2, 3)

    def get_info(self):
        return f"Circle: center - point ({self.__center.x}, {self.__center.y}), radius - {self.__radius}"


class Triangle(Figure):

    __triangle_cnt = 0

    def __init__(self, a: Point, b: Point, c: Point):
        self.__a = a
        self.__b = b
        self.__c = c

        # Triangle.__triangle_cnt += 1
        self.__class__.__triangle_cnt += 1
        Figure._figures_cnt += 1

    def __del__(self):
        # Triangle.__triangle_cnt -= 1
        self.__class__.__triangle_cnt -= 1
        Figure._figures_cnt -= 1

    def __str__(self):
        return f"({self.__a.x}, {self.__a.y}), ({self.__b.x}, {self.__b.y}), ({self.__c.x}, {self.__c.y})"

    @classmethod
    def get_triangle_cnt(cls):
        return cls.__triangle_cnt

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    @a.setter
    def a(self, a: Point):
        self.__a = a

    @b.setter
    def b(self, b: Point):
        self.__b = b

    @c.setter
    def c(self, c: Point):
        self.__c = c

    # Calculate triangle sides
    def str_calc(self):
        s1 = sqrt((self.__b.x - self.__a.x) ** 2 + (self.__b.y - self.__a.y) ** 2)
        s2 = sqrt((self.__c.x - self.__a.x) ** 2 + (self.__c.y - self.__a.y) ** 2)
        s3 = sqrt((self.__b.x - self.__c.x) ** 2 + (self.__b.y - self.__c.y) ** 2)
        return s1, s2, s3

    # p = s1 + s2 + s3
    def perimetr(self):
        return round(sum(self.str_calc()), 3)

    # Gerone formula S = sqrt(pp*(pp-a)*(pp-b)*(pp-c), pp = p / 2
    def square(self):
        s1, s2, s3 = self.str_calc()
        pp = (s1 + s2 + s3) / 2
        return round(sqrt(pp * (pp - s1) * (pp - s2) * (pp - s3)), 3)

    def get_info(self):
        return f"Triangle: A({self.__a.x}, {self.__a.y}), B({self.__b.x}, {self.__b.y}), C({self.__c.x}, {self.__c.y})"


class Square(Figure):

    __square_cnt = 0

    def __init__(self, x1: Point, x2: Point):
        self.__x1 = x1
        self.__x2 = x2

        # Square.__square_cnt += 1
        self.__class__.__square_cnt += 1
        Figure._figures_cnt += 1

    def __del__(self):
        # Square.__square_cnt -= 1
        self.__class__.__square_cnt -= 1
        Figure._figures_cnt -= 1

    def __str__(self):
        return f"({self.__x1.x}, {self.__x1.y}), ({self.__x2.x}, {self.__x2.y})"

    @classmethod
    def get_square_cnt(cls):
        return cls.__square_cnt

    @property
    def x1(self):
        return self.__x1

    @property
    def x2(self):
        return self.__x2

    @x1.setter
    def x1(self, x1: Point):
        self.__x1 = x1

    @x2.setter
    def x2(self, x2: Point):
        self.__x2 = x2

    # Calculate square side
    def str_calc(self):
        a = sqrt((self.__x2.x - self.__x1.x) ** 2)
        return a

    # p = a * 4
    def perimetr(self):
        return round(self.str_calc() * 4, 3)

    # S = a ** 2
    def square(self):
        return round(self.str_calc() ** 2, 3)

    def get_info(self):
        return f"Square: x1({self.__x1.x}, {self.__x1.y}), x2({self.__x2.x}, {self.__x2.y})"


if __name__ == "__main__":

    def main():
        a = Point(0, 0)
        print(a.get_info())

        b = Point(2, 4)
        print(b.get_info())

        c = Point(4, 0)
        print(c.get_info())

        print(f"Number of points in class Point: {Point.get_points_cnt()}")
        del a
        print(f"Number of points in class Point: {Point.get_points_cnt()}")

        o = Circle(center=Point(1, 1), r=4)
        print(f"\n{o.get_info()}")
        print(f"Length: {o.perimetr()}, square: {o.square()}.")
        print(f"Number of circles in class Circle: {Circle.get_circles_cnt()}")
        print(f"Number of figures in class Figure: {Figure.figures_cnt()}")

        abc = Triangle(Point(0, 0), Point(5, 10), Point(10, 0))
        print(f"\n{abc.get_info()}")
        print(abc)
        print(f"Perimetr: {abc.perimetr()}, square: {abc.square()}.")
        print(f"Number of triangles in class Triangle: {Triangle.get_triangle_cnt()}")
        print(f"Number of figures in class Figure: {Figure.figures_cnt()}")

        abcd = Square(Point(1, 1), Point(8, 8))
        print(f"\n{abcd.get_info()}")
        print(f"Perimetr: {abcd.perimetr()}, square: {abcd.square()}.")

        print(f"\nNumber of circles in class Circle: {Circle.get_circles_cnt()}")
        print(f"Number of triangles in class Triangle: {Triangle.get_triangle_cnt()}")
        print(f"Number of squares in class Square: {Square.get_square_cnt()}")
        print(f"Number of figures in class Figure: {Figure.figures_cnt()}")

        del abcd
        del abc

        print(f"\nNumber of circles in class Circle: {Circle.get_circles_cnt()}")
        print(f"Number of triangles in class Triangle: {Triangle.get_triangle_cnt()}")
        print(f"Number of squares in class Square: {Square.get_square_cnt()}")
        print(f"Number of figures in class Figure: {Figure.figures_cnt()}")

    # main()