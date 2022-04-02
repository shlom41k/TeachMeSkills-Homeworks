"""
# Task 14.1
# shlom41k
"""

# import sys
import argparse


def timer_argparse():
    # print(sys.argv)

    parser = argparse.ArgumentParser(description="Input data for timer")

    parser.add_argument("-fn", "--first-name", dest="first_name", type=str, help="First name", default="Ivan")
    parser.add_argument("-ln", "--last-name", dest="last_name", type=str, help="Last name", default="Ivanov")
    parser.add_argument("-hh", "--hours", dest="h", type=int, help="Hours for timer", default=0)
    parser.add_argument("-mm", "--minutes", dest="m", type=int, help="Minutes for timer", default=0)
    parser.add_argument("-ss", "--seconds", dest="s", type=int, help="Seconds for timer", default=5)

    args = parser.parse_args()

    return args.first_name, args.last_name, args.h, args.m, args.s


if __name__ == "__main__":
    print(*timer_argparse())
