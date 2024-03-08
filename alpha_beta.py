import numpy as np
import constants as c
import game_logic as game

def alpha_beta(board, piece, opponent_piece):
    return 0

def min_value(board: np.ndarray, depth: int, alpha: int, beta: int):
    min_eval = float('+inf')
    childrens = get_childrens(board, c.HUMAN_PIECE)
    for move in childrens:
        eval = max_value(move, depth-1, alpha, beta)
        min_eval = min(eval, min_eval)
        beta = min(beta, eval)
        if beta <= alpha: break
    return min_eval

def max_value(board, depth, alpha, beta):
    max_eval = float('-inf')
    childrens = get_childrens(board, c.AI_PIECE)
    for move in board:
        eval = min_value(move, depth-1, alpha, beta)
        max_eval = max(eval, max_eval)
        alpha = max(alpha, eval)
        if beta <= alpha: break
    return max_eval

def get_childrens(board: np.darray, piece: int) -> list:
    childrens = []
    for col in c.COLUMNS:
        copy_board = game.simulate_move(board, piece, col)
        childrens.append(copy_board)
    return childrens
