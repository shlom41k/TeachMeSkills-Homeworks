# __eq__
# __hash__

class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


if __name__ == '__main__':
    p1 = Point(1, 1)
    p2 = Point(1, 1)

    print(isinstance(p1, object))
    print(isinstance(p2, object))

    print(id(p1), id(p2))
    # print(hash(p1), hash(p2))

    print(p1 == p2)
    print(hash(p1), hash(p2))

    my_dict = {p1: 1}
    print(my_dict)