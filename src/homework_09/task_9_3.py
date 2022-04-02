# Task 9.3
# shlom41k

"""
Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных - удалять все четные элементы из списка.
"""

from random import randint


def my_decorator(my_func):
    # print('Входим в декоратор')
    def wrapper(lst):
        # print('Входим в функцию-обёртку')
        # print('Выполняем предварительную фильтрацию данных - удаляем четные элементы')
        new_lst = [elem for elem in lst if elem % 2]
        # print('Выполняем обёрнутую функцию...')
        my_func(new_lst)
        # print('Выходим из обёртки')
    # print('Выходим из декоратора')
    return wrapper


@my_decorator
# Исходная функция тупо выводит список в консоль
def print_list(lst: list):
    print(lst)


if __name__ == "__main__":

    # Test

    # Исходный список
    my_list = [randint(-100, 100) for _ in range(20)]
    print(my_list)

    # Результат выполнения обернутой функции
    print_list(my_list)







