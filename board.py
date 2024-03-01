import numpy as np
import constants as c
from dataclasses import dataclass

@dataclass
class Board:
    rows: int = c.ROWS
    columns: int = c.COLUMNS
    board: int = np.zeros((rows, columns))
            
    def get_board(self) -> np.ndarray:
        return self.board

    def print_board(self) -> None:
        print(np.flip(self.board, 0), "\n")
        
 