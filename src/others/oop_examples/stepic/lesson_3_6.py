# __bool__


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __len__(self):
        print("Call __len__")
        return abs(self.x - self.y)

    def __bool__(self):
        print("Call __bool__")
        return True if (self.x or self.y) else False


class City:

    def __init__(self, name: str):
        self.name = name.title()

    def __str__(self):
        return self.name

    def __bool__(self):
        return False if self.name[-1] in ["a", "e", "i", "o", "u"] else True


class Quadrilateral:

    def __init__(self, width: int, height: (int, None) = None):
        self.width = width

        # if height is None:
        #     self.height = width
        # else:
        #     self.height = height

        self.height = height or width

    def __str__(self):
        return f"Куб размером {self.width}х{self.height}" if self.width == self.height else \
            f"Прямоугольник размером {self.width}х{self.height}"

    def __bool__(self):
        return self.width == self.height


if __name__ == '__main__':
    q1 = Quadrilateral(10)
    print(q1)  # печатает "Куб размером 10х10"
    print(bool(q1))  # печатает "True"
    q2 = Quadrilateral(3, 5)
    print(q2)  # печатает "Прямоугольник размером 3х5"
    print(q2 == True)  # печатает "False"


    # p1 = City('new york')
    # print(p1)  # печатает "New York"
    # print(bool(p1))  # печатает "True"
    # p2 = City('SaN frANCISco')
    # print(p2)  # печатает "San Francisco"
    # print(p2 == True)  # печатает "False"

    # p1 = Point(2, 2)
    # print(bool(p1))
    #
    # print(bool(Point(1, 3)))
    # print(bool(Point(1, 0)))
    # print(bool(Point(-1, 0)))
    # print(bool(Point(0, 1)))
    # print(bool(Point(0, 0)))
    # print(bool(Point(5, 5)))
