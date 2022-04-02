# Task 8.2
# shlom41k

"""
Даны слова. Выяснить, является ли хоть одно из них палиндромом. 
(Определить функцию, позволяющую распознавать слова палиндромы.)
"""


# Проверяем слово
def is_word_polyndrom(word):
    return True if word.lower() == word.lower()[::-1] else False


# Проверяем строку
def is_str_polyndrom(s):
    s = s.replace(" ", "")
    return True if s.lower() == s.lower()[::-1] else False


if __name__ == '__main__':

    # Test
    words = ["lol", "топот", "lolli", "powop", "student"]
    s = "А роза упала на лапу Азора"

    [print(f"{i}) '{word}' {'is poly' if is_word_polyndrom(word) else 'is not poly'}") for i, word in enumerate(words, 1)]
    print(f"\n-> '{s}' {'is poly string' if is_str_polyndrom(s) else 'is not poly string'}")
