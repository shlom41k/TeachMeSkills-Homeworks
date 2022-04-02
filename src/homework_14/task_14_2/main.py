"""
# Task 14.2
# shlom41k

Project struct
# main.py
# |- pomodoro.py
# |   |- pomodoro.log
# |
# |- play_sound.py
# |   |- ring.mp3
# |
# |- argparser.py

# !!! Before using, install 'pygame' package !!!

# You can try to run script main.py from console, using arguments:
# -fn -> first_name [str]
# -ln -> last_name [str]
# -f -> focus: time to focusing (in minutes) [int]
# -p -> pause: time to break (in minutes) [int]
# -c -> cycle: number of cycles [int]
# -t -> task : task description [str]

# for example: python main.py -fn Sergey -ln shlom41k -c 3
"""

from pomodoro import Pomodoro
from argparser import pomodoro_argparse


if __name__ == "__main__":
    first_name, last_name, focus, pause, cycle, task = pomodoro_argparse()
    my_timer = Pomodoro(first_name, last_name, focusing=focus, pause=pause, cycles=cycle, task=task)
    my_timer.start()