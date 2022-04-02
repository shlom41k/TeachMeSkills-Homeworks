"""
# Task 14.2
# shlom41k
"""

from time import sleep
from pygame import mixer


# Play sound
def play_jingle():
    mixer.init()
    mixer.music.load("ring.mp3")
    mixer.music.set_volume(1)
    mixer.music.play()
    sleep(2)
    mixer.music.stop()


if __name__ == "__main__":
    play_jingle()
