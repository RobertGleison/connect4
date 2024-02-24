import constants as c

def drop_piece(board, row, col, piece):
	board[row][col] = piece

def is_valid_location(board, col):
	return board[c.ROWS-1][col] == 0

def get_next_open_row(board, col):
	for row in range(c.ROWS):
		if board[row][col] == 0:
			return row

def winning_move(board, piece):
	# Checa horizontal
	for col in range(c.COLUMNS-3):
		for row in range(c.ROWS):
			if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
				return True

	# Checa vertical
	for col in range(c.COLUMNS):
		for row in range(c.ROWS-3):
			if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
				return True

	# Checa diagonal crescente
	for col in range(c.COLUMNS-3):
		for row in range(c.ROWS-3):
			if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
				return True

	# Checa diagonal decrescente
	for col in range(c.COLUMNS-3):
		for row in range(3, c.ROWS):
			if board[row][col] == piece and board[row-1][col+1] == piece and board[row-2][col+2] == piece and board[row-3][col+3] == piece:
				return True