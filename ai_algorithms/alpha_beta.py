from game import constants as c
from heuristics import heuristics as h
from game import game_logic as game
import time
import logging

#O tempo de resposta está compatível com o trabalho do matheus. No começo demora próximo de 1 segundo, mas depois passa a ser 0.5 segundos ou 0.3 segundos
NODES_VISITED = 1
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def alpha_beta(board):
    start_time = time.time()
    global NODES_VISITED
    NODES_VISITED = 1
    best_score = float('-inf')
    best_move = -1
    depth_limit = 5
    children = get_children(board, c.AI_PIECE)

    for col in range(c.COLUMNS):
        child_board = children[col]
        if not game.is_valid(child_board, col): continue
        current_score = min_value(child_board, 0, float('-inf'), float('+inf'), depth_limit, c.HUMAN_PIECE)
        if current_score > best_score:
            best_move = col
            best_score = current_score
        # logging.info(f"Number of nodes visited = {NODES_VISITED}")
        # logging.info(f"Score = {best_score}")
    end_time = time.time()
    logging.info(f"Tempo de resposta = {end_time-start_time}")
    return best_move


def max_value(board, depth, alpha, beta, depth_limit: int, piece: int):
    max_eval = float('-inf')
    childrens = get_children(board, c.AI_PIECE)

    if game.winning_move(board, piece) or depth == depth_limit:
        return h.calculate_board_score(board, c.HUMAN_PIECE, c.AI_PIECE)

    for move in childrens:
        score = min_value(move, depth+1, alpha, beta, depth_limit, c.AI_PIECE)
        global NODES_VISITED
        NODES_VISITED+=1
        score = max(score, max_eval)
        alpha = max(alpha, score)
        if beta <= alpha: break
    # logging.info(f"Score: {score}")
    return score


def min_value(board, depth: int, alpha: int, beta: int, depth_limit: int, piece: int):
    if game.winning_move(board, piece) or depth == depth_limit:
        return h.calculate_board_score(board, c.HUMAN_PIECE, c.AI_PIECE)
    min_eval = float('+inf')
    childrens = get_children(board, c.HUMAN_PIECE)
    for move in childrens:
        score = max_value(move, depth+1, alpha, beta, depth_limit, c.HUMAN_PIECE)
        global NODES_VISITED
        NODES_VISITED+=1
        score = min(score, min_eval)
        beta = min(beta, score)
        if beta <= alpha: break
    # logging.info(f"Score: {score}")
    return score


def get_children(board, piece: int) -> list:
    childrens = []
    for col in range(c.COLUMNS):
        copy_board = game.simulate_move(board, piece, col)
        childrens.append(copy_board)
    return childrens
