import numpy as np
import constants as c

class Board:
    def __init__(self) -> None:
        self.rows = c.ROWS
        self.columns = c.COLUMNS
        self.board = np.zeros((self.rows, self.columns))
            
    def get_board(self) -> np.ndarray:
        return self.board

    def print_board(self) -> None:
        print(np.flip(self.board, 0), "\n")
        
 