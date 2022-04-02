# __iter__
# __next__

class Marks:

    def __init__(self, values: list):
        self.values = values
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        print("Called next Marks")
        if self.index >= len(self.values):
            self.index = 0
            raise StopIteration
        letter = self.values[self.index]
        self.index += 1
        return letter


class Student:

    def __init__(self, name: str, surname: str, marks: Marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __getitem__(self, item):
        return self.marks[item]

    def __iter__(self):
        print("Called iter")
        self.index = 0
        return iter(self.marks)

    def __next__(self):
        print("Called next Student")
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter


if __name__ == "__main__":
    m = Marks([5, 4, 3, 4, 5, 2])
    s1 = Student("Ivan", "Ivanov", m)

    for i in s1:
        print(i)