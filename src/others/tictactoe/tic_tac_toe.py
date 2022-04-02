"""
# shlom41k

packages:
- pygame
- tabulate
"""

import pygame.mixer
from tabulate import tabulate
from time import sleep
from pygame import mixer
from random import randint


"""
Делаем игру крестики-нолики
-- поле 3*3
-- Режимы игры: 1 игрок (Player vs. Computer), 2 игрока (Player 1 vs. Player 2)
"""


class Cell:
    _value: str

    def __init__(self):
        self._value = ""

    def __str__(self):
        return "." if self._value == "" else self._value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val: str):
        self._value = val


class Field:

    _width = 3
    _height = 3

    def __init__(self):
        self._field = [
            ["\\", "1", "2", "3"],
            ["a", Cell(), Cell(), Cell()],
            ["b", Cell(), Cell(), Cell()],
            ["c", Cell(), Cell(), Cell()],
        ]

    def print(self):
        print(tabulate(self._field, tablefmt="grid", stralign='center'))

    def get_value(self, row: int, col: int):
        return self._field[row][col]._value

    def set_value(self, row: int, col: int, val: str):
        self._field[row][col]._value = val

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width: int):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height: int):
        self._height = height


class Application:

    _players: list
    _sym: str
    _sym_comp: str
    _mode = "multi"
    _sound = "sound/"

    def __init__(self):
        self.field = Field()

    def play_background(self, file: str):
        self._mixer = mixer
        self._mixer.init()
        self._mixer.music.load(file)
        self._mixer.music.set_volume(0.5)
        self._mixer.music.play(loops=-1)
        # sleep(2)
        # mixer.music.stop()

    @staticmethod
    def play_sound(file: str, volume: int, time=None):
        sobj = pygame.mixer.Sound(file)
        sobj.set_volume(volume)
        sobj.play()
        if time:
            sleep(time)
            sobj.stop()

    def choose_symbol(self):
        players = ["X", "0"]
        while True:
            sym = input(f"Player{' 1' if self._mode == 'multi' else ''}, выберите Ваш символ: [X - крестик, 0 - нолик]: ").upper()
            if sym == "X":
                if self._mode == "multi":
                    print("\nPlayer: X (крестики), Player 2: 0 (нолики).")
                else:
                    print("\nPlayer: X (крестики), Computer: 0 (нолики).")
                break
            elif sym == "0":
                players.reverse()
                if self._mode == "multi":
                    print("\nPlayer: 0 (нолики), Player 2: X (крестики).")
                else:
                    print("\nPlayer: 0 (нолики), Computer: X (крестики).")
                break
            else:
                print("Некорректный символ!")
                self.play_sound(self._sound + "wrong.mp3", volume=1)

        self._players, self._sym = players, sym
        self.play_sound(self._sound + "sfx-1.mp3", volume=1)

        if self._mode == "single":
            self._sym_comp = "0" if self._sym == "X" else "X"

    def game_mode(self):
        while True:
            mode = input("Выберите режим игры: [1] - Single mode, [2] - Multiplayer: ")

            if mode == "1":
                self._mode = "single"
            elif mode == "2":
                self._mode = "multi"
            else:
                print("WARNING! Некорректрый ввод")
                self.play_sound(self._sound + "wrong.mp3", volume=1)
                continue

            self.play_sound(self._sound + "sfx-1.mp3", volume=1)
            break

    def make_step(self):
        while True:
            self.field.print()

            try:
                if self._mode == "multi":
                    row, col = list(input(f"Player {1 if self._players[0] == self._sym else 2} [{self._players[0]}], Ваш ход: "))
                else:
                    row, col = list(input(f"Player [{self._sym}], Ваш ход: "))
            except:
                print("WARNING! Для совершения хода введите строку и столбец, например, а3")
                self.play_sound(self._sound + "wrong.mp3", volume=1)
                continue

            if row.lower() not in "abc" or col not in "123":
                print("WARNING! Вне диапазона игнового поля")
                self.play_sound(self._sound + "wrong.mp3", volume=1)
                continue

            row_ind = "abc".find(row.lower()) + 1
            col_ind = int(col)

            if self.field.get_value(row_ind, col_ind) == "":
                self.field.set_value(row_ind, col_ind, self._players[0])
                self.play_sound(self._sound + "sfx-8.mp3", volume=1)
                break
            else:
                self.play_sound(self._sound + "shot_none.mp3", volume=1)
                print("Данная ячейка уже занята!")

    def can_win(self, gamer: str) -> bool:
        for i in range(1, self.field.width + 1):
            if self.field.get_value(i, 1) == self.field.get_value(i, 2) == gamer and self.field.get_value(i, 3) == "":
                if gamer == self._sym_comp:
                    self.field.set_value(i, 3, gamer)
                else:
                    self.field.set_value(i, 3, self._sym_comp)
                return True

            elif self.field.get_value(i, 1) == self.field.get_value(i, 3) == gamer and self.field.get_value(i, 2) == "":
                if gamer == self._sym_comp:
                    self.field.set_value(i, 2, gamer)
                else:
                    self.field.set_value(i, 2, self._sym_comp)
                return True

            elif self.field.get_value(i, 2) == self.field.get_value(i, 3) == gamer and self.field.get_value(i, 1) == "":
                if gamer == self._sym_comp:
                    self.field.set_value(i, 1, gamer)
                else:
                    self.field.set_value(i, 1, self._sym_comp)
                return True

        for j in range(1, self.field.height + 1):
            if self.field.get_value(1, j) == self.field.get_value(2, j) == gamer and self.field.get_value(3, j) == "":
                if gamer == self._sym_comp:
                    self.field.set_value(3, j, gamer)
                else:
                    self.field.set_value(3, j, self._sym_comp)
                return True

            elif self.field.get_value(1, j) == self.field.get_value(3, j) == gamer and self.field.get_value(2, j) == "":
                if gamer == self._sym_comp:
                    self.field.set_value(2, j, gamer)
                else:
                    self.field.set_value(2, j, self._sym_comp)
                return True

            elif self.field.get_value(2, j) == self.field.get_value(3, j) == gamer and self.field.get_value(1, j) == "":
                if gamer == self._sym_comp:
                    self.field.set_value(1, j, gamer)
                else:
                    self.field.set_value(1, j, self._sym_comp)
                return True

        if self.field.get_value(1, 1) == self.field.get_value(2, 2) == gamer and self.field.get_value(3, 3) == "":
            if gamer == self._sym_comp:
                self.field.set_value(3, 3, gamer)
            else:
                self.field.set_value(3, 3, self._sym_comp)
            return True

        elif self.field.get_value(1, 1) == self.field.get_value(3, 3) == gamer and self.field.get_value(2, 2) == "":
            if gamer == self._sym_comp:
                self.field.set_value(2, 2, gamer)
            else:
                self.field.set_value(2, 2, self._sym_comp)
            return True

        elif self.field.get_value(2, 2) == self.field.get_value(3, 3) == gamer and self.field.get_value(1, 1) == "":
            if gamer == self._sym_comp:
                self.field.set_value(1, 1, gamer)
            else:
                self.field.set_value(1, 1, self._sym_comp)
            return True

        elif self.field.get_value(1, 3) == self.field.get_value(2, 2) == gamer and self.field.get_value(3, 1) == "":
            if gamer == self._sym_comp:
                self.field.set_value(3, 1, gamer)
            else:
                self.field.set_value(3, 1, self._sym_comp)
            return True

        elif self.field.get_value(1, 3) == self.field.get_value(3, 1) == gamer and self.field.get_value(2, 2) == "":
            if gamer == self._sym_comp:
                self.field.set_value(2, 2, gamer)
            else:
                self.field.set_value(2, 2, self._sym_comp)
            return True

        elif self.field.get_value(2, 2) == self.field.get_value(3, 1) == gamer and self.field.get_value(1, 3) == "":
            if gamer == self._sym_comp:
                self.field.set_value(1, 3, gamer)
            else:
                self.field.set_value(1, 3, self._sym_comp)
            return True
        return False

    def set_to_angle(self):
        if self.field.get_value(2, 2) == "":
            self.field.set_value(2, 2, self._sym_comp)
            return True

        if self.field.get_value(2, 2) == self._sym:
            if self.field.get_value(1, 1) == "":
                self.field.set_value(1, 1, self._sym_comp)
                return True
            elif self.field.get_value(1, 3) == "":
                self.field.set_value(1, 3, self._sym_comp)
                return True
            elif self.field.get_value(3, 1) == "":
                self.field.set_value(3, 1, self._sym_comp)
                return True
            elif self.field.get_value(3, 3) == "":
                self.field.set_value(3, 3, self._sym_comp)
                return True
        return False

    def random_comp_step(self):
        while True:
            row, col = randint(1, 3), randint(1, 3)
            if self.field.get_value(row, col) == "":
                self.field.set_value(row, col, self._sym_comp)
                break

    def is_win(self):

        if (self.field.get_value(1, 1) == self.field.get_value(1, 2) == self.field.get_value(1, 3) and self.field.get_value(1, 1) != "") or \
                (self.field.get_value(2, 1) == self.field.get_value(2, 2) == self.field.get_value(2, 3) and self.field.get_value(2, 1) != "") or\
                (self.field.get_value(3, 1) == self.field.get_value(3, 2) == self.field.get_value(3, 3) and self.field.get_value(3, 1) != "") or \
                (self.field.get_value(1, 1) == self.field.get_value(2, 1) == self.field.get_value(3, 1) and self.field.get_value(1, 1) != "") or \
                (self.field.get_value(1, 2) == self.field.get_value(2, 2) == self.field.get_value(3, 2) and self.field.get_value(1, 2) != "") or \
                (self.field.get_value(1, 3) == self.field.get_value(2, 3) == self.field.get_value(3, 3) and self.field.get_value(1, 3) != "") or \
                (self.field.get_value(1, 1) == self.field.get_value(2, 2) == self.field.get_value(3, 3) and self.field.get_value(1, 1) != "") or \
                (self.field.get_value(1, 3) == self.field.get_value(2, 2) == self.field.get_value(3, 1) and self.field.get_value(1, 3) != ""):

            return True
        return False

    def if_field_full(self):
        for i in range(1, self.field.width + 1):
            if any(list(map(lambda x: x == "", [self.field.get_value(i, j) for j in range(1, self.field.height + 1)]))):
                return False
        else:
            return True

    def draw(self):
        self.field.print()
        print("НИЧЬЯ! Свободных клеток нет.")
        self._mixer.music.stop()
        sleep(0.5)
        self.play_sound(self._sound + "game_over.mp3", volume=1, time=4)

    def multiplayer(self):
        while True:
            self.make_step()

            if self.is_win():
                self.field.print()
                print(f"Player {2 if self._players[0] == self._sym else 1} game over. "
                      f"Player {1 if self._players[0] == self._sym else 2} WINS!")
                self._mixer.music.stop()
                sleep(0.5)
                self.play_sound(self._sound + "fanfara.mp3", volume=1, time=6)
                break

            if self.if_field_full():
                self.draw()
                break

            self._players.append(self._players.pop(0))

    def single_mode(self):
        while True:
            self.make_step()

            if self.is_win():
                self.field.print()
                print(f"Player WINS!")
                self._mixer.music.stop()
                sleep(0.5)
                self.play_sound(self._sound + "fanfara.mp3", volume=1, time=6)
                break

            if self.if_field_full():
                self.draw()
                break

            self.field.print()
            print(f"Computer [{self._sym_comp}] ходит", end=" ")

            sleep(0.7)
            if self.can_win(gamer=self._sym_comp):
                print("(шанс победы компъютера)")
                self.play_sound(self._sound + "sfx-8.mp3", volume=1)
                self.field.print()
                self._mixer.music.stop()
                print(f"GAME OVER! Computer WINS!")
                self.play_sound(self._sound + "mario-smert.mp3", volume=1, time=4)
                break

            if self.can_win(gamer=self._sym):
                print("(угроза победы игрока)")
                self.play_sound(self._sound + "sfx-8.mp3", volume=1)
                continue

            if self.set_to_angle():
                print("(Ход в свободный угол)")
                self.play_sound(self._sound + "sfx-8.mp3", volume=1)
            else:
                print("(рандомный ход)")
                self.random_comp_step()
                self.play_sound(self._sound + "sfx-8.mp3", volume=1)

            if self.if_field_full():
                self.draw()
                break

    def run(self):
        print("Добро пожаловать в игру крестики-нолики!\n")

        self.play_background(file=self._sound + "chip.mp3")
        self.game_mode()
        self.choose_symbol()

        print("Для совершения хода введите строку и столбец, например, 'а3'")

        if self._mode == "multi":
            self.multiplayer()
        else:
            self.single_mode()

        self._mixer.music.stop()


if __name__ == "__main__":
    app = Application()
    app.run()


