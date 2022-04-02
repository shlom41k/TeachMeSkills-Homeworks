# shlom41k
"""
# Some tests for classes. All attributes
"""


class Book:
    """
    # self.title        <- public
    # self._author      <- private
    # self.__pages      <- protected
    """

    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self._author = author
        self.__pages = pages

    def __repr__(self):
        return f"Title='{self.title}', author='{self._author}', pages='{self.__pages}'"


if __name__ == "__main__":

    book1 = Book("Mu-Mu", "Turgenev", 35)

    print(book1)                                    # Title='Mu-Mu', author='Turgenev', pages='35'
    print("Title:", book1.title)                    # Title: Mu-Mu  - No problem
    print("Author:", book1._author, "\n")           # Author: Turgenev - Warning
    # print("Number of pages:", book1.__pages)      # Error!

    book1.title = "mu"          # Change attribute
    book1._author = "Tur"       # Change attribute
    book1.__pages = 0           # No changes (create a local variable)
    print(book1, "\n")          # Title='mu', author='Tur', pages='35'

    print("Number of pages:", book1._Book__pages)   # Number of pages: 35
    book1._Book__pages = 0      # Change attribute
    print(book1, "\n")          # Title='mu', author='Tur', pages='0'




