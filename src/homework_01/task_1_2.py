# Task 1.2
# shlom41k

"""
Даны действительные числа x и y. Получить (|x| −|y|)/(1 + |xy|).
"""

from math import fabs


x, y = 3, -5

res = (fabs(x) - fabs(y)) / (1 + fabs(x * y))

print(res)

