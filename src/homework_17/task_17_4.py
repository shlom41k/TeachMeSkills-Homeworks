# shom41k
# homework 17.4


from random import randint


class Matrix:
    def __init__(self, *args):
        if len(args) == 4:
            self.n, self.m, a, b = args
            self.data = [[randint(a, b) for i in range(self.n)] for j in range(self.m)]
        elif len(args) == 1 and isinstance(args[0], Matrix):
            source_matrix = args[0]
            self.n = source_matrix.n
            self.m = source_matrix.m
            self.data = source_matrix.data
        else:
            self.n = 5
            self.m = 5
            self.data = [[0 for i in range(self.n)] for j in range(self.m)]

    def __str__(self):
        result_line = ""
        for i, line in enumerate(self.data):
            str_line = ' '.join(map(str, line))
            result_line += f'{str_line}\n'
        return result_line


def matrix_max_elem(matrix):
    max_elem = matrix.data[0][0]
    for i, row in enumerate(matrix.data):
        for j, elem in enumerate(row):
            if elem > max_elem:
                max_elem = elem
    return max_elem


def matrix_min_elem(matrix):
    min_elem = matrix.data[0][0]
    for i, row in enumerate(matrix.data):
        for j, elem in enumerate(row):
            if elem < min_elem:
                min_elem = elem
    return min_elem


def matrix_sum(matrix):
    summ = 0
    for line in matrix.data:
        for elem in line:
            summ += elem
    return summ