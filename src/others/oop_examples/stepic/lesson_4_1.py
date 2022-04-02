# НАСЛЕДОВАНИЕ

class Person:   # parent

    def can_breathe(self):
        print("Я могу дышать")

    def can_walk(self):
        print("Я могу ходить")


class Doctor(Person):   # subclass

    def can_cure(self):
        print("Я могу лечить")


class Ortoped(Doctor):
    pass


class Architect(Person):    # subclass

    def can_duild(self):
        print("Я могу построить здание")


if __name__ == '__main__':
    p = Person()
    d = Doctor()
    a = Architect()
    o = Ortoped()

    print(issubclass(Doctor, Person))

    p.can_breathe()
    p.can_walk()

    d.can_cure()
    d.can_walk()
    d.can_breathe()

    a.can_duild()
    a.can_walk()
    a.can_breathe()

    o.can_walk()
    o.can_breathe()
    o.can_cure()
