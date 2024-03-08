import numpy as np
from game import constants as c
from heuristics import heuristics as h
from game import game_logic as game
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def alpha_beta(board):
    best_score = float('-inf')
    best_move = -1
    depth_limit = 3
    children = get_childrens(board, c.AI_PIECE)
    for col in (range(c.COLUMNS)):
        if not game.is_valid(board, col): continue
        current_score = min_value(board, 0, float('-inf'), float('+inf'), depth_limit, c.HUMAN_PIECE)
        logging.info(f"Score for root for column {col+1} = {current_score}")
        if current_score > best_score:
            best_move = col
            best_score = current_score
    return best_move


def max_value(board, depth, alpha, beta, depth_limit: int, piece: int):
    logging.info("Enter max_value")
    max_eval = float('-inf')
    childrens = get_childrens(board, c.AI_PIECE)

    if game.winning_move(board, piece) or depth == depth_limit:
        return h.calculate_board_score(board, c.HUMAN_PIECE, c.AI_PIECE)

    for move in childrens:
        score = min_value(move, depth+1, alpha, beta, depth_limit, c.AI_PIECE)
        score = max(score, max_eval)
        alpha = max(alpha, score)
        if beta <= alpha: break
    logging.info(f"Score: {score}")
    print("teste branch")
    return score


def min_value(board, depth: int, alpha: int, beta: int, depth_limit: int, piece: int):
    logging.info("Enter min_value")
    if game.winning_move(board, piece) or depth == depth_limit:
        return h.calculate_board_score(board, c.HUMAN_PIECE, c.AI_PIECE)
    min_eval = float('+inf')
    childrens = get_childrens(board, c.HUMAN_PIECE)
    for move in childrens:
        score = max_value(move, depth+1, alpha, beta, depth_limit, c.HUMAN_PIECE)
        score = min(score, min_eval)
        beta = min(beta, score)
        if beta <= alpha: break
    logging.info(f"Score: {score}")
    return score


def get_childrens(board, piece: int) -> list:
    childrens = []
    for col in range(c.COLUMNS):
        copy_board = game.simulate_move(board, piece, col)
        childrens.append(copy_board)
    return childrens
