# shlom41k
"""
# Some tests for classes. Classes and dataclasses
"""

from dataclasses import dataclass


class RegularBook:
    def __init__(self, title, author):
        self.title = title
        self.author = author


@dataclass(frozen=True)
class Book:
    title: str
    author: str


b1 = RegularBook("War and Peace", "Tolstoy")
print(b1)

b2 = Book("War and Peace", "Tolstoy")
print(b2)
