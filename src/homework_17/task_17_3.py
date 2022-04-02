# shom41k
# homework 17.3


from datetime import datetime


class BookError(Exception):
    def __init__(self, message='Ошибка ввода данных для книги'):
        super().__init__(message)


class WrongPagesTypeError(BookError):
    def __init__(self, message='Неверный тип страниц. Ожидается int'):
        super().__init__(message)


class WrongPagesAmountError(BookError):
    def __init__(self, message='Количество страниц должно быть положительным числом'):
        super().__init__(message)


class WrongYearTypeError(BookError):
    def __init__(self, message='Год должен быть целым числом'):
        super().__init__(message)


class FutureBookError(BookError):
    def __init__(self, message='Год не может быть больше текущего'):
        super().__init__(message)


class WrongAuthorTypeError(BookError):
    def __init__(self, message='Имя автора должно быть строкой'):
        super().__init__(message)


class ZeroLengthAuthorError(BookError):
    def __init__(self, message='Имя автора не должно быть пустой строкой'):
        super().__init__(message)


class WrongPriceTypeError(BookError):
    def __init__(self, message='Цена должна быть числом'):
        super().__init__(message)


class WrongPriceValueError(BookError):
    def __init__(self, message='Цена не может быть отрецательной'):
        super().__init__(message)


def validate_pages(pages):
    if not isinstance(pages, int):
        raise WrongPagesTypeError
    elif pages < 1:
        raise WrongPagesAmountError


def validate_year(year):
    if not isinstance(year, int):
        raise WrongYearTypeError
    elif year > datetime.now().year:
        raise FutureBookError


def validate_author(author):
    if not isinstance(author, str):
        raise WrongAuthorTypeError
    elif not author:
        raise ZeroLengthAuthorError


def validate_price(price):
    if not (isinstance(price, (int, float))):
        raise WrongPriceTypeError
    elif price < 0:
        raise WrongPriceValueError


if __name__ == '__main__':
    pass