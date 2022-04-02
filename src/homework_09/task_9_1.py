# Task 9.1
# shlom41k

"""
Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’,
где i - это порядковый номер строки в списке. Использовать генератор списков.
"""

my_strs = ["Hello, shlom41k",
           "This ia string",
           "and one more string",
           "this is a 4'th string",
           "33333333333333",
           "London is the capital of Great Britan",
           ]

[print(f"{ind} - {s}")for ind, s in enumerate(my_strs, 1)]