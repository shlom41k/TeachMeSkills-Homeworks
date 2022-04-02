# shlom41k
"""
# Some tests for classes. Public and protected methods
"""


class User:

    def __init__(self, login: str, password: str):
        self._login = login
        self.__password = password

    def get_token(self):
        pass

    def __generate_token(self):
        return self.__password[::-1]


if __name__ == "__main__":
    u = User("login", "password")
    print(u._login)