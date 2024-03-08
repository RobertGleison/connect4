import numpy as np
import constants as c
import heuristics as h
import game_logic as game

def alpha_beta(board):
    best_move = -1
    depth = 5
    current_value = float('-inf')
    children = get_childrens(board, c.AI_PIECE)

    for i in (range(len(children))):
        if(h.calculate_board_score(children[i],c.HUMAN_PIECE, c.AI_PIECE) == 512):
            return children[i]
        score = max_value(board, depth, float('-inf'), float('+inf'), depth, c.HUMAN_PIECE)
        if score > current_value:
            current_value = score
            best_move = i
    return best_move


def max_value(board, depth, alpha, beta, depth_limit: int, piece: int):
    if game.winning_move(board, piece) or depth == depth_limit:
        return h.calculate_board_score(board, c.HUMAN_PIECE, c.AI_PIECE)

    max_eval = float('-inf')
    childrens = get_childrens(board, c.AI_PIECE)
    for move in childrens:
        eval = min_value(move, depth-1, alpha, beta, c.AI_PIECE)
        score = max(eval, max_eval)
        alpha = max(alpha, eval)
        if beta <= alpha: break
    return score


def min_value(board, depth: int, alpha: int, beta: int, depth_limit: int, piece: int):
    if game.winning_move(board, piece) or depth == depth_limit:
        return h.calculate_board_score(board, c.HUMAN_PIECE, c.AI_PIECE)

    min_eval = float('+inf')
    childrens = get_childrens(board, c.HUMAN_PIECE)
    for move in childrens:
        eval = max_value(move, depth-1, alpha, beta, c.HUMAN_PIECE)
        score = min(eval, min_eval)
        beta = min(beta, eval)
        if beta <= alpha: break
    return score


def get_childrens(board, piece: int) -> list:
    childrens = []
    for col in range(c.COLUMNS):
        copy_board = game.simulate_move(board, piece, col)
        childrens.append(copy_board)
    return childrens
