from typing import List
from aoc_utils import data_import
import os
import time

raw_data = data_import.get_input()
data_import.preview()
example_data = """.#.#.#
...##.
#....#
..#...
#.#..#
####.."""

def data_prep(data):
    pass

def create_grid(length:int) -> List[List]:
    return [["." for _ in range(length)] for _ in range(length)]


def create_grid_from_str(data:str) -> List[List]:
    grid = []
    for row in data.splitlines():
        grid.append([char for char in list(row)])
    return grid

def display_grid(grid: List[List]) -> None:
    for l in grid:
        print("".join(l))


def return_value_in_grid(grid: List[List], row:int, column:int) -> str:
    row_max = len(grid) - 1
    col_max = len(grid[0]) - 1
    if row > row_max or column > col_max:
        return -1
    elif row < 0 or column < 0:
        return -1
    else:
        return grid[row][column]


def return_surrounding_score(grid: List[List], row: int, column: int) -> int:
    score = 0
    for r in range(row-1 , row + 2):
        for c in range(column -1, column + 2):
            if r == row and c == column:
                continue
            # print(r, c, return_value_in_grid(grid, r, c))
            score += return_score(return_value_in_grid(grid, r, c))
    return score


def return_score(value: str) -> int:
    if value == "#":
        return 1
    else:
        return 0


def next_grid(grid):
    next_grid = create_grid(len(grid))
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            char = return_value_in_grid(grid, row, col)
            surrounding_score = return_surrounding_score(grid, row, col)

            if char == "#" and surrounding_score in (2, 3):
                next_grid[row][col] = "#"
            elif char == "." and surrounding_score == 3:
                next_grid[row][col] = "#"
            else:
                next_grid[row][col] = "."
    return next_grid


def next_grid_p2(grid):
    next_grid = create_grid(len(grid))
    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            char = return_value_in_grid(grid, row, col)
            surrounding_score = return_surrounding_score(grid, row, col)

            if char == "#" and surrounding_score in (2, 3):
                next_grid[row][col] = "#"
            elif char == "." and surrounding_score == 3:
                next_grid[row][col] = "#"
            else:
                next_grid[row][col] = "."
    corner_coords = [(0,0), (0, max_col), (max_row, 0), (max_row, max_col)]
    for row, col in corner_coords:
        next_grid[row][col] = "#"
    return next_grid

def return_num_of_lights_on(grid: List[List]) -> int:
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '#':
                count += 1
    return count     

def main_p1(data:str, steps:int) -> None:
    grid = create_grid_from_str(data)
    print("Initial grid:")
    display_grid(grid)
    for _ in range(steps):
        grid = next_grid(grid)
    print("\nFinal Grid:")
    display_grid(grid)
    print(f"Count of Lights: {return_num_of_lights_on(grid)}")

def main_p2(data:str, steps:int):
    grid = create_grid_from_str(data)
    print("Initial grid:")
    display_grid(grid)
    for _ in range(steps):
        grid = next_grid_p2(grid)
    print("\nFinal Grid:")
    display_grid(grid)
    print(f"Count of Lights: {return_num_of_lights_on(grid)}")

def watch_game_of_life(data:str, steps:int) -> None:
    grid = create_grid_from_str(data)
    display_grid(grid)
    for _ in range(steps):
        os.system("clear")
        grid = next_grid_p2(grid)
        display_grid(grid)
        time.sleep(0.15)


if __name__ == "__main__":
    # main_p1(raw_data, 100)
    # main_p2(raw_data, 100)
    watch_game_of_life(raw_data, 100)