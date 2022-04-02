# shlom41k
"""
# Some tests for classes. Protected attributes
"""


class Book:
    def __init__(self, title: str, author:str):
        self.__title = title
        self.__author = author

    def __repr__(self):
        return f"Title='{self.__title}', author='{self.__author}'"


if __name__ == "__main__":

    book1 = Book("Mu-Mu", "Turgenev")
    print(book1, "\n")

    # print("Title:", book1.__title)
    # print("Author:", book1.__author)

    book1.__title = "mu"
    book1.__author = "Tur"

    print("Title:", book1.__title)
    print("Author:", book1.__author)
    print(book1, "\n")                      # No changes!


    print("Title:", book1._Book__title)
    print("Author:", book1._Book__author)

    book1._Book__title = "mu"
    book1._Book__author = "Tur"

    print(book1)                            # Changed!