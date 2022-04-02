from lesson_3_8 import Rectangle, Square, Circle


rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)

print(f"Area r1: {rect1.get_area()}, area r2: {rect2.get_area()}")

sq1 = Square(5)
sq2 = Square(7)

print(f"Area s1: {sq1.get_area()}, area r2: {sq2.get_area()}")

c1 = Circle(3)
c2 = Circle(2)

figures = [rect1, rect2, sq1, sq2, c1, c2]

for figure in figures:
    print(f"Figure: {figure}, area={figure.get_area()}")