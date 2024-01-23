'''
auto2048.py - This programs plays the GNOME 2048 game automatically by pressing
the UP, RIGHT, DOWN and LEFT arrow keys in that order.
'''


import time
import pyautogui as pag


def main():
    """The main function to run the program.
    """

    time.sleep(3)               # Give time to SWITCH to the game window.
    while True:
        pag.press("up")         # Press the 'up' arrow key.
        time.sleep(0.1)
        pag.press("right")      # Press the 'right' arrow key.
        time.sleep(0.1)
        pag.press("down")       # Press the 'down' arrow key.
        time.sleep(0.1)
        pag.press("left")       # PRess the 'left' arrow key.
        time.sleep(0.1)


if __name__ == "__main__":
    main()
