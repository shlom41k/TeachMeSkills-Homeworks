"""
# Task 14.06
# shlom41k
# classwork
"""

import argparse
import os

parser = argparse.ArgumentParser(description="Task 14.06")

parser.add_argument("folder_name", type=str)
parser.add_argument("file_name", type=str)
args = parser.parse_args()

print(args.folder_name, args.file_name)

folder_name = args.folder_name
file_name = args.file_name

os.mkdir(folder_name)
with open(f"{folder_name}/{file_name}", encoding="utf-8", mode="a") as f:
    pass

print("Script finish successfully")

