import numpy as np
import constants as c
import heuristics as h
import game_logic as game
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def alpha_beta(board):
    logging.info("Enter alpha beta")
    best_move = -1
    depth_limit = 3
    current_value = float('-inf')
    children = get_childrens(board, c.AI_PIECE)

    for i in (range(len(children))):
        score = min_value(board, 0, float('-inf'), float('+inf'), depth_limit, c.HUMAN_PIECE)
        logging.info(f"Score for root for column {i+1} = {score}")
        if score > current_value:
            current_value = score
            best_move = i
    return best_move


def max_value(board, depth, alpha, beta, depth_limit: int, piece: int):
    logging.info("Enter max_value")
    max_eval = float('-inf')
    childrens = get_childrens(board, c.AI_PIECE)

    if game.winning_move(board, piece) or depth == depth_limit:
        return h.calculate_board_score(board, c.HUMAN_PIECE, c.AI_PIECE)

    for move in childrens:
        eval = min_value(move, depth+1, alpha, beta, depth_limit, c.AI_PIECE)
        score = max(eval, max_eval)
        alpha = max(alpha, eval)
        if beta <= alpha: break
    logging.info(f"Score: {score}")
    return score


def min_value(board, depth: int, alpha: int, beta: int, depth_limit: int, piece: int):
    logging.info("Enter min_value")
    if game.winning_move(board, piece) or depth == depth_limit:
        return h.calculate_board_score(board, c.HUMAN_PIECE, c.AI_PIECE)
    logging.info("Passou to winning_move validations o min value")
    min_eval = float('+inf')
    childrens = get_childrens(board, c.HUMAN_PIECE)
    for move in childrens:
        eval = max_value(move, depth+1, alpha, beta, depth_limit, c.HUMAN_PIECE)
        score = min(eval, min_eval)
        beta = min(beta, eval)
        if beta <= alpha: break
    logging.info(f"Score: {score}")
    return score


def get_childrens(board, piece: int) -> list:
    childrens = []
    for col in range(c.COLUMNS):
        copy_board = game.simulate_move(board, piece, col)
        childrens.append(copy_board)
    return childrens
