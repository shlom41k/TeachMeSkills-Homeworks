"""
# Task 14.1
# shlom41k
"""

from time import sleep
from pygame import mixer

# Play siren
def play_siren():
    mixer.init()
    mixer.music.load("air_raid_siren.wav")
    mixer.music.set_volume(0.7)
    mixer.music.play()
    sleep(10)
    mixer.music.stop()


if __name__ == "__main__":
    play_siren()