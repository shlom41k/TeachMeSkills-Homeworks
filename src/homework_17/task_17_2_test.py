# shom41k
# tests for homework 17.2


import unittest
from task_17_2 import WrongInputError, validate_args, Math


class ValidTest(unittest.TestCase):
    def test_validator(self):
        self.assertIsNone(validate_args(1, 1))
        self.assertIsNone(validate_args(-1, 1))
        self.assertIsNone(validate_args(0, -1))
        self.assertIsNone(validate_args(0.10, -1.1))
        self.assertIsNone(validate_args(0.0, -0.0))
        self.assertIsNone(validate_args(False, True))   # False == 0, True == 1 - исключения нет

        self.assertRaises(WrongInputError, validate_args, x="a", y=1)
        self.assertRaises(WrongInputError, validate_args, x="a", y=-2.0)
        # self.assertRaises(WrongInputError, validate_args, x=True, y=-5)   # Воспринимает True как 1
        self.assertRaises(WrongInputError, validate_args, x=[], y=-2.0)
        self.assertRaises(WrongInputError, validate_args, x=[11, 22], y=-2.0)
        self.assertRaises(WrongInputError, validate_args, x="", y="-2.0")
        self.assertRaises(WrongInputError, validate_args, x=" ", y="")
        self.assertRaises(WrongInputError, validate_args, x=(1), y=(1, 3))
        self.assertRaises(WrongInputError, validate_args, x={1: "sd"}, y=None)
        self.assertRaises(WrongInputError, validate_args, x=None, y=None)
        self.assertRaises(WrongInputError, validate_args, x=2, y=None)
        self.assertRaises(WrongInputError, validate_args, x=-8.0, y="+")

    def testInsufficientArgs(self):
        self.assertIsNotNone(Math(x=0, y=1))
        self.assertIsNotNone(Math(x=-2, y=1.0))
        self.assertIsNotNone(Math(x=-0, y=0.0))
        self.assertIsNotNone(Math(x=-5, y=0.0))

        self.assertRaises(WrongInputError, Math, x=0, y="a")
        self.assertRaises(WrongInputError, Math, x="a", y="a")
        self.assertRaises(WrongInputError, Math, x=[], y="a")
        self.assertRaises(WrongInputError, Math, x=[], y=[])
        self.assertRaises(WrongInputError, Math, x=2.5, y=None)
        self.assertRaises(WrongInputError, Math, x=None, y=-5)

    def setUp(self):
        self.calc0 = Math(x=1, y=1)
        self.calc1 = Math(x=0, y=1.0)
        self.calc2 = Math(x=0, y=0)
        self.calc3 = Math(x=0, y=5)
        self.calc4 = Math(x=2.0, y=4)

    def test_sum(self):
        self.assertEqual(self.calc0.calc_sum(), 2)
        self.assertEqual(self.calc1.calc_sum(), 1.0)
        self.assertEqual(self.calc2.calc_sum(), 0)
        self.assertEqual(self.calc3.calc_sum(), 5)
        self.assertEqual(self.calc4.calc_sum(), 6.0)

    def test_diff(self):
        self.assertEqual(self.calc0.calc_diff(), 0)
        self.assertEqual(self.calc1.calc_diff(), -1.0)
        self.assertEqual(self.calc2.calc_diff(), 0)
        self.assertEqual(self.calc3.calc_diff(), -5)
        self.assertEqual(self.calc4.calc_diff(), -2.0)

    def test_mult(self):
        self.assertEqual(self.calc0.calc_mult(), 1)
        self.assertEqual(self.calc1.calc_mult(), 0.0)
        self.assertEqual(self.calc2.calc_mult(), 0)
        self.assertEqual(self.calc3.calc_mult(), 0)
        self.assertEqual(self.calc4.calc_mult(), 8.0)

    def test_div(self):
        self.assertEqual(self.calc0.calc_div(), 1)
        self.assertEqual(self.calc1.calc_div(), 0.0)
        # self.assertRaises(self.calc2.calc_div(), ZeroDivisionError)
        self.assertEqual(self.calc3.calc_div(), 0)
        self.assertEqual(self.calc4.calc_div(), 0.5)


if __name__ == '__main__':
    unittest.main()