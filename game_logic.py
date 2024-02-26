import constants as c
import numpy as np

def drop_piece(board: np.ndarray, row: int, col: int, piece: int):
	board[row][col] = piece

def is_valid_location(col: int):
	return col >= 0 and col < c.COLUMNS

def get_next_open_row(board: np.ndarray, col: int):
	for row in range(c.ROWS):
		if board[row][col] == 0:
			return row

def winning_move(board: np.ndarray, piece: int):
	# Check horizontal
	for col in range(c.COLUMNS-3):
		for row in range(c.ROWS):
			if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
				return True

	# Check vertical
	for col in range(c.COLUMNS):
		for row in range(c.ROWS-3):
			if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
				return True

	# Check ascending diagonal
	for col in range(c.COLUMNS-3):
		for row in range(c.ROWS-3):
			if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
				return True

	# Check descending diagonal
	for col in range(c.COLUMNS-3):
		for row in range(3, c.ROWS):
			if board[row][col] == piece and board[row-1][col+1] == piece and board[row-2][col+2] == piece and board[row-3][col+3] == piece:
				return True