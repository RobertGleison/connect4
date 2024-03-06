import numpy as np
import constants as c 
import game_logic as game
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def greedy(board: np.ndarray, ai_piece: int, opponent_piece: int) -> int:
    best_score = float('-inf')
    best_move = -1
    for col in range(c.COLUMNS):
        if not game.is_valid(board, col): continue
        cur_score = 0
        simulated_board = simulate_move(board, ai_piece, col)
        cur_score = calculate_board_score(simulated_board, ai_piece, opponent_piece)
        if cur_score > best_score:
            best_move = col
            best_score = cur_score
    return best_move


def predictive_greedy(board: np.ndarray, ai_piece: int, opponent_piece: int) -> int:
    move_score = float('-inf')
    best_move = -1
    best_opponent = 0;
    for col in range(c.COLUMNS):
        if not game.is_valid(board, col): continue
        cur_score = 0
        simulated_board = simulate_move(board, ai_piece, col)

        opponent_col = greedy(simulated_board, opponent_piece, ai_piece)  
        opponent_simulated_board = simulate_move(simulated_board, opponent_piece, opponent_col)
        cur_score = calculate_board_score(opponent_simulated_board, ai_piece, opponent_piece)

        if cur_score > move_score:
            best_opponent = opponent_col + 1
            best_move = col
            move_score = cur_score
        
    print("Próximo passo sugerido: coluna " + str(best_opponent))
    return best_move


def simulate_move(board: np.ndarray, piece: int, col: int) -> np.ndarray:
    board_copy = board.copy()
    row = game.get_next_open_row(board_copy, col)
    game.drop_piece(board_copy, row, col, piece)
    return board_copy


def calculate_board_score(board: np.ndarray, piece: int, opponent_piece: int) -> int:
    score = 0

    # Check horizontal
    for col in range(c.COLUMNS - 3):
        for r in range(c.ROWS):
            segment = [board[r][col + i] for i in range(4)]
            score += count_cur(segment, piece, opponent_piece)

    # Check vertical
    for col in range(c.COLUMNS):
        for r in range(c.ROWS - 3):
            segment = [board[r + i][col] for i in range(4)]
            score += count_cur(segment, piece, opponent_piece)

    # Check ascending diagonal
    for col in range(c.COLUMNS - 3):
        for r in range(c.ROWS - 3):
            segment = [board[r + i][col + i] for i in range(4)]
            score += count_cur(segment, piece, opponent_piece)

    # Check descending diagonal
    for col in range(c.COLUMNS - 3):
        for r in range(3, c.ROWS):
            segment = [board[r - i][col + i] for i in range(4)]
            score += count_cur(segment, piece, opponent_piece)

    return score


def count_cur(segment: list, piece: int, opponent_piece: int) -> int:
    if piece in segment and opponent_piece in segment: return 0
    if segment.count(piece) == 1: return 1
    if segment.count(piece) == 2: return 10
    if segment.count(piece) == 3: return 50
    if segment.count(piece) == 4: return 1000
    if segment.count(opponent_piece) == 1: return -1
    if segment.count(opponent_piece) == 2: return -10
    if segment.count(opponent_piece) == 3: return -50
    if segment.count(opponent_piece) == 4: return -2000
    return 0

