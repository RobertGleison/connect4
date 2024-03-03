import numpy as np
import constants as c 
import game_logic as game
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def a_star(board: np.ndarray, ai_piece: int, opponent_piece: int) -> int:
    move_score = -2000
    best_move = -1
    for col in range(c.COLUMNS):
        if not game.is_valid(board, col): continue
        temp_score = 0
        board_copy = board.copy()
        row = game.get_next_open_row(board_copy, col)
        game.drop_piece(board_copy, row, col, 2)
        temp_score = calculate_score(board_copy, row, col, ai_piece, opponent_piece)
        if temp_score > move_score:
            best_move = col
            move_score = temp_score
    return best_move


def calculate_score(board: np.ndarray, row: int, column: int, ai_piece: int, opponent_piece: int) -> int:
    score_ai =  0
    score_opponent = 0

    score_ai += 1 * get_ocurrences(board, 1, ai_piece, row, column)
    score_ai += 10 * get_ocurrences(board, 2, ai_piece, row, column)
    score_ai += 50 * get_ocurrences(board, 3, ai_piece, row, column)
    score_ai += 1000 * get_ocurrences(board, 4, ai_piece, row, column)

    score_opponent += 1 * get_ocurrences(board, 1, opponent_piece, row, column)
    score_opponent += 10 * get_ocurrences(board, 2, opponent_piece, row, column)
    score_opponent += 50 * get_ocurrences(board, 3, opponent_piece, row, column)
    score_opponent += 1000 * get_ocurrences(board, 4, opponent_piece, row, column)

    return score_ai - score_opponent  

    # Não apagar esse código comentado, será util para testes
    # logging.info("Calculate Score")
    # score_ai =  0
    # score_ai1 = 0
    # score_ai2 = 0
    # score_ai3 = 0
    # score_ai4 = 0
    # score_opponent = 0
    # score_opponent1 = 0
    # score_opponent2 = 0
    # score_opponent3 = 0
    # score_opponent4 = 0

    # score_ai1 += 1 * get_ocurrences(board, 1, ai_piece, row, column)
    # logging.info(f"Total score from 1 yellow ocurrences (1 point each): {score_ai1}")

    # score_ai2 += 10 * get_ocurrences(board, 2, ai_piece, row, column)
    # logging.info(f"Total score from 2 yellow ocurrences (10 point each): {score_ai2}")

    # score_ai3 += 50 * get_ocurrences(board, 3, ai_piece, row, column)
    # logging.info(f"Total score from 3 yellow ocurrences (50 point each): {score_ai3}")

    # score_ai4 += 1000 * get_ocurrences(board, 4, ai_piece, row, column)
    # logging.info(f"Total score from 3 yellow ocurrences (1000 point each): {score_ai4}")

    # score_opponent1 += 1 * get_ocurrences(board, 1, opponent_piece, row, column)
    # logging.info(f"Total score from 1 red ocurrences (1 point each): {score_opponent1}")

    # score_opponent2 += 10 * get_ocurrences(board, 2, opponent_piece, row, column)
    # logging.info(f"Total score from 2 red ocurrences (10 point each): {score_opponent2}")

    # score_opponent3 += 50 * get_ocurrences(board, 3, opponent_piece, row, column)
    # logging.info(f"Total score from 3 red ocurrences (50 point each): {score_opponent3}")

    # score_opponent4 += 1000 * get_ocurrences(board, 4, opponent_piece, row, column)
    # logging.info(f"Total score from 4 red ocurrences (1000 point each): {score_opponent4}")

    # score_ai = score_ai1 + score_ai2 + score_ai3 + score_ai4
    # score_opponent = score_opponent1 + score_opponent2 + score_opponent3 + score_opponent4

    # logging.info(f"Total: {score_ai - score_opponent}")
    # logging.info(f"Coluna: {column}\n")

    # return score_ai - score_opponent 


def get_ocurrences(board: np.ndarray, reference_quantity: int, piece: int, row: int, column: int) -> int:
    occurrences = 0
    # Check horizontal
    for col in range(c.COLUMNS - 3):
        for r in range(c.ROWS):
            temp = 0
            sliding_window = [board[r][col + i] for i in range(4)]
            for board_piece in sliding_window:
                if board_piece == piece:
                    temp += 1
            if temp == reference_quantity:
                occurrences += 1

    # Check vertical
    for col in range(c.COLUMNS):
        for r in range(c.ROWS - 3):
            temp = 0
            sliding_window = [board[r + i][col] for i in range(4)]
            for board_piece in sliding_window:
                if board_piece == piece:
                    temp += 1
            if temp == reference_quantity:
                occurrences += 1

    # Check ascending diagonal
    for col in range(c.COLUMNS - 3):
        for r in range(c.ROWS - 3):
            temp = 0
            sliding_window = [board[r + i][col + i] for i in range(4)]
            for board_piece in sliding_window:
                if board_piece == piece:
                    temp += 1
            if temp == reference_quantity:
                occurrences += 1

    # Check descending diagonal
    for col in range(c.COLUMNS - 3):
        for row in range(3, c.ROWS):
            temp = 0
            sliding_window = [board[row - i][col + i] for i in range(4)]
            for board_piece in sliding_window:
                if board_piece == piece:
                    temp += 1
            if temp == reference_quantity:
                occurrences += 1
    return occurrences

# para implementar ainda
# def a_star_melhorado(board: np.ndarray, ai_piece: int, opponent_piece: int) -> int:
#     move_score = -10000
#     best_move = -1
#     for col in range(c.COLUMNS):
#         if not game.is_valid(board, col): continue
#         board_copy = board.copy()
#         cur_score = 0
#         row = game.get_next_open_row(board_copy, col)
#         # add peça no novo tabuleiro falso para cada coluna
#         # chamar a_star para o oponente e retornar aqui apenas com o tabuleiro que contenha a melhor peça jogada dele 
#         cur_score = calculate_score(board, row, col, ai_piece, opponent_piece)
#         if cur_score > move_score:
#             best_move = col
#             move_score = cur_score
#     return best_move


def alphabeta(board: np.ndarray, piece: int) -> int:
    return 0


def monte_carlo_tree_search(board: np.ndarray, piece: int) -> int:
    best_column = 0
    return best_column
