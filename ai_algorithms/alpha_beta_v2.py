# from game import constants as c
# from heuristics import heuristics as h
# from game import game_logic as game
# import logging


# def minimax(board, depth, alpha, beta, maximizingPlayer):
# 	valid_locations = get_valid_locations(board)
# 	is_terminal = is_terminal_node(board)
# 	if depth == 0 or is_terminal:
# 		if is_terminal:
# 			if winning_move(board, AI_PIECE):
# 				return (None, 100000000000000)
# 			elif winning_move(board, PLAYER_PIECE):
# 				return (None, -10000000000000)
# 			else: # Game is over, no more valid moves
# 				return (None, 0)
# 		else: # Depth is zero
# 			return (None, score_position(board, AI_PIECE))
# 	if maximizingPlayer: 
# 		return max_value(board, depth, alpha, beta, maximizingPlayer)
# 	return min_value(board, depth, alpha, beta, maximizingPlayer)
		
	
# def max_value(board, depth, alpha, beta, maximizingPlayer):
# 	value = float('-inf')
# 	column = random.choice(valid_locations)
# 	for col in valid_locations:
# 		row = get_next_open_row(board, col)
# 		b_copy = board.copy()
# 		drop_piece(b_copy, row, col, AI_PIECE)
# 		new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
# 		if new_score > value:
# 			value = new_score
# 			column = col
# 			alpha = max(alpha, value)
# 			if alpha >= beta:
# 				break
# 			return column, value
	
# def min_value(board, depth, alpha, beta, maximizingPlayer):
#     value = float('+inf')
#     column = random.choice(valid_locations)
#     for col in valid_locations:
#         row = get_next_open_row(board, col)
#         b_copy = board.copy()
#         drop_piece(b_copy, row, col, PLAYER_PIECE)
#         new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
#         if new_score < value:
#             value = new_score
#             column = col
#         beta = min(beta, value)
#         if alpha >= beta:
#             break
#     return column, value