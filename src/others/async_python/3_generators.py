from time import time, sleep


def gen(s):
    for i in s:
        yield i


def gen_filename():
    while True:
        pattern = "file-{}.jpeg"
        t = int(time() * 1000)
        yield pattern.format(str(t))
        print(2 + 8)


def gen2():
    yield 1
    yield 2
    yield 3


# g = gen("sergey")
# g_time = gen_filename()
#
# print(next(g_time))
# print(next(g_time))
#
# g2 = gen2()
#
# print(next(g2))
# print(next(g2))
# print(next(g2))

# Генераторы - функции!
# Передача контроля выполнения программы

# Событийный цикл RoundRobbin

def gen1(s):
    for i in s:
        yield i


def gen2(n):
    for i in range(n):
        yield i


g1 = gen1("shlom41k")
g2 = gen2(4)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        print("Pass")

