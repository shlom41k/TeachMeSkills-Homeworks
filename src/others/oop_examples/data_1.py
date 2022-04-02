# shlom41k
"""
# Some tests for classes. Private attributes
"""

# self.name     <- public
# self._name    <- private
# self.__name   <- protected


class Book:
    def __init__(self, title: str, author:str):
        self._title = title
        self._author = author

    def __repr__(self):
        return f"Title='{self._title}', author='{self._author}'"


if __name__ == "__main__":

    book1 = Book("Mu-Mu", "Turgenev")
    print(book1)
    print("Title:", book1._title)
    print("Author:", book1._author, "\n")

    book1._title = "mu"
    book1._author = "Tur"
    print(book1)