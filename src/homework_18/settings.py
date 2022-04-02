# -*- coding: utf-8 -*-

# homework 18
# shlom41k

"""
# Module with global settings and constants
"""


import os


HOST = "http://127.0.0.1"
PORT = 5000

LOCALHOST = HOST + ":" + str(PORT)
URL_PRODUCT = "/product/"
URL_EDIT_PRODUCT = "/edit/"
URL_DELETE_PRODUCT ="/delete/"
URL_ADD_PRODUCT = "/add/"

BASEDIR = os.path.abspath(os.path.dirname(__file__))

DATABASE_URI = "sqlite:///data.db"

if __name__ == "__main__":
    print(BASEDIR)

