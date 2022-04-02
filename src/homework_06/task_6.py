# Task 6
# shlom41k


from random import randint


# Get input data
# Matrix elements range
# a = int(input("Введите нижнюю границу [a]: "))
# b = int(input("Введите верхнюю границу [b]: "))

# Matrix size [n x m]
# n = int(input("Введите количество строк матрицы [n]: "))
# m = int(input("Введите количество столбцов матрицы [m]: "))

a, b = -10, 10
n, m, = 4, 4

matrix = list()     # Matrix

# 6.1) Generate matrix elements
for _ in range(n):
    matrix.append([randint(a, b) for _ in range(m)])

# Print matrix
print("\n1) Исходная матрица:")
[print(*(matrix[i]), sep="\t\t", end="\n") for i in range(n)]

# 6.2) Search MAX element:
max_mtx = max(matrix[0])

for i in range(n):
    if max(matrix[i]) > max_mtx:
        max_mtx = max(matrix[i])

print(f"\n2) Максимальный элемент матрицы: {max_mtx}")
# or
# print(f"Максимальный элемент матрицы: {max([max(matrix[i]) for i in range(n)])}")

# 6.3) Search MIN element:
min_mtx = min(matrix[0])

for i in range(n):
    if min(matrix[i]) < max_mtx:
        min_mtx = min(matrix[i])

print(f"3) Минимальный элемент матрицы: {min_mtx}")
# or
# print(f"Минимальный элемент матрицы: {min([min(matrix[i]) for i in range(n)])}")

# 6.4) Search SUM of element:
total = 0
for i in range(n):
    total += sum(matrix[i])

print(f"4) Сумма всех элементов матрицы: {total}")
# or
# print(f"Сумма всех элементов матрицы: {sum([sum(matrix[i]) for i in range(n)])}")

# 6.5) Search ROW with MAX SUM of elements:
max_row = sum(matrix[0])
max_row_ind = 0
for i in range(n):
    if sum(matrix[i]) > max_row:
        max_row = sum(matrix[i])
        max_row_ind = i

print(f"5) Индекс ряда с максимальной суммой элементов: {max_row_ind}")

# 6.6) Search COL with MAX SUM of elements:
max_col_sum, max_col_ind = 0, 0

for j in range(m):
    s = 0
    for i in range(n):
        s += matrix[i][j]
    if s > max_col_sum:
        max_col_sum = s
        max_col_ind = j

print(f"6) Индекс столбца с максимальной суммой элементов: {max_col_ind}")

# 6.7) Search ROW with MIN SUM of elements:
min_row = sum(matrix[0])
min_row_ind = 0
for i in range(n):
    if sum(matrix[i]) < min_row:
        min_row = sum(matrix[i])
        min_row_ind = i

print(f"7) Индекс ряда с минимальной суммой элементов: {min_row_ind}")

# 6.8) Search COL with MIN SUM of elements:
min_col_sum, min_col_ind = 0, 0

for j in range(m):
    s = 0
    for i in range(n):
        s += matrix[i][j]
    if s < min_col_sum:
        min_col_sum = s
        min_col_ind = j

print(f"8) Индекс столбца с минимальной суммой элементов: {min_col_ind}")

# 6.9) Set to zero upper elements:
for i in range(n):
    for j in range(m):
        if j > i:
            matrix[i][j] = 0

print("9) Измененная матрица:")
[print(*matrix[i], sep="\t\t", end="\n") for i in range(n)]

# 6.10) Set to zero lower elements:
for i in range(n):
    for j in range(m):
        if j < i:
            matrix[i][j] = 0

print("\n10) Измененная матрица:")
[print(*matrix[i], sep="\t\t", end="\n") for i in range(n)]

# 6.11) Generate matrix_a and matrix_b elements:
matrix_a, matrix_b = [], []

for _ in range(n):
    matrix_a.append([randint(a, b) for _ in range(m)])
    matrix_b.append([randint(a, b) for _ in range(m)])

# Print matrix
print("\n11) Исходная матрица A:")
[print(*matrix_a[i], sep="\t\t", end="\n") for i in range(n)]

print("\nИсходная матрица B:")
[print(*matrix_b[i], sep="\t\t", end="\n") for i in range(n)]

# 6.12) Generate matrix_sum:
matrix_sum = [[] for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix_sum[i].append(matrix_a[i][j] + matrix_b[i][j])

print("\nРезультирующая матрица (сложение matrix_a + matrix_b):")
[print(*matrix_sum[i], sep="\t\t", end="\n") for i in range(n)]

# 6.13) Generate matrix_sum:
matrix_diff = [[] for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix_diff[i].append(matrix_a[i][j] - matrix_b[i][j])

print("\nРезультирующая матрица (вычитание matrix_a - matrix_b):")
[print(*matrix_diff[i], sep="\t\t", end="\n") for i in range(n)]

# 6.15) Generate matrix_mult:
matrix_mult = [[] for _ in range(n)]
# g = int(input("Введите множитель для matrix_a [g]: "))
g = 4

for i in range(n):
    for j in range(m):
        matrix_mult[i].append(matrix_a[i][j] * g)

print("\nРезультирующая матрица (умножение matrix_a * g):")
[print(*matrix_mult[i], sep="\t\t", end="\n") for i in range(n)]