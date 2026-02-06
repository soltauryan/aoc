"""
The goal of this module is to provide a simple wrapper around a 2D list to make it easier
to work with matrices. It provides some basic functionality such as getting the dimensions
of the matrix, accessing elements, and iterating over the elements. It also provides some
additional functionality such as getting the neighbors of an element and rotating the
matrix.
"""

class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

    def __getitem__(self, idx):
        return self.data[idx]

    def __iter__(self):
        for row in self.data:
            for elem in row:
                yield elem

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