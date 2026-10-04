import os
import time
import random

ROWS = 15
COLS = 30


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def make_grid():
    return [
        [random.choice([0, 0, 0, 1]) for _ in range(COLS)]
        for _ in range(ROWS)
    ]


def render(grid):
    clear_terminal()

    for row in grid:
        print("".join("██" if cell else "  " for cell in row))


def main():
    grid = make_grid()

    for _ in range(100):
        render(grid)

        # fake animation for demonstration
        grid = make_grid()

        time.sleep(0.15)


if __name__ == "__main__":
    main()