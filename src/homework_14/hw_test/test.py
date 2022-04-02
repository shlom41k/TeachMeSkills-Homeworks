import sys
import os

def sys_argv():
    print(sys.argv)

    s = 0
    for arg in sys.argv:
        if arg.isdigit():
            s += int(arg)

    print(s)


def with_os():
    spis = os.listdir()
    print(*spis, sep="\n")




if __name__ == "__main__":
    # sys_argv()
    with_os()

