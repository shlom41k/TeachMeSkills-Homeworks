# Task 12.2
# shlom41k

"""
# Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран
"""


from classes import Point, Figure, Circle, Triangle, Square


if __name__ == "__main__":

    def main():

        p1, p2, p3, p4 = Point(0, 0), Point(-3, 3), Point(-2, -19), Point(3, 9)
        print("Points:", p1, p2, p3, p4)
        print(f"Number of points in class Point: {Point.get_points_cnt()}")
        del p1
        print(f"Number of points in class Point: {Point.get_points_cnt()}\n")

        o1 = Circle(center=Point(1, 1), r=6)
        o2 = Circle(center=Point(5, -2), r=2)

        print(f"Number of circles in class Circle: {Circle.get_circles_cnt()}")
        print(f"Number of figures in class Figure: {Figure.figures_cnt()}\n")

        abc = Triangle(Point(-1, -2), Point(3, 4), Point(8, -6))
        mnk = Triangle(Point(0, 0), Point(0, 4), Point(10, 0))

        print(f"Number of triangles in class Triangle: {Triangle.get_triangle_cnt()}")
        print(f"Number of figures in class Figure: {Figure.figures_cnt()}\n")

        abcd = Square(Point(1, 1), Point(6, 6))
        mnko = Square(Point(-1, 1), Point(-8, -8))

        print(f"Number of squares in class Square: {Square.get_square_cnt()}")
        print(f"Number of figures in class Figure: {Figure.figures_cnt()}\n")

        figures = [o1, o2, abc, mnk, abcd, mnko]

        for fig in figures:
            print(f"{fig.get_info()}, perimetr: {fig.perimetr()}, square: {fig.square()}")

        print(f"\nNumber of circles in class Circle: {Circle.get_circles_cnt()}")
        print(f"Number of triangles in class Triangle: {Triangle.get_triangle_cnt()}")
        print(f"Number of squares in class Square: {Square.get_square_cnt()}")
        print(f"Number of figures in class Figure: {Figure.figures_cnt()}")

        del figures     # delete list !!!
        del abcd        # delete Square
        del abc         # delete Triangle

        print(f"\nNumber of circles in class Circle: {Circle.get_circles_cnt()}")
        print(f"Number of triangles in class Triangle: {Triangle.get_triangle_cnt()}")
        print(f"Number of squares in class Square: {Square.get_square_cnt()}")
        print(f"Number of figures in class Figure: {Figure.figures_cnt()}\n")


    main()



