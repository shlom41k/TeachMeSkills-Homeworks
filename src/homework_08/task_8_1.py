# Task 8.1
# shlom41k

"""
Описать функцию fact2(n), вычисляющую двойной факториал:
n!! = 1·3·5·...·n, если n — нечетное;
n!! = 2·4·6·...·n, если n — четное
(n > 0 — параметр целого типа).
С помощью этой функции найти двойные факториалы пяти данных целых чисел.
"""

from random import randint


# Через рекурсию
def fact2_rec(n):
    if n <= 0:
        return 1
    return fact2_rec(n - 2) * n


# Через цикл
def fact2(n):
    fact = 1
    if n % 2:
        for i in range(1, n + 1, 2):
            fact *= i
    else:
        for i in range(2, n + 1, 2):
            fact *= i
    return fact


if __name__ == '__main__':

    # Test
    nums = [randint(1, 20) for _ in range(5)]
    [print(f"Number: {n}, factorial: for (func) --> {fact2(n)} ({fact2_rec(n)})") for n in nums]




