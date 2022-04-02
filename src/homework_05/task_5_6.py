# Task 5.6
# shlom41k

"""
Задан целочисленный массив.
Определить количество участков массива, на котором элементы монотонно возрастают
(каждое следующее число больше предыдущего).
"""


import random


n = 10  # List range

rand_list = [random.randint(-100, 100) for _ in range(n)]

cnt = 0
fl = False

for i in range(1, len(rand_list)):
    if rand_list[i] > rand_list[i - 1]:
        fl = True
    else:
        if fl:
            cnt += 1
            fl = False
else:
    if fl:
        cnt += 1

print("Исходный массив:\n", rand_list)
print("Количество возрастающих участков:", cnt)