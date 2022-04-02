# Task 8.3
# shlom41k

"""
Описать функцию Sin1(x, ε) вещественного типа (параметры x, ε — вещественные, ε > 0),
находящую приближенное значение функции sin(x):
    sin(x) = x – x^3/(3!) + x^5/(5!) – ... + (–1)^n · x^( 2·n+1)/((2· n +1)!) + ... .
В сумме учитывать все слагаемые, модуль которых больше ε.
С помощью Sin1 найти приближенное значение синуса для данного x при шести данных ε.
"""

from math import factorial, pi, sin


def sin1(x, eps):
    sum = 0     # Сумма ряда
    k = x       # Первый член ряда
    n = 0       # Степень

    while abs(k) > eps:     # eps - точность
        sum += k
        n += 1
        k = pow(-1, n) * (pow(x, 2 * n + 1) / factorial(2 * n + 1))

    return sum


if __name__ == '__main__':

    # Test

    # sin(pi/2) = sin(90) = 1               # my_answer = 0.9998431013994987
    print(f"Real sin: {sin(pi / 2)}, my_sin: {sin1(pi / 2, 0.001)}, eps = {0.001}")

    # sin(pi/4) = sin(45) = (2^0.5) / 2     # my_answer = 0.7071064695751781
    print(f"Real sin: {sin(pi / 4)}, my_sin: {sin1(pi / 4, 0.00001)}, eps = {0.00001}")

    # sin(pi/6) = sin(30) = 0.5             # my_answer = 0.49967417939436376
    print(f"Real sin: {sin(pi / 6)}, my_sin: {sin1(pi / 6, 0.001)}, eps = {0.001}")

    # sin(pi) = sin(180) = 0                # my_answer = -0.00044516023820921277
    print(f"Real sin: {sin(pi)}, my_sin: {sin1(pi, 0.005)}, eps = {0.005}\n")

    for eps in [0.1, 0.01, 0.05, 0.001, 0.002, 0.0005, 0.000001]:
        print(f"sin = {sin(pi/2)}, my_sin = {sin1(pi / 2, eps)}, delta = {sin(pi/2) - sin1(pi / 2, eps)}, eps = {eps}")
