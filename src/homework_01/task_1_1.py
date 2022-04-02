# Task 1.1
# shlom41k

"""
Даны 2 действительных числа a и b. Получить их сумму, разность и произведение.
"""


def print_sum(num1, num2):
    print("Sum =", num1 + num2)


def print_diff(num1, num2):
    print("Diff =", num1 - num2)


def print_mult(num1, num2):
    print("Mult =", num1 * num2)


if __name__ == "__main__":

    a, b = 4, 7

    print_sum(a, b)
    print_diff(a, b)
    print_mult(a, b)
    print()

    sum = a + b
    diff = a - b
    mult = a * b

    print("Sum =", sum)
    print("Diff =", diff)
    print("Mult =", mult,)



