# shom41k
# homework 17.2


class WrongInputError(Exception):
    def __init__(self, message='Wrong input'):
        super().__init__(message)


class Math:
    def __init__(self, x, y):
        validate_args(x, y)
        self.x = x
        self.y = y

    def calc_sum(self):
        return self.x + self.y

    def calc_diff(self):
        return self.x - self.y

    def calc_mult(self):
        return self.x * self.y

    def calc_div(self):
        return self.x / self.y


def validate_args(x, y):
    message = ''
    if not isinstance(x, (int, float)):
        message += f'The first argument type should be int or float. Now it is{type(x)}.\n'
    if not isinstance(y, (int, float)):
        message += f'The second argument type should be int or float. Now it is{type(y)}.\n'
    if message:
        raise WrongInputError(message)


if __name__ == '__main__':

    # print(validate_args(1, -1))
    print(isinstance(True, int))