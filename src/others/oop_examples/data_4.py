# shlom41k
"""
# Some tests for classes. Getters and setters
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

    @property
    def pages(self):
        # return number of pages

        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        # set attribute '__pages'

        if self.is_valid_pages(pages):
            self.__pages = pages

    @staticmethod
    def is_valid_pages(pages: int):
        # validation of parameter 'pages'

        if not isinstance(pages, int):
            print("ERROR: Expected <int> type!")
            return False
        if pages <= 0:
            print("ERROR: Parameter must be positive > 0")
            return False
        return True


if __name__ == "__main__":

    book1 = Book("Mu-Mu", "Turgenev", 35)

    print(book1)
    print("Title:", book1.title)                        # No problem
    print("Author:", book1._author)                     # Warning
    # print("Number of pages:", book1.__pages)          # Error!
    # print("Number of pages:", book1._Book__pages)          # Error!
    print("Number of pages:", book1.pages, "\n")        # No problem

    book1.title = "mu"          # Change attribute
    book1._author = "Tur"       # Change attribute
    book1.__pages = 0           # No changes (create a local variable)
    print(book1, "\n")

    print("Number of pages:", book1._Book__pages)
    book1._Book__pages = 0
    print(book1, "\n")

    print("Valid" if Book.is_valid_pages(pages=4) else "Invalid")
    print("Valid" if Book.is_valid_pages(pages=4.5) else "Invalid")
    print("Valid" if Book.is_valid_pages(pages=-22) else "Invalid")

    book1.pages = 22.1
    print(book1, "\n")

    book1.pages = -1
    print(book1, "\n")

    book1.pages = 15
    print(book1, "\n")




