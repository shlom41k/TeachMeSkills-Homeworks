"""
# Task 14.05
# shlom41k
# classwork
"""

import argparse
import os

parser = argparse.ArgumentParser(description="Task 14.05")

parser.add_argument("folder", type=str)
args = parser.parse_args()

print(args.folder)

os.mkdir(args.folder)

