from aoc_utils import data_import, matrix

raw_data = data_import.get_input()
test_raw_data = """ULL
RRDDD
LURDL
UUUUD"""

DIRECTIONS_4 = {
    "U": "UP",
    "L": "LEFT",
    "D": "DOWN",
    "R": "RIGHT",
}

pad = matrix.Matrix([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])

p2_pad = matrix.Matrix(
    [
        [".", ".", "1", ".", "."],
        [".", "2", "3", "4", "."],
        ["5", "6", "7", "8", "9"],
        [".", "A", "B", "C", "."],
        [".", ".", "D", ".", "."],
    ],
    bounds_mode="clamp_with_allowed_coords",
)

pad.set_position((1, 1))
p2_pad.set_position((0, 2))
p2_pad.create_allowed_coords(".")


def data_prep(raw_data):
    data = raw_data.split("\n")
    return data


def main_p1(data):
    answer = ""
    for line in data:
        for direction in line:
            pad.move(DIRECTIONS_4[direction])
        answer += pad.current_char
    print(answer)


def main_p2(data):
    answer = ""
    for line in data:
        for direction in line:
            p2_pad.move(DIRECTIONS_4[direction])
        answer += p2_pad.current_char
    print(answer)


if __name__ == "__main__":
    data = data_prep(raw_data)
    test_data = data_prep(test_raw_data)
    main_p1(data)
    main_p2(data)
