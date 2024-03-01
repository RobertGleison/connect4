import numpy as np
import constants as c 
import game_logic as game


def alphabeta(board: np.ndarray, piece: int) -> int:
    return 0

def monte_carlo_tree_search(board: np.ndarray, piece: int) -> int:
    best_column = 0
    return best_column

def a_star(board: np.ndarray, piece: int) -> int:
    # move_score = 0
    # best_move = 0
    # for col in range(c.COLUMNS):
    #     row = game.get_next_open_row(board, col)
    #     temp_score = calculate_score(board, row, col, piece)
    #     if temp_score > move_score:
    #         best_move = col
    #         move_score = temp_score
    # return best_move
    return 0


#@TODO: mudar int x e int y para uma tupla?
def calculate_score(board: np.ndarray, row: int, column: int, piece: int) -> int:
    scoreAI = 0
    # Linha com 1 
    scoreAI += 1 * get_ocurrences(board, 1, piece, row, column)
    # Linha com 2 
    scoreAI += 4 * get_ocurrences(board, 2, piece, row, column)
    # Linha com 3 
    scoreAI += 40 * get_ocurrences(board, 3, piece, row, column)
    # Linha com 4 
    scoreAI += 100 * get_ocurrences(board, 4, piece, row, column)
    
    return scoreAI 


def get_ocurrences(board: np.ndarray, reference_quantity: int, turn: int, row: int, column: int) -> int:
    occurrences = 0

    # Check horizontal    
    for col in range(c.COLUMNS-3):
        temp_quantity = 0
        for row in range(c.ROWS):
            groupOf4 = [board[row][col + i] for i in range(4)]
            for piece in groupOf4:
                if piece == turn:
                    temp_quantity+=1


    # Check vertical
    for col in range(c.COLUMNS):
        temp_quantity = 0
        for row in range(c.ROWS-3):
            groupOf4 = [board[row + i][col] for i in range(4)]
            for piece in groupOf4:
                if piece == turn:
                    temp_quantity+=1

    # Check ascending diagonal
    for col in range(c.COLUMNS-3):
        temp_quantity = 0
        for row in range(c.ROWS-3):
            groupOf4 = [board[row + i][col + i] for i in range(4)]
            for piece in groupOf4:
                if piece == turn:
                    temp_quantity+=1

    # Check descending diagonal
    for col in range(c.COLUMNS-3):
        temp_quantity = 0
        for row in range(3, c.ROWS):
            groupOf4 = [board[row + i][col - i] for i in range(4)]
            for piece in groupOf4:
                if piece == turn:
                    temp_quantity+=1
        
