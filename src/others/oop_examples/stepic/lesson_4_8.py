
class Rectangle:

    __slots__ = ("__width", "height")

    def __init__(self, width: (int, float), height: (int, float)):
        self.width = width
        self.height = height

    @property
    def perimetr(self):
        return (self.width + self.height) * 2

    @property
    def area(self):
        return self.width * self.height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: (int, float)):
        self.__width = width
        print("Setter called")


class Square(Rectangle):

    __slots__ = ("color")

    def __init__(self, width: (int, float), height: (int, float), color: str):
        super().__init__(width, height)
        self.color = color


if __name__ == "__main__":
    r = Rectangle(3, 4)

    print(r.width)

    s = Square(4, 5, "red")
    print(s.width)
    print(s.height)
    print(s.color)
    print(s.area)
    print(s.perimetr)


