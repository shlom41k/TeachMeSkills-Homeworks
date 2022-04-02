"""
# Task 14.2
# shlom41k
"""

from datetime import datetime
from play_sound import play_jingle, sleep


# Constants
LOG_FILE = "pomodoro.log"


class Pomodoro:

    __logfile = LOG_FILE

    def __init__(self, firstname: str, lastname: str, focusing=25, pause=5, cycles=4, task="Programming"):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__focusing = focusing
        self.__pause = pause
        self.__cycles = cycles
        self.__task = task

    # Getters and setters
    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, fn: str):
        self.__firstname = fn

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, ln: str):
        self.__lastname = ln

    @property
    def focusing(self):
        return self.__focusing

    @focusing.setter
    def focusing(self, focus: int):
        self.__focusing = focus

    @property
    def pause(self):
        return self.__pause

    @pause.setter
    def pause(self, p: int):
        self.__pause = p

    @property
    def cycles(self):
        return self.__cycles

    @cycles.setter
    def cycles(self, c: int):
        self.__cycles = c

    @property
    def task(self):
        return self.__task

    @task.setter
    def task(self, task: str):
        self.__task = task

    # Convert to seconds
    @staticmethod
    def time_to_sec(m: int):
        return m * 60

    # Convert seconds to time
    @staticmethod
    def sec_to_mytime(sec: int):
        h = sec // 3600
        m = (sec % 3600) // 60
        s = sec % 60
        return h, m, s

    # Logging
    def log(self):
        now = datetime.now()
        dt = "{:04}-{:02}-{:02} {:02}:{:02}:{:02}".format(now.year, now.month, now.day, now.hour, now.minute,
                                                          now.second)
        with open(self.__class__.__logfile, "a") as logfile:
            print(f"{self.__firstname} {self.__lastname}, {dt}, focusing: {self.__focusing} min, "
                  f"pause: {self.__pause} min, cycles: {self.__cycles}; task: {self.__task}", file=logfile)

    # Start timer
    def start(self):
        self.log()
        print(f"\nInfo: {self.__firstname} {self.__lastname}, focusing = {self.__focusing} min, "
              f"pause = {self.__pause} min, cycles = {self.__cycles}; task: {self.__task}")
        print("Let's do it!")
        for j in range(self.__cycles):
            print("\n!!! Time to focusing !!!\n")
            play_jingle()

            focus = self.time_to_sec(self.__focusing)

            while focus >= 0:
                h, m, s = self.sec_to_mytime(focus)
                print("Cycle {}[{}], focusing time {:02}:{:02}:{:02}".format(j + 1, self.__cycles, h, m, s))
                focus -= 1
                sleep(1)
            else:
                print("\n!!! Time to take a break !!!\n")
                play_jingle()

            pause = self.time_to_sec(self.__pause)

            while pause >= 0:
                h, m, s = self.sec_to_mytime(pause)
                print("Cycle {}[{}], break time {:02}:{:02}:{:02}".format(j + 1, self.__cycles, h, m, s))
                pause -= 1
                sleep(1)
        else:
            print("\n!!! FINISH !!!")
            play_jingle()


if __name__ == "__main__":

    def main():
        my_timer = Pomodoro("Sergey", "shlom41k", focusing=1, pause=1, cycles=2, task="Create Pomodoro program")
        my_timer.start()

    main()
