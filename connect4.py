import numpy as np
import pygame
import sys
import math
import itertools
import constants as c
import game_logic as game
from board import Board

def start_game(bd):
	pygame.init()
	bd.print_board()	# prints the current matrix to the terminal
	bd.draw_board()    # draws the initial board on the screen
	pygame.display.update()
	play_game(bd)


def play_game(bd):
	board = bd.get_board()	# pieces matrix
	rad = c.RADIUS
	game_over = False

	turns = itertools.cycle([1, 2]) 	# iteration between turns (player 1 and player 2)
	turn = next(turns)

	myfont = pygame.font.SysFont("Monospace", 50)
	
	while not game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEMOTION:
				pygame.draw.rect(bd.screen, c.BACKGORUND_COLOR, (0,0, bd.width, bd.pixels-14))
				posx = event.pos[0]
				pygame.draw.circle(bd.screen, c.PIECES_COLORS[turn], (posx, int(bd.pixels/2)-7), rad)
			pygame.display.update()

			if event.type == pygame.MOUSEBUTTONDOWN:
				pygame.draw.rect(bd.screen, c.BACKGORUND_COLOR, (0,0, bd.width, bd.pixels-14))
				posx = event.pos[0]
				col = int(math.floor(posx/bd.pixels)) - 2
				if game.is_valid_location(board, col):
					row = game.get_next_open_row(board, col)
					game.drop_piece(board, row, col, turn)	# adds the new piece to the data matrix
					bd.draw_new_piece(row+1, col+2, turn) 	# adds new piece to the screen
					if game.winning_move(board, turn):
						label = myfont.render("Player " + str(turn) +" wins!!!", 1, c.PIECES_COLORS[turn])
						bd.screen.blit(label, (300,15))
						game_over = True
						pygame.display.update()

					bd.print_board()
					turn = next(turns)


	pygame.time.wait(3000)
