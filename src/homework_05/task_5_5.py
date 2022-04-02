# Task 5.5
# shlom41k

"""
В массиве целых чисел с количеством элементов 19 определить максимальное число
и заменить им все четные по значению элементы.
"""


import random


n = 19  # List range

rand_list = [random.randint(-100, 100) for _ in range(n)]

print("Исходный массив:\n", rand_list)
print("Наибольний элемент массива:", max(rand_list))

for i in range(0, len(rand_list)):
    if rand_list[i] % 2 == 0:
        rand_list[i] = max(rand_list)

print("Измененный массив:\n", rand_list)