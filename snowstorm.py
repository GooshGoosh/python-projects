import os
import random
import time


# Thickness of snow on screen.
SNOW_DENSITY = 5
# Number of seconds before updating snowstorm
DELAY = .3

snowflakes = ['❄️', '❅', '❆', '❃', '❇', '❈', '❋']

term = os.get_terminal_size()

w = term.columns
h = term.lines

grid = []

for _ in range(h):
    grid.append([' '] * w)


def draw_grid():
    os.system('cls' if os.name == 'nt' else 'clear')

    # Remove cursor from the terminal.
    print('\033[?25l')

    output = ''

    for row in grid:
        output += ''.join(row) + '\n'

    output = output.strip('\n')

    print(output, end='')


while True:
    row = []

    for _ in range(w):
        if random.random() < SNOW_DENSITY / 100:
            row.append(random.choice(snowflakes))
        else:
            row.append(' ')

    grid.insert(0, row)
    grid.pop()

    draw_grid()

    time.sleep(DELAY)
