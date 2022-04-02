# shom41k
# tests for homework 17.3


import unittest
from task_17_3 import *


class ValidateTest(unittest.TestCase):
    def test_pages_validator(self):
        self.assertIsNone(validate_pages(pages=1))
        self.assertIsNone(validate_pages(pages=5))

        # self.assertRaises(WrongPagesTypeError, validate_pages, pages=True)    # проходит
        # self.assertRaises(WrongPagesTypeError, validate_pages, pages=(1))     # проходит

        pages_err = [1.0, -1.0, [4], "2", {1: 1}, [], "", None, tuple()]

        for page in pages_err:
            self.assertRaises(WrongPagesTypeError, validate_pages, pages=page)

        self.assertRaises(WrongPagesAmountError, validate_pages, pages=0)
        self.assertRaises(WrongPagesAmountError, validate_pages, pages=-11)

    def test_year_validator(self):
        self.assertIsNone(validate_year(year=1999))
        self.assertIsNone(validate_year(year=2021))
        self.assertIsNone(validate_year(year=0))
        self.assertIsNone(validate_year(year=-2000))

        years_err = [1999.25, -1999.25, [2002], [], "1998", "-0", "", {"year": 1998}, {}, None]
        for year in years_err:
            self.assertRaises(WrongYearTypeError, validate_year, year=year)

        # self.assertRaises(WrongYearTypeError, validate_year, year=True)   # проходит
        # self.assertRaises(WrongYearTypeError, validate_year, year=False)  # проходит

        self.assertRaises(FutureBookError, validate_year, year=2054)
        self.assertRaises(FutureBookError, validate_year, year=2099)

    def test_author_validator(self):
        self.assertIsNone(validate_author(author="Ivanov"))
        self.assertIsNone(validate_author(author="2002"))
        self.assertIsNone(validate_author(author="exit"))
        self.assertIsNone(validate_author(author=" "))

        authors_err = [123, -123, 0, ["Ivamov"], [], [""], {"author": "Ivanov"}, {"": ""}, None, True, False, tuple()]
        for author in authors_err:
            self.assertRaises(WrongAuthorTypeError, validate_author, author=author)

        self.assertRaises(ZeroLengthAuthorError, validate_author, author="")

    def test_price_validator(self):
        self.assertIsNone(validate_price(price=198))
        self.assertIsNone(validate_price(price=225.2))
        self.assertIsNone(validate_price(price=0.2))
        self.assertIsNone(validate_price(price=0.0))

        prices_err = [[123], ["123123"], [""], [], "1258", "", "None", None, {"price": 1}, {1.20: 1}, tuple()]

        # self.assertRaises(WrongPriceTypeError, validate_price, price=True)    # проходит
        # self.assertRaises(WrongPriceTypeError, validate_price, price=False)   # проходит

        self.assertRaises(WrongPriceValueError, validate_price, price=-2)
        self.assertRaises(WrongPriceValueError, validate_price, price=-1.0)
        self.assertRaises(WrongPriceValueError, validate_price, price=-0.1)


if __name__ == '__main__':
    unittest.main()