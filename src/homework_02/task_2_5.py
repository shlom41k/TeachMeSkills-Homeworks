# Task 2.5
# shlom41k

"""
Создать строку, равную всем элементам введенной строки с четными индексами
(считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого, индексы 0,2,4,6... .)
"""


# Read string from console
s = input()

# New string
s_new = s[::2]

print("Input string:", s)
print("New string:", s_new)