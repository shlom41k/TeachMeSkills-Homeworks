"""
# Task 14.01
# shlom41k
# classwork
"""

from random import randint
from time import  sleep


def random_generator():
    while True:
        yield randint(-100, 100)
        sleep(1)


r_gen = random_generator()
for el in r_gen:
    print(el)