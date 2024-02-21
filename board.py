import numpy as np

class Board:

    def __init__(self, rows=6, columns=7, square_size = 100):
        self.rows = rows
        self.columns = columns
        self.data = np.zeros((rows, columns))
        self.square_size = square_size
        self.width = columns * square_size
        self.height = (rows + 1) * square_size
        self.radius = int(square_size / 2 -5)
       

    def drop_piece(self, row, col, piece):
        self.data[row][col] = piece

    def is_valid_location(self, col):
        return self.data[self.rows - 1][col] == 0

    def get_next_open_row(self, col):
        for r in range(self.rows):
            if self.data[r][col] == 0:
                return r

    def __str__(self):
        return str(np.flip(self.data, 0))

