import constants as c
import numpy as np
import math
import pygame
import heuristics as h
from board import Board


def drop_piece(board: np.ndarray, row: int, col: int, piece: int):
	"""Insert a piece into board on correct location"""
	board[row][col] = piece


def is_valid_location(col: int):
	"""Analize if chose column is valid"""
	return col >= 0 and col < c.COLUMNS


def get_next_open_row(board: np.ndarray, col: int):
	"""Given a column, return the first row avaiable to set a piece"""
	for row in range(c.ROWS):
		if board[row][col] == 0:
			return row
		

def winning_move(board: np.ndarray, piece: int):
	"""Return if the selected move will win the game"""
	return check_vertical(board, piece) or check_horizontal(board, piece) or check_ascending_diagonal(board, piece) or check_descending_diagonal(board, piece)


def check_horizontal(board: np.ndarray, piece: int) -> bool:
	"""Check winning condition on horizontal lines"""
	for col in range(c.COLUMNS-3):
		for row in range(c.ROWS):
			if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
				return True
			

def check_vertical(board: np.ndarray, piece: int) -> bool:
	"""Check winning condition on vertical lines"""
	for col in range(c.COLUMNS):
		for row in range(c.ROWS-3):
			if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
				return True
			

def check_ascending_diagonal(board: np.ndarray, piece: int) -> bool:
	"""Check winning condition on ascending diagonal lines"""
	for col in range(c.COLUMNS-3):
		for row in range(c.ROWS-3):
			if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
				return True
			

def check_descending_diagonal(board: np.ndarray, piece: int) -> bool:
	"""Check winning condition on descending diagonal lines"""
	for col in range(c.COLUMNS-3):
		for row in range(3, c.ROWS):
			if board[row][col] == piece and board[row-1][col+1] == piece and board[row-2][col+2] == piece and board[row-3][col+3] == piece:
				return True
			

def hover_motion(interface: any, event: any):
	"""Print mouse hover animation"""
	pygame.draw.rect(interface.screen, c.BACKGROUND_COLOR, (0,0, interface.width, interface.pixels-14))
	posx = event.pos[0]
	return int(math.floor(posx/interface.pixels)) - 2


def show_winner(interface: any, myfont: any, turn: int) -> None:
	"""Print the winner"""
	label = myfont.render("Player " + str(turn) +" wins!", turn, c.PIECES_COLORS[turn])
	interface.screen.blit(label, (350,15))

def make_move(bd: Board, interface: any, board: np.ndarray, turn: int, myfont: any, move: int):
	game_over = False
	if is_valid_location(move):
		row = get_next_open_row(board, move)
		drop_piece(board, row, move, turn)	# adds the new piece to the data matrix
		interface.draw_new_piece(row+1, move+2, turn) 	# adds new piece to the screen

		if winning_move(board, turn):
			show_winner(interface, myfont, turn)
			game_over = True
		pygame.display.update()
		bd.print_board()
	return game_over

def human_move(bd: Board, interface: any, board: np.ndarray, turn: int, myfont: any, event: any) -> bool:
	"""Set the human move and see if this move won the game"""
	col = hover_motion(interface, event)
	game_over = make_move(bd, interface, board, turn, myfont, col)
	return game_over


def ai_move(bd: Board, interface: any, game_mode: int, board: np.ndarray, turn: int, myfont: any) -> int:
	"""Set the ai move and see if this move won the game"""
	ai_move = get_ai_move(bd, turn, game_mode)
	game_over = make_move(bd, interface, board, turn, myfont, ai_move)
	return game_over
	

def get_ai_move(board, piece, game_mode) -> int:
	"""Select the chose ai algorithm to make a move"""
	chose_column = 0
	if game_mode == 2:
		chose_column = h.a_star(board, piece)
	elif game_mode == 3:
		chose_column = h.monte_carlo_tree_search(board, piece)
	elif game_mode == 4:
		chose_column = h.alphabeta(board, piece)
	return chose_column


