# Task 9.2
# shlom41k

"""
Создать lambda функцию, которая принимает на вход неопределенное количество именных аргументов
и выводит словарь с ключами удвоенной длины: {‘abc’: 5} --> {‘abcabc’: 5}.
"""


f = lambda **kwargs: {key * 2: value for key, value in kwargs.items()}


if __name__ == "__main__":

    # Test
    print(f(one=1, two=2, three=3))
    print(f(x="a", y="b"))
    print(f(abc=5, xyz=4, ijk=1, lmn=10))
    print(f(w=3))