"""
# Task 13.2
# shlom41k
"""

from exceptions import *


class Calculator:
    __a: float
    __b: float
    __res: float

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def res(self):
        return self.__res

    @a.setter
    def a(self, a):
        self.__a = a

    @b.setter
    def b(self, b):
        self.__b = b

    def my_add(self):
        self.__res = self.__a + self.__b

    def my_sub(self):
        self.__res = self.__a - self.__b

    def my_mult(self):
        self.__res = self.__a * self.__b

    def my_div(self):
        self.__res = self.__a / self.__b

    @staticmethod
    def is_num_valid(n: str) -> bool:
        if n.isdigit() or (n[0] == "-" and n[1:].isdigit()) or \
                (n.count(".") < 2 and (n.replace(".", "")).count(".") == 0):
            return True
        else:
            return False

    @staticmethod
    def is_oper_valid(op: str) -> bool:
        return True if op in "+-*/0" else False

    @staticmethod
    def get_operation():
        while True:
            print("Выберите любую из доступных операций:")
            print("[+] Cложение\n"
                  "[-] Вычитание\n"
                  "[*] Умножение\n"
                  "[/] Деление\n"
                  "[0] Выход из программы")
            op = input("Желаемая операция: ")

            if Calculator.is_oper_valid(op):
                break
            else:
                raise MyActionException("Error! invalid operator!")
        return op

    def get_result(self, op):
        if op == "+":
            self.my_add()
            return f"{self.__a} + {self.__b} = {self.__res}\n"
        elif op == "-":
            self.my_sub()
            return f"{self.__a} - {self.__b} = {self.__res}\n"
        elif op == "*":
            self.my_mult()
            return f"{self.__a} * {self.__b} = {self.__res}\n"
        elif op == "/":
            if self.b == 0:
                raise MyZeroDivision("Error! Division by zero!")
            else:
                self.my_div()
                return f"{self.__a} / {self.__b} = {self.__res}\n"

    def start(self):
        while True:
            op = Calculator.get_operation()

            if op == "0":
                print("Выход из программы")
                break

            a = input("Введите число а: ")
            b = input("Введите число b: ")

            if not self.is_num_valid(a) or not self.is_num_valid(b):
                raise MyNumException("Error! Invalid input arguments!")
            else:
                self.__a, self.__b = float(a), float(b)

            print(self.get_result(op))