"""
# Task 14.02
# shlom41k
# classwork
"""

from random import randint
from time import  sleep


def random_generator(a: int, b: int, diff: int):
    k = 0
    while True:
        yield randint(a + k, b + k)
        sleep(1)
        k += diff


r_gen = random_generator(a=1, b=10, diff=10)
for el in r_gen:
    print(el)