# shom41k
# tests for homework 17.3


import unittest
from task_17_4 import matrix_max_elem, matrix_min_elem, matrix_sum, Matrix


class ValidateTest(unittest.TestCase):
    def test_matrix_max_elem(self):

        # n, m, a, b
        # n - число строк, m - столбцов

        tests = [
            (3, 3, -10, 10),
            (5, 5, -100, 100),
            (1, 4, 0, 10),
            (3, 1, 0, 1),
            (),
            (1, 1, -10, 10),
            (2, 2, -100, 100),
            (3, 3, 1, 1),
        ]

        for test in tests:
            self.matrix = Matrix(*test)
            print(self.matrix, matrix_max_elem(self.matrix), matrix_min_elem(self.matrix), matrix_sum(self.matrix),
                  sep=" | ", end="\n\n")

            self.assertEqual(matrix_max_elem(self.matrix), max([max(self.matrix.data[i]) for i in range(self.matrix.m)]))
            self.assertEqual(matrix_min_elem(self.matrix), min([min(self.matrix.data[i]) for i in range(self.matrix.m)]))
            self.assertEqual(matrix_sum(self.matrix), sum([sum(self.matrix.data[i]) for i in range(self.matrix.m)]))


if __name__ == '__main__':
    unittest.main()