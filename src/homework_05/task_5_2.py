# Task 5.2
# shlom41k

"""
-> Дано число. Найти сумму и произведение его цифр
"""

num = 50005

# Using str
s = 0
p = 1

for n in str(num):
    s += int(n)
    p *= int(n)

print(f"Сумма цифр числа {num} равна {s}")
print(f"Произведение цифр числа {num} равно {p}\n")

# Without str
s = 0
p = 1

while num:
    last_digit = num % 10   # Get last digit
    s += last_digit
    p *= last_digit
    num = num // 10     # Delete last digit

print(f"Сумма цифр числа равна {s}")
print(f"Произведение цифр числа равно {p}")