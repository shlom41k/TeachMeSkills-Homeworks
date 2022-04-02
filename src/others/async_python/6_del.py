from inspect import getgeneratorstate


class BlaBlaException(Exception):
    pass


def coroutine(func):

    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


# @coroutine
def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            # print("Ku-ku!")
            break
        else:
            print("..........", message)

    return "From subgen()"


@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaException as e:
    #         g.throw(e)
    result = yield from g
    print(result)


sg = subgen()
g = delegator(sg)

print(g.send("OK"))
print(g.send("dsghdgf"))
print(g.throw(StopIteration))

