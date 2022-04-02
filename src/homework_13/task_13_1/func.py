"""
# Task 13.1
# shlom41k
"""


from exceptions import *


# Functions
def my_add(a, b):
    return a + b


def my_sub(a, b):
    return a - b


def my_mult(a, b):
    return a * b


def my_div(a, b):
    return a / b


def is_num_valid(n: str) -> bool:
    if n.isdigit() or (n[0] == "-" and n[1:].isdigit()) or (n.count(".") < 2 and (n.replace(".", "")).count(".") == 0):
        return True
    else:
        return False


def is_oper_valid(op: str) -> bool:
    return True if op in "+-*/0" else False


def get_operation():
    while True:
        print("Выберите любую из доступных операций:")
        print("[+] Cложение\n"
              "[-] Вычитание\n"
              "[*] Умножение\n"
              "[/] Деление\n"
              "[0] Выход из программы")
        op = input("Желаемая операция: ")

        if is_oper_valid(op):
            break
        else:
            raise MyActionException("Error! invalid operator!")

    return op


def get_result(a, b, op):
    if op == "+":
        print(f"{a} + {b} = {my_add(a, b)}\n")
    elif op == "-":
        print(f"{a} - {b} = {my_sub(a, b)}\n")
    elif op == "*":
        print(f"{a} * {b} = {my_mult(a, b)}\n")
    elif op == "/":
        if b == 0:
            raise MyZeroDivision("Error! Division by zero!")
        else:
            print(f"{a} / {b} = {my_div(a, b)}\n")