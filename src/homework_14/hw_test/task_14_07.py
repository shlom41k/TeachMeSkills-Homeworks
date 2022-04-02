"""
# Task 14.07
# shlom41k
# classwork
"""

import argparse
import os

parser = argparse.ArgumentParser(description="Task 14.07")

try:
    parser.add_argument("folder_name", type=str)
    parser.add_argument("file_name", type=str)
    args = parser.parse_args()
except:
    args = parser.parse_args(["my_dir", "my_file.py"])


print(args.folder_name, args.file_name)

folder_name, file_name = args.folder_name, args.file_name

os.mkdir(folder_name)

with open(f"{folder_name}/{file_name}", encoding="utf-8", mode="w") as f:
    if file_name.endswith(".py"):
        f.write("def main():\n    pass\n\n")
        f.write("if __name__ == '__main__':\n    main()\n")

print("Script finish successfully")

