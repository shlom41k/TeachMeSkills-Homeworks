# __getitem__
# __setitem__ <- позволяет создать разряженный список
# __delitem__

class Vector:

    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item: int):
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            raise IndexError("Index our of collection range")

    def __setitem__(self, key: int, value):
        if 0 <= key < len(self.values):
            self.values[key] = value
        else:
            raise IndexError("Index our of collection range")

    def __delitem__(self, key: int):
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError("Index our of collection range")


if __name__ == '__main__':
    v1 = Vector(1, 2, 3, 4, 0)
    print(v1)

    print(v1[2])
    print(v1[0])
    # print(v1[10])
    v1[0] = 0
    print(v1)

    del v1[0]
    print(v1)
