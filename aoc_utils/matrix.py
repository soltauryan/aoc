"""
The goal of this module is to provide a simple wrapper around a 2D list to make it easier
to work with matrices. It provides some basic functionality such as getting the dimensions
of the matrix, accessing elements, and iterating over the elements. It also provides some
additional functionality such as getting the neighbors of an element and rotating the
matrix.
"""

DIRECTIONS_4 = {
    "UP": (0, -1),
    "LEFT": (-1, 0),
    "DOWN": (0, 1),
    "RIGHT": (1, 0),
}


class Matrix:
    def __init__(
        self,
        data: list[list[str]],
        allowed_coords=None,
        bounds_mode: str = "clamp",
        move_mode: str = "directions_4",
    ):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
        self.current_position = (0, 0)
        self.bounds_mode = bounds_mode
        self.move_mode = move_mode
        self.current_char = self.data[0][0]
        
        if allowed_coords is None:
            self.allowed_coords = set()

        if self.bounds_mode == "clamp_with_allowed_coords":
            self.allowed_coords.update(allowed_coords)

    def __getitem__(self, idx):
        return self.data[idx]

    def __iter__(self):
        for row in self.data:
            for elem in row:
                yield elem

    def clamp(
        self,
        value,
        min_val: int,
        max_val: int,
        left_inclusive=True,
        right_inclusive=False,
    ):
        """Clamp values to a min and max value. Define seperate logic for each possible inclusive state."""
        if left_inclusive and not right_inclusive:
            if value < min_val:
                return min_val
            elif value >= max_val:
                return max_val - 1
            else:
                return value
        else:
            return AttributeError

    def show_grid(self):
        """Display the matrix in the terminal"""
        for row in self.data:
            print(row)

    def set_position(self, new_coords: tuple):
        self.current_position = new_coords
        self.current_char = self.data[new_coords[1]][new_coords[0]]

    def create_allowed_coords(self, null_character="."):
        for y in range(self.rows):
            for x in range(self.cols):
                if self.data[y][x] == null_character:
                    pass
                else:
                    self.allowed_coords.add((x, y))

    def move(self, instruction):
        """Move the current position around the grid"""
        new_position = self.current_position

        if self.bounds_mode == "clamp" and self.move_mode == "directions_4":
            new_x = new_position[0] + DIRECTIONS_4[instruction][0]
            new_x = self.clamp(new_x, 0, self.cols)
            new_y = new_position[1] + DIRECTIONS_4[instruction][1]
            new_y = self.clamp(new_y, 0, self.rows)

            self.set_position((new_x, new_y))

        elif (
            self.bounds_mode == "clamp_with_allowed_coords"
            and self.move_mode == "directions_4"
        ):
            new_x = new_position[0] + DIRECTIONS_4[instruction][0]
            new_y = new_position[1] + DIRECTIONS_4[instruction][1]

            if (new_x, new_y) in self.allowed_coords:
                self.set_position((new_x, new_y))

    def neighbors(self, row, col):
        """Returns the neighbors of the element at (row, col)"""
        neighbors = []
        for r in range(max(0, row - 1), min(self.rows, row + 2)):
            for c in range(max(0, col - 1), min(self.cols, col + 2)):
                if (r, c) != (row, col):
                    neighbors.append(self.data[r][c])
        return neighbors

    def rotate(self):
        """Rotates the matrix 90 degrees clockwise"""
        rotated = [[None] * self.rows for _ in range(self.cols)]
        for r in range(self.rows):
            for c in range(self.cols):
                rotated[c][self.rows - r - 1] = self.data[r][c]
        return Matrix(rotated)
