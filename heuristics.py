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

def a_star(board: np.ndarray, ai_piece: int, opponent_piece: int) -> int:
    move_score = -2000
    best_move = -1
    for col in range(c.COLUMNS):
        row = game.get_next_open_row(board, col)
        temp_score = calculate_score(board, row, col, ai_piece, opponent_piece)
        if temp_score > move_score:
            best_move = col
            move_score = temp_score
    return best_move


def calculate_score(board: np.ndarray, row: int, column: int, ai_piece: int, opponent_piece: int) -> int:
    logging.info("Calculate Score")
    
    score_ai =  0
    score_ai1 = 0
    score_ai2 = 0
    score_ai3 = 0
    score_ai4 = 0
    score_opponent = 0
    score_opponent1 = 0
    score_opponent2 = 0
    score_opponent3 = 0
    score_opponent4 = 0

    # Linha com 1 
    score_ai1 += 1 * get_ocurrences(board, 1, ai_piece, row, column)
    logging.info(f"1 ocorrencia ai: {score_ai1}")
    # Linha com 2 
    score_ai2 += 10 * get_ocurrences(board, 2, ai_piece, row, column)
    logging.info(f"2 ocorrencia ai: {score_ai2}")
    # Linha com 3 
    score_ai3 += 50 * get_ocurrences(board, 3, ai_piece, row, column)
    logging.info(f"3 ocorrencia ai: {score_ai3}")
    # Linha com 4
    score_ai4 += 1000 * get_ocurrences(board, 4, ai_piece, row, column)
    logging.info(f"3 ocorrencia ai: {score_ai3}")
    #Linha com 1 (Inimigo)
    score_opponent1 += 1 * get_ocurrences(board, 1, opponent_piece, row, column)
    logging.info(f"1 ocorrencia oponente: {score_opponent1}")
    #Linha com 2 Inimigo)
    score_opponent2 += 10 * get_ocurrences(board, 2, opponent_piece, row, column)
    logging.info(f"2 ocorrencia oponente: {score_opponent2}")
    #Linha com 3 (Inimigo)
    score_opponent3 += 50 * get_ocurrences(board, 3, opponent_piece, row, column)
    logging.info(f"3 ocorrencia oponente: {score_opponent3}")
    #Linha com 4 (Inimigo)
    score_opponent4 += 1000 * get_ocurrences(board, 4, opponent_piece, row, column)
    logging.info(f"3 ocorrencia oponente: {score_opponent3}")
    score_ai = score_ai1 + score_ai2 + score_ai3
    score_opponent = score_opponent1 + score_opponent2 + score_opponent3
    logging.info(f"Total: {score_ai - score_opponent}\n")
    if row > 5:
        score_opponent + 10000
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
            sliding_window = [board[row- i][col + i] for i in range(4)]
            for board_piece in sliding_window:
                print(board[row][column])
                if board_piece == piece:
                    temp += 1
        if temp == reference_quantity:
            occurrences += 1

    return occurrences

        
