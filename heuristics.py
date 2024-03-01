import numpy as np
import constants as c 
import game_logic as game
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def alphabeta(board: np.ndarray, piece: int) -> int:
    return 0

def monte_carlo_tree_search(board: np.ndarray, piece: int) -> int:
    best_column = 0
    return best_column

def a_star(board: np.ndarray, piece: int) -> int:
    move_score = 0
    best_move = 0
    for col in range(c.COLUMNS):
        row = game.get_next_open_row(board, col)
        temp_score = calculate_score(board, row, col, piece)
        if temp_score > move_score:
            best_move = col
            move_score = temp_score
    return best_move


def calculate_score(board: np.ndarray, row: int, column: int, piece: int) -> int:
    logging.info("Calculate Score")
    score_ai = 0
    score_opponent = 0
    # Linha com 1 
    score_ai += 1 * get_ocurrences(board, 1, piece, row, column)
    # Linha com 2 
    score_ai += 10 * get_ocurrences(board, 2, piece, row, column)
    # Linha com 3 
    score_ai += 50 * get_ocurrences(board, 3, piece, row, column)
    #Linha com 1 (Inimigo)
    score_opponent += 1 * get_ocurrences(board, 1, piece, row, column)
    #Linha com 2 Inimigo)
    score_opponent += 10 * get_ocurrences(board, 2, piece, row, column)
    #Linha com 3 (Inimigo)
    score_opponent += 50 * get_ocurrences(board, 3, piece, row, column)
    
    return score_ai - score_opponent 


def get_ocurrences(board: np.ndarray, reference_quantity: int, piece: int, row: int, column: int) -> int:
    occurrences = 0

    # Check horizontal
    for col in range(c.COLUMNS - 3):
        temp = 0
        for row in range(c.ROWS):
            sliding_window = [board[row][col + i] for i in range(4)]
            for board_piece in sliding_window:
                if board_piece == piece:
                    temp += 1
        if temp == reference_quantity:
            occurrences += 1


    # Check vertical
    for col in range(c.COLUMNS):
        temp = 0
        for row in range(c.ROWS - 3):
            sliding_window = [board[row + i][column] for i in range(4)]
            for board_piece in sliding_window:
                if board_piece == piece:
                    temp += 1
        if temp == reference_quantity:
            occurrences += 1

    # Check ascending diagonal
    for col in range(c.COLUMNS - 3):
        temp = 0
        for row in range(c.ROWS - 3):
            sliding_window = [board[row + i][col + i] for i in range(4)]
            for board_piece in sliding_window:
                if board_piece == piece:
                    temp += 1
        if temp == reference_quantity:
            occurrences += 1

    # Check descending diagonal
    for col in range(c.COLUMNS - 3):
        temp = 0
        for row in range(3, c.ROWS):
            sliding_window = [board[row + i][col - i] for i in range(4)]
            for board_piece in sliding_window:
                if board_piece == piece:
                    temp += 1
        if temp == reference_quantity:
            occurrences += 1

    return occurrences

        
