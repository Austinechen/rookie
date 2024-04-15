"""


from karel.stanfordkarel import *


def main():
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_right()
    move()
    put_99_beeper()
    move()


def turn_right():
    for i in range(3):
        turn_left()


def put_99_beeper():
    for i in range(99):
        put_beeper()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
