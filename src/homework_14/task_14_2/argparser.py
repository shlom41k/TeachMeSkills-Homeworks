"""
# Task 14.2
# shlom41k
"""

# import sys
import argparse


def pomodoro_argparse():
    # print(sys.argv)
    parser = argparse.ArgumentParser(description="Input data for Pomodoro program")

    parser.add_argument("-fn", "--first-name", dest="first_name", type=str, help="First name", default="Ivan")
    parser.add_argument("-ln", "--last-name", dest="last_name", type=str, help="Last name", default="Ivanov")
    parser.add_argument("-f", "--focusing", dest="focus", type=int, help="Focusing time (minutes)", default=25)
    parser.add_argument("-p", "--pause", dest="pause", type=int, help="Breaking time (minutes)", default=5)
    parser.add_argument("-c", "--cycles", dest="cycle", type=int, help="Number of cycles", default=4)
    parser.add_argument("-t", "--task", dest="task", type=str, help="Tank name", default="Programming")

    args = parser.parse_args()

    return args.first_name, args.last_name, args.focus, args.pause, args.cycle, args.task


if __name__ == "__main__":
    def self_main():
        print(*pomodoro_argparse())


    self_main()
