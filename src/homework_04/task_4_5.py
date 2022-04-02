# Task 4.5
# shlom41k

"""
Составить список чисел Фибоначчи содержащий 15 элементов
"""


n = 15  # Fibonacci length


# Use while
fib_list = [1, 1]
i = 1       # Loops counter

while len(fib_list) < n:
    fib_list.append(sum(fib_list[-2:]))
    i += 1

print("\nFibonacci (use while):\n", fib_list)


# Use for
fib_list2 = [1, 1]

for i in range(n - 2):
    fib_list2.append(sum(fib_list2[-2:]))

print("\nFibonacci (use for:)\n", fib_list2)