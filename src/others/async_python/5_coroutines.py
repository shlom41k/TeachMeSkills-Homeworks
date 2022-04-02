from inspect import getgeneratorstate


class BlaBlaException(Exception):
    pass

def coroutine(func):

    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner

def subgen():
    x = "Ready to accept message"
    message = yield x
    print("Subgen received:", message)


@coroutine
def average():
    cnt = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print("Done")
            break
        except BlaBlaException:
            print("...........................")
            break
        else:
            cnt += 1
            summ += x
            average = round(summ / cnt, 2)

    return average


g = average()
print(getgeneratorstate(g))

print(g.send(5))
print(g.send(6))
print(g.send(1))

try:
    g.throw(StopIteration)
except StopIteration as e:
    print("Average:", e.value)
