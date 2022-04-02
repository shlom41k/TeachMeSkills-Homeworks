# Task 14.1
# shlom41k

"""
Project struct
# main.py
# |- timer.py
# |   |- timer.log
# |
# |- play_sound.py
# |   |- air_raid_siren.wav
# |
# |- argparser.py

# !!! Before using, install 'pygame' package !!!

# You can try to run script main.py from console, using arguments:
# -fn -> first_name
# -ln -> last_name
# -h -> h (hours)
# -m -> m (minutes)
# -s -> s (seconds)

# for example: python main.py -fn Sergey -ln shlom41k -s 10
"""

from timer import MyTimer
from argparser import timer_argparse


if __name__ == "__main__":
    first_name, last_name, h, m, s = timer_argparse()
    my_timer = MyTimer(first_name, last_name, hh=h, mm=m, ss=s)
    my_timer.run_timer()