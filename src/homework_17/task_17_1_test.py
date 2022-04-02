# shom41k
# tests for homework 17.1

import unittest

from task_17_1 import calc_sum, calc_diff, calc_mult, calc_div


class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc_sum(2, 2), 4)
        self.assertEqual(calc_sum(0, 2), 2)
        self.assertEqual(calc_sum(-1, 5), 4)
        self.assertEqual(calc_sum(0, 1), 1)
        self.assertEqual(calc_sum("1", "1"), "11")  # Херня, а работает
        self.assertEqual(calc_sum([], [1]), [1])    # Херня, а работает

        self.assertRaises(TypeError, calc_sum, a=[], b=-2.0)
        self.assertRaises(TypeError, calc_sum, a="1", b=-2)
        self.assertRaises(TypeError, calc_sum, a=None, b=1.5)
        self.assertRaises(TypeError, calc_sum, a="None", b=None)

    def test_diff(self):
        self.assertEqual(calc_diff(0, 1), -1)
        self.assertEqual(calc_diff(10, 9), 1)
        self.assertEqual(calc_diff(0, 0), 0)

        self.assertRaises(TypeError, calc_diff, a=[], b=-3.0)
        self.assertRaises(TypeError, calc_diff, a="11", b=-2)
        self.assertRaises(TypeError, calc_diff, a=None, b=1.5)
        self.assertRaises(TypeError, calc_diff, a="None", b=None)
        self.assertRaises(TypeError, calc_diff, a="123", b="12")

    def test_mult(self):
        self.assertEqual(calc_mult(1, 3), 3)
        self.assertEqual(calc_mult(0, 3), 0)
        self.assertEqual(calc_mult(3, 0), 0)
        self.assertEqual(calc_mult(0, 0), 0)
        self.assertEqual(calc_mult(-1, 0), 0)
        self.assertEqual(calc_mult(-1, -5), 5)
        self.assertEqual(calc_mult(-1, 7), -7)
        self.assertEqual(calc_mult("a", 2), "aa")   # Херня, а работает

        self.assertRaises(TypeError, calc_mult, a=[1], b=-3.0)
        self.assertRaises(TypeError, calc_mult, a=None, b=-4)
        self.assertRaises(TypeError, calc_mult, a="None", b=None)
        self.assertRaises(TypeError, calc_mult, a="123", b="12")

    def test_div(self):
        self.assertEqual(calc_div(9, 1), 9)
        self.assertEqual(calc_div(9, 2), 4.5)
        self.assertEqual(calc_div(0, 2), 0)
        self.assertEqual(calc_div(0, -2), 0)

        self.assertRaises(ZeroDivisionError, calc_div, a=3, b=0)
        self.assertRaises(ZeroDivisionError, calc_div, a=0, b=0)

        self.assertRaises(TypeError, calc_div, a=[1, 0], b="-3.0")
        self.assertRaises(TypeError, calc_div, a=None, b=-4)
        self.assertRaises(TypeError, calc_div, a="None", b=None)
        self.assertRaises(TypeError, calc_div, a="123", b="12")
        self.assertRaises(TypeError, calc_div, a="123", b=3)
        self.assertRaises(TypeError, calc_div, a="123", b=0)


if __name__ == "__main__":
    unittest.main()

