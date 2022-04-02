# Task 12.1
# shlom41k

"""
# Создать класс MyTime. Атрибуты: hours, minutes, seconds.
# Методы: переопределить магические методы сравнения(==, !=, >=, <=, <, >),
# сложения, вычитания, умножения на число, вывод на экран.
# Перегрузить конструктор на обработку входных параметров вида:
# одна строка, три числа, другой объект класса MyTime, и отсутствие входных параметров.
# Реализовать нормальное отображение времени (13:06:23)
"""

"""
class MyException(Exception):
    def __init__(self, message="AAA!!!"):
        super().__init__(message)
"""


class MyTime:
    def __init__(self, str_time="", hours=0, minutes=0, seconds=0, my_time=None):
        # If input data - string
        if str_time:
            try:
                h, m, s = map(int, str_time.split(":"))
                if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
                    self.__hours, self.__minutes, self.__seconds = h, m, s
                else:
                    print("Error: Input data out of range")
            except:
                print("Error: Invalid input string")

        # If input data - int
        elif hours or minutes or seconds:
            if (type(hours) == type(minutes) == type(seconds) == int) and \
                    (0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59):
                self.__hours, self.__minutes, self.__seconds = hours, minutes, seconds
            else:
                print("Error: Invalid input data")

        # If input data - MyTime object
        elif my_time:
            if type(my_time) == type(self):
                self.__dict__ = my_time.__dict__
            else:
                print(f"Error: Input object in not {type(self)} type")

        else:
            print("Error: Empty or invalid input data")

    # Override "magical" methods
    # Output format
    def __str__(self):
        return "{:02}:{:02}:{:02}".format(self.__hours, self.__minutes, self.__seconds)

    # class <MyTime> '==' class <MyTime>
    def __eq__(self, other):
        if type(other) == type(self):
            return self.__hours == other.__hours and self.__minutes == other.__minutes and \
                   self.__seconds == other.__seconds
        else:
            print("Error! Input arguments have various types")

    # class <MyTime> '!=' class <MyTime>
    def __ne__(self, other):
        if type(other) == type(self):
            return self.__hours != other.__hours and self.__minutes != other.__minutes and \
                   self.__seconds != other.__seconds
        else:
            print("Error! Input arguments have various types")

    # class <MyTime> '<' class <MyTime>
    def __lt__(self, other):
        if type(other) == type(self):
            return self.mytime_to_sec(self.__hours, self.__minutes, self.__seconds) < \
                   other.mytime_to_sec(other.__hours, other.__minutes, other.__seconds)
        else:
            print("Error! Input arguments have various types")

    # class <MyTime> '>' class <MyTime>
    def __gt__(self, other):
        if type(other) == type(self):
            return self.mytime_to_sec(self.__hours, self.__minutes, self.__seconds) > \
                   other.mytime_to_sec(other.__hours, other.__minutes, other.__seconds)
        else:
            print("Error! Input arguments have various types")

    # class <MyTime> '<=' class <MyTime>
    def __le__(self, other):
        if type(other) == type(self):
            return self.mytime_to_sec(self.__hours, self.__minutes, self.__seconds) <= \
                   other.mytime_to_sec(other.__hours, other.__minutes, other.__seconds)
        else:
            print("Error! Input arguments have various types")

    # class <MyTime> '>=' class <MyTime>
    def __ge__(self, other):
        if type(other) == type(self):
            return self.mytime_to_sec(self.__hours, self.__minutes, self.__seconds) >= \
                   other.mytime_to_sec(other.__hours, other.__minutes, other.__seconds)
        else:
            print("Error! Input arguments have various types")

    # class <MyTime> '+' class <MyTime>
    def __add__(self, other):
        if type(other) == type(self):
            add = self.mytime_to_sec(self.__hours, self.__minutes, self.__seconds) + \
                  other.mytime_to_sec(other.__hours, other.__minutes, other.__seconds)
            if add >= 24 * 3600:
                return self.sec_to_mytime(add % (24 * 3600))
            else:
                return self.sec_to_mytime(add)
        else:
            print("Error! Input arguments have various types")

    # class <MyTime> '-' class <MyTime>
    def __sub__(self, other):
        if type(other) == type(self):
            sub = self.sec_to_mytime(self.mytime_to_sec(self.__hours, self.__minutes, self.__seconds) -
                                     other.mytime_to_sec(other.__hours, other.__minutes, other.__seconds))
            return sub
        else:
            print("Error! Input arguments have various types")

    # class <MyTime> '*' class<int>
    def __mul__(self, other):
        if type(other) == int:
            mult = self.mytime_to_sec(self.__hours, self.__minutes, self.__seconds) * other
            if mult >= 24 * 3600:
                return self.sec_to_mytime(mult % (24 * 3600))
            else:
                return self.sec_to_mytime(mult)
        else:
            print("Error! Input arguments have various types")

    # Properties
    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    # Setters
    @hours.setter
    def hours(self, hh: int):
        if type(hh) == int and 0 <= hh <= 23:
            self.__hours = hh
        else:
            print("Error! Input arguments out of range!")

    @minutes.setter
    def minutes(self, mm: int):
        if type(mm) == int and 0 <= mm <= 59:
            self.__minutes = mm
        else:
            print("Error! Input arguments out of range!")

    @seconds.setter
    def seconds(self, ss: int):
        if type(ss) == int and 0 <= ss <= 59:
            self.__seconds = ss
        else:
            print("Error! Input arguments out of range!")

    # Convert MyTime to seconds
    @staticmethod
    def mytime_to_sec(h, m, s):
        return h * 3600 + m * 60 + s

    # Convert seconds to MyTime
    @staticmethod
    def sec_to_mytime(sec):
        return MyTime(hours=sec // 3600, minutes=(sec % 3600) // 60, seconds=sec % 60)


if __name__ == "__main__":
    def main():
        # Create object
        a = MyTime("22:25:44")
        print(a)
        print(type(a))

        # Create object
        b = MyTime(hours=14, minutes=53, seconds=22)
        print(b)
        print(type(b))

        # Create object
        c = MyTime(my_time=MyTime("01:11:35"))
        print(c)
        print(type(c))

        # Create object
        d = MyTime()  # Error - empty input data

        # Compare
        print(a < b)
        print(type(a < b))
        print(a > b)
        print(b <= a)
        print(b >= a)

        # Create objects
        t1 = MyTime("14:30:20")
        print("t1 =", t1)

        t2 = MyTime(hours=6, minutes=30, seconds=20)
        print("t2 =", t2)

        # Some math operations
        print("t1 + t2 = ", (t1 + t2))
        print("t1 - t2 = ", t1 - t2)
        print("t2 * n = ", t2 * 4)

        print(type(t1 + t2))
        print(type(t1 - t2))
        print(type(t2 * 4))

        t1.hours = 25   # Error - out of range

    main()
