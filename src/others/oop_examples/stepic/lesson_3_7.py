# __call__

from time import perf_counter


class Counter:

    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.length = 0
        print("Init object:", self)

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.length += len(args)
        print(f"Object {self} called {self.counter}")

    def average(self) -> float:
        return self.summa / self.length


class Timer:

    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f"Called function {self.fn.__name__}")

        result = self.fn(*args, **kwargs)

        finish = perf_counter()
        print(f"Function works {finish - start}")
        return result


if __name__ == '__main__':

    @Timer
    def fact(n):
        if n <= 1:
            return n
        return n * fact(n - 1)

    # @Timer
    def fib(n):
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    print(fib(6))
    # print(fact(10))
    print(Timer(fib)(10))

    # c = Counter()
    # c()
    # c()
    # c()
    # c(1, 5, -2)
    # print(c.summa)
    # print(c.length)
    # c(0, 3, 2, 2)
    # print(c.summa)
    # print(c.length)
