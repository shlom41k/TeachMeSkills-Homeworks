# Множественное наследование
# mro

class Doctor:

    def __init__(self, degree):
        self.degree = degree

    def graduate(self):
        print("Я отучился на доктора")

    def can_build(self):
        print("Я доктор, но я тоже умею строить, но не очень")


class Builder:

    def __init__(self, rang):
        self.rang = rang

    def graduate(self):
        print("Я отучился на строителя")

    def can_build(self):
        print("Я строитель, я умею строить")


class Person(Doctor, Builder):

    def __init__(self, rank, degree):
        # self.rang = rank
        # self.degree = degree

        super().__init__(degree)
        Builder.__init__(self, rank)

    def __str__(self):
        return f"Person {self.rang} {self.degree}"


if __name__ == "__main__":
    s = Person(5, "spec")

    print(s)
