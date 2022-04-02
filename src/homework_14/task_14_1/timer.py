# Task 14.1
# shlom41k

"""
Написать программу таймер. Программа при запуске принимает имя, фамилию, часы, минуты и секунды.
После программа начинает обратный отсчет выводя оставшееся время.
Программа должна хранить файл логирования с информацией о том кто запускал программу и когда.
"""

from datetime import datetime
from play_sound import play_siren, sleep

# Constants
LOG_FILE = "timer.log"


class MyTimer:

    __logfile = LOG_FILE

    def __init__(self, firstname: str, lastname: str, hh: int, mm: int, ss: int):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__hh = hh
        self.__mm = mm
        self.__ss = ss

        if (type(hh) == type(mm) == type(ss) == int) and \
                (0 <= hh <= 23 and 0 <= mm <= 59 and 0 <= ss <= 59):
            self.__hh, self.__mm, self.__ss = hh, mm, ss
        else:
            print("Error: Invalid input data")

    # Getters and setters
    @property
    def hh(self):
        return self.__hh

    @hh.setter
    def hh(self, hh: int):
        if type(hh) == int and 0 <= hh <= 23:
            self.__hh = hh
        else:
            print("Error! Input arguments out of range!")

    @property
    def mm(self):
        return self.__mm

    @mm.setter
    def mm(self, mm: int):
        if type(mm) == int and 0 <= mm <= 59:
            self.__mm = mm
        else:
            print("Error! Input arguments out of range!")

    @property
    def ss(self):
        return self.__ss

    @ss.setter
    def ss(self, ss: int):
        if type(ss) == int and 0 <= ss <= 59:
            self.__ss = ss
        else:
            print("Error! Input arguments out of range!")

    # Convert MyTime to seconds
    @staticmethod
    def mytime_to_sec(h: int, m: int, s: int):
        return h * 3600 + m * 60 + s

    # Convert seconds to MyTime
    @staticmethod
    def sec_to_mytime(sec: int):
        h = sec // 3600
        m = (sec % 3600) // 60
        s = sec % 60
        return h, m, s

    # Logging
    def log(self):
        now = datetime.now()
        dt = "{:04}-{:02}-{:02} {:02}:{:02}:{:02}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
        with open(self.__class__.__logfile, "a") as logfile:
            print(f"{self.__firstname} {self.__lastname}, {dt}", file=logfile)

    # Start timer
    def run_timer(self):
        print(f"\n{self.__firstname}! Attention! Timer activated!")
        self.log()
        seconds = self.mytime_to_sec(self.__hh, self.__mm, self.__ss)

        while seconds >= 0:
            h, m, s = self.sec_to_mytime(seconds)
            print("{:02}:{:02}:{:02}".format(h, m, s))
            seconds -= 1
            sleep(1)
        else:
            print("!!! ALARM !!!")
            play_siren()


if __name__ == "__main__":
    my_timer = MyTimer("Sergey", "shlom41k", hh=0, mm=0, ss=2)
    my_timer.run_timer()

