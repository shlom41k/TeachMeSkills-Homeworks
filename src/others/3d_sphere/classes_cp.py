import decimal
from decimal import Decimal as dec

decimal.getcontext().prec = 7
decimal.getcontext().rounding = decimal.ROUND_HALF_UP


class Vec2:

    def __init__(self, x, y=None):
        self.__x = dec(x)
        if y is None:
            self.__y = dec(x)
        else:
            self.__y = dec(y)

    def __str__(self):
        return f"x={self.__x}, y={self.__y}"

    def __add__(self, other):
        if type(self) == type(other):
            return Vec2(self.__x + other.__x, self.__y + other.__y)
        elif type(other) == int:
            return Vec2(self.__x + other, self.__y + other)
        elif type(other) == float:
            return Vec2(self.__x + dec(other), self.__y + dec(other))

    def __sub__(self, other):
        if type(self) == type(other):
            return Vec2(self.__x - other.__x, self.__y - other.__y)
        elif type(other) == int:
            return Vec2(self.__x - other, self.__y - other)
        elif type(other) == float:
            return Vec2(self.__x - dec(other), self.__y - dec(other))

    def __mul__(self, other):
        if type(self) == type(other):
            return Vec2(self.__x * other.__x, self.__y * other.__y)
        elif type(other) == int:
            return Vec2(self.__x * other, self.__y * other)
        elif type(other) == float:
            return Vec2(self.__x * dec(other), self.__y * dec(other))

    def __truediv__(self, other):
        if type(self) == type(other):
            return Vec2(self.__x / other.__x, self.__y / other.__y)
        elif type(other) == int:
            return Vec2(self.__x / other, self.__y / other)
        elif type(other) == float:
            return Vec2(self.__x / dec(other), self.__y / dec(other))

    def __neg__(self):
        return Vec2(-self.__x, -self.__y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        if type(x) == dec:
            self.__x = x
        elif type(x) in [int, float]:
            self.__x = dec(x)

    @y.setter
    def y(self, y):
        if type(y) == dec:
            self.__y = y
        elif type(y) in [int, float]:
            self.__y = dec(y)


class Vec3:

    def __init__(self, x, y=None, z=None, v=None):
        self.__x = dec(x)
        if y is None and z is None and v is None:
            self.__y = dec(x)
            self.__z = dec(x)
        elif y is not None and z is not None:
            self.__y = dec(y)
            self.__z = dec(z)
        elif v is not None:
            self.__y = v.x
            self.__z = v.y

    def __str__(self):
        return f"x={self.__x}, y={self.__y}, z={self.__z}"

    def __add__(self, other):
        if type(self) == type(other):
            return Vec3(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)
        elif type(other) == int:
            return Vec3(self.__x + other, self.__y + other, self.__z + other)
        elif type(other) == float:
            return Vec3(self.__x + dec(other), self.__y + dec(other), self.__z + dec(other))

    def __sub__(self, other):
        if type(self) == type(other):
            return Vec3(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)
        elif type(other) == int:
            return Vec3(self.__x - other, self.__y - other, self.__z - other)
        elif type(other) == float:
            return Vec3(self.__x - dec(other), self.__y - dec(other), self.__z - dec(other))

    def __mul__(self, other):
        if type(self) == type(other):
            return Vec3(self.__x * other.__x, self.__y * other.__y, self.__z * other.__z)
        elif type(other) == int:
            return Vec3(self.__x * other, self.__y * other, self.__z * other)
        elif type(other) == float:
            return Vec3(self.__x * dec(other), self.__y * dec(other), self.__z * dec(other))

    def __truediv__(self, other):
        if type(self) == type(other):
            if other.__x != 0 and other.__y != 0 and other.__z != 0:
                return Vec3(self.__x / other.__x, self.__y / other.__y, self.__z / other.__z)
            else:
                return Vec3(self.__x / other.__x, self.__y / -0.01, self.__z / other.__z)
        elif type(other) == int:
            return Vec3(self.__x / other, self.__y / other, self.__z / other)
        elif type(other) == float:
            return Vec3(self.__x / dec(other), self.__y / dec(other), self.__z / dec(other))

    def __neg__(self):
        return Vec3(-self.__x, -self.__y, -self.__z)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    @x.setter
    def x(self, x):
        if type(x) == dec:
            self.__x = x
        elif type(x) in [int, float]:
            self.__x = dec(x)

    @y.setter
    def y(self, y):
        if type(y) == dec:
            self.__y = y
        elif type(y) in [int, float]:
            self.__y = dec(y)

    @z.setter
    def z(self, z):
        if type(z) == dec:
            self.__z = z
        elif type(z) in [int, float]:
            self.__z = dec(z)


if __name__ == "__main__":
    def test_fun():
        v1 = Vec2(1, 4)
        print(v1)

        v2 = Vec2(1.1, -5.4)
        print(v2.x > 1.1)

        v3 = Vec3(2, 4, 5)
        print(v3)

        print(v3 * 0.2)


    test_fun()
