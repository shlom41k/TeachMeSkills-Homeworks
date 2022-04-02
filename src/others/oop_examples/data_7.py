class Point:

    points_cnt = 0

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.__class__.points_cnt += 1

    def __del__(self):
        self.__class__.points_cnt -= 1

    def __str__(self):
        return f"Point: x={self.x}, y={self.y}"

    @classmethod
    def points(cls):
        return cls.points_cnt

    @property
    def xx(self):
        return self.x


if __name__ == "__main__":
    print("Class cnt:", Point.points_cnt)

    p1 = Point(0, 0)
    print("Class cnt:", Point.points_cnt)
    print("Self cnt:", p1.points_cnt)

    p2 = Point(0, 0)
    print("Class cnt:", Point.points_cnt)
    print("Self cnt:", p1.points_cnt)


