import numpy as np
import constants as c 
import game_logic as game
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def a_star(board: np.ndarray, ai_piece: int, opponent_piece: int) -> int:
    debug = False


    best_score = -2000
    best_move = -1
    for col in range(c.COLUMNS):
        if not game.is_valid(board, col): continue
        cur_score = 0
        board_copy = board.copy()
        row = game.get_next_open_row(board_copy, col)
        game.drop_piece(board_copy, row, col, ai_piece)

        if debug: 
            print(np.flip(board_copy, 0))
            cur_score = calculate_score(board_copy, col, ai_piece, opponent_piece)
        else: 
            cur_score = curr_score(board_copy, ai_piece, opponent_piece)

        if cur_score > best_score:
            best_move = col
            best_score = cur_score
    return best_move

# função para debug
def calculate_score(board: np.ndarray, column: int, ai_piece: int, opponent_piece: int) -> int:
    # score_ai =  0
    # score_opponent = 0

    # score_ai += 1 * get_ocurrences(board, 1, ai_piece, opponent_piece)
    # score_ai += 10 * get_ocurrences(board, 2, ai_piece, opponent_piece)
    # score_ai += 50 * get_ocurrences(board, 3, ai_piece, opponent_piece)
    # score_ai += 1000 * get_ocurrences(board, 4, ai_piece, opponent_piece)

    # score_opponent += 1 * get_ocurrences(board, 1, opponent_piece, ai_piece)
    # score_opponent += 10 * get_ocurrences(board, 2, opponent_piece, ai_piece)
    # score_opponent += 50 * get_ocurrences(board, 3, opponent_piece, ai_piece)
    # score_opponent += 1000 * get_ocurrences(board, 4, opponent_piece, ai_piece)

    # return score_ai - score_opponent  

    # Não apagar esse código comentado, será util para testes
    logging.info("Calculate Score")

    ocurrences_ai1 = get_ocurrences(board, 1, ai_piece, opponent_piece)
    logging.info(f"Total score from 1 yellow ocurrences (1 point each): {ocurrences_ai1}")

    ocurrences_ai2 = get_ocurrences(board, 2, ai_piece, opponent_piece)
    logging.info(f"Total score from 2 yellow ocurrences (10 point each): {ocurrences_ai2}")

    ocurrences_ai3 = get_ocurrences(board, 3, ai_piece, opponent_piece)
    logging.info(f"Total score from 3 yellow ocurrences (50 point each): {ocurrences_ai3}")

    ocurrences_ai4 = get_ocurrences(board, 4, ai_piece, opponent_piece)
    logging.info(f"Total score from 3 yellow ocurrences (1000 point each): {ocurrences_ai4}")

    ocurrences_opponent1 = get_ocurrences(board, 1, opponent_piece, ai_piece)
    logging.info(f"Total score from 1 red ocurrences (1 point each): {ocurrences_opponent1}")

    ocurrences_opponent2 = get_ocurrences(board, 2, opponent_piece, ai_piece)
    logging.info(f"Total score from 2 red ocurrences (10 point each): {ocurrences_opponent2}")

    ocurrences_opponent3 = get_ocurrences(board, 3, opponent_piece, ai_piece)
    logging.info(f"Total score from 3 red ocurrences (50 point each): {ocurrences_opponent3}")

    # score_opponent4 += 1000 * get_ocurrences(board, 4, opponent_piece, ai_piece)
    # logging.info(f"Total score from 4 red ocurrences (1000 point each): {score_opponent4}")

    score_ai = ocurrences_ai1 + 10*ocurrences_ai2 + 50*ocurrences_ai3 + 1000*ocurrences_ai4
    score_opponent = ocurrences_opponent1 + 10*ocurrences_opponent2 + 50*ocurrences_opponent3

    logging.info(f"Total: {score_ai - score_opponent}")
    logging.info(f"Coluna: {column}\n")

    return score_ai - score_opponent 

# função para debug
def get_ocurrences(board: np.ndarray, reference_quantity: int, piece: int, opponent_piece: int) -> int:
    occurrences = 0
    # Check horizontal
    for col in range(c.COLUMNS - 3):
        for r in range(c.ROWS):
            # temp = 0
            sliding_window = [board[r][col + i] for i in range(4)]
            if piece in sliding_window and opponent_piece in sliding_window: continue
            if sliding_window.count(piece) == reference_quantity: occurrences += 1
            # for board_piece in sliding_window:
            #     if board_piece == piece:
            #         temp += 1
            # if temp == reference_quantity:
            #     occurrences += 1

    # Check vertical
    for col in range(c.COLUMNS):
        for r in range(c.ROWS - 3):
            # temp = 0
            sliding_window = [board[r + i][col] for i in range(4)]
            if piece in sliding_window and opponent_piece in sliding_window: continue
            if sliding_window.count(piece) == reference_quantity: occurrences += 1
            # for board_piece in sliding_window:
            #     if board_piece == piece:
            #         temp += 1
            # if temp == reference_quantity:
            #     occurrences += 1

    # Check ascending diagonal
    for col in range(c.COLUMNS - 3):
        for r in range(c.ROWS - 3):
            # temp = 0
            sliding_window = [board[r + i][col + i] for i in range(4)]
            if piece in sliding_window and opponent_piece in sliding_window: continue
            if sliding_window.count(piece) == reference_quantity: occurrences += 1
            # for board_piece in sliding_window:
            #     if board_piece == piece:
            #         temp += 1
            # if temp == reference_quantity:
            #     occurrences += 1

    # Check descending diagonal
    for col in range(c.COLUMNS - 3):
        for r in range(3, c.ROWS):
            # temp = 0
            sliding_window = [board[r - i][col + i] for i in range(4)]
            if piece in sliding_window and opponent_piece in sliding_window: continue
            if sliding_window.count(piece) == reference_quantity: occurrences += 1
            # for board_piece in sliding_window:
            #     if board_piece == piece:
            #         temp += 1
            # if temp == reference_quantity:
            #     occurrences += 1
    return occurrences


def curr_score(board: np.ndarray, piece: int, opponent_piece: int) -> int:
    score = 0

    # Check horizontal
    for col in range(c.COLUMNS - 3):
        for r in range(c.ROWS):
            sliding_window = [board[r][col + i] for i in range(4)]
            score += count_cur(sliding_window, piece, opponent_piece)

    # Check vertical
    for col in range(c.COLUMNS):
        for r in range(c.ROWS - 3):
            sliding_window = [board[r + i][col] for i in range(4)]
            score += count_cur(sliding_window, piece, opponent_piece)

    # Check ascending diagonal
    for col in range(c.COLUMNS - 3):
        for r in range(c.ROWS - 3):
            sliding_window = [board[r + i][col + i] for i in range(4)]
            score += count_cur(sliding_window, piece, opponent_piece)

    # Check descending diagonal
    for col in range(c.COLUMNS - 3):
        for r in range(3, c.ROWS):
            sliding_window = [board[r - i][col + i] for i in range(4)]
            score += count_cur(sliding_window, piece, opponent_piece)

    return score


# COMENTARIO PARA NOTEBOOK: scanear o quadro inteiro só uma vez
def count_cur(sliding_window: list, piece: int, opponent_piece: int) -> int:
    if piece in sliding_window and opponent_piece in sliding_window: return 0
    if sliding_window.count(piece) == 1: return 1
    if sliding_window.count(piece) == 2: return 10
    if sliding_window.count(piece) == 3: return 50
    if sliding_window.count(piece) == 4: return 1000
    if sliding_window.count(opponent_piece) == 1: return -1
    if sliding_window.count(opponent_piece) == 2: return -10
    if sliding_window.count(opponent_piece) == 3: return -50
    if sliding_window.count(opponent_piece) == 4: return -2000
    return 0


def a_star_adversarial(board: np.ndarray, ai_piece: int, opponent_piece: int) -> int:
    move_score = -2000
    best_move = -1
    best_opponent = 0;
    for col in range(c.COLUMNS):
        if not game.is_valid(board, col): continue
        board_copy = board.copy()
        cur_score = 0
        row = game.get_next_open_row(board_copy, col)
        game.drop_piece(board_copy, row, col, ai_piece)

        # supor a melhor jogada do oponente na próxima jogada
        opponent_col = a_star(board_copy, opponent_piece, ai_piece)  # melhor jogada do oponente se a IA jogar na posição atual
        opponent_row = game.get_next_open_row(board_copy, opponent_col)
        game.drop_piece(board_copy, opponent_row, opponent_col, 1) # chamar a_star para o oponente e retornar aqui apenas com o tabuleiro que contenha a melhor peça jogada dele 
        cur_score = curr_score(board_copy, ai_piece, opponent_piece)
        if cur_score > move_score:
            best_opponent = opponent_col + 1
            best_move = col
            move_score = cur_score
        
    print("Solução: coluna " + str(best_opponent))
    return best_move


def alphabeta(board: np.ndarray, piece: int) -> int:
    return 0


def monte_carlo_tree_search(board: np.ndarray, piece: int) -> int:
    best_column = 0
    return best_column
