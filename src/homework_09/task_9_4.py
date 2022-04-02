# Task 9.4
# shlom41k

"""
Создать универсальный декоратор, который меняет порядок аргументов в функции на противоположный
"""


def my_decorator(my_func):
    def wrapper(*args):
        my_func(args[::-1])     # Меняем порядок аргументов
    return wrapper


@my_decorator
def print_args(*args):
    # Тупо выводим аргументы
    [print(*arg, sep=" ") for arg in args]


if __name__ == "__main__":

    # Test

    # Исходные данные
    args = ("first", 1, [4], 6, 8, {1: True}, "a", "last")
    print(*args)

    # Результат выполнения обернутой функции
    print_args(*args)







