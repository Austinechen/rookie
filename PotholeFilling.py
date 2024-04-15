"""
File: PotholeFilling.py
Name: Austine:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    Austine:
    """
    implement()


def implement():
    for i in range(3):
        move()
        turn_right()
        move()
        put_99_beeper()
        turn_back()
        move()
        turn_right()
        move()


def turn_right():
    for i in range(3):
        turn_left()


def put_99_beeper():
    for i in range(99):
        put_beeper()


def turn_back():
    for i in range(2):
        turn_left()


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
