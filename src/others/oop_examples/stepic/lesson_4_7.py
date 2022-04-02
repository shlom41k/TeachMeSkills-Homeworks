# slots экономит память
# slots не дает создавать новых атрибутов

from timeit import timeit

class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class PointSlots:

    __slots__ = ("x", "y")

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y



if __name__ == "__main__":
    p1 = Point(3, 4)
    print(p1.__sizeof__(), p1.__dict__.__sizeof__())

    s1 = PointSlots(3, 4)
    print(s1.__sizeof__())

    def make_cls_1():
        p = Point(3, 4)
        p.x = 100
        # print(p.x)
        del p.x

    def make_cls_2():
        s = PointSlots(3, 4)
        s.x = 100
        # print(s.x)
        del s.x

    print(timeit(make_cls_1))
    print(timeit(make_cls_2))
