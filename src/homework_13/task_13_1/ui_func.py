"""
# Task 13.1
# shlom41k
"""

from func import *


def calc():
    print("Добро пожаловать в миникалькулятор!\n")

    while True:
        op = get_operation()

        if op == "0":
            print("Выход из программы")
            break

        a = input("Введите число а: ")
        b = input("Введите число b: ")

        if not is_num_valid(a) or not is_num_valid(b):
            raise MyNumException("Error! Invalid input arguments!")
        else:
            a, b = float(a), float(b)

        get_result(a, b, op)


if __name__ == "__main__":
    calc()