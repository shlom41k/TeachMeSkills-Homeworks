# Task 5.7
# shlom41k

"""
Дана целочисленная квадратная матрица.
Найти в каждой строке наибольший элемент и поменять его местами с элементом главной диагонали.
"""


import random


n = 5       # Matrix size

a = list()  # Matrix

# Generate matrix elements
for _ in range(n):
    a.append([random.randint(-10, 10) for _ in range(n)])

# Print matrix
print("\nИсходная матрица:")
[print(*a[i], sep="\t\t", end="\n") for i in range(n)]

# Change matrix
for i in range(n):
    max_el = a[i].index(max(a[i]))
    a[i][i], a[i][max_el] = a[i][max_el], a[i][i]

# Print matrix
print("\nРезультирующая матрица:")
[print(*a[i], sep="\t\t", end="\n") for i in range(n)]