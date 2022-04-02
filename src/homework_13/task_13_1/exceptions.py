"""
# Task 13.1
# shlom41k
"""


class MyZeroDivision(Exception):
    def __init__(self, message: str):
        # print("ERROR! Division by zero!")
        super().__init__(message)


class MyNumException(Exception):
    def __init__(self, message: str):
        # print("ERROR! Invalid input data!")
        super().__init__(message)


class MyActionException(Exception):
    def __init__(self, message: str):
        # print("ERROR! Invalid operator!")
        super().__init__(message)