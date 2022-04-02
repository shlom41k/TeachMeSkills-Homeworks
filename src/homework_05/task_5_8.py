# Task 5.8
# shlom41k

"""
В заданной строке расположить в обратном порядке все слова.
Разделителями слов считаются пробелы.
"""

# 1) Get string from console
# 2) Split string (sep=" ")
# 3) Reverse list of words
# 4) Join reversed list into a string (sep=" ")

s = " ".join(input().split()[::-1])

print(s)