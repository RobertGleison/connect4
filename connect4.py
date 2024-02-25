import numpy as np
import pygame
import sys
import math
import itertools
import constants as c
import game_logic as game

def start_game(bd, options_bd):
	pygame.init()
	game_mode = options_bd.draw_options_board()

	if game_mode != 0:
		bd.print_board()	# prints the current matrix to the terminal
		bd.draw_board()    # draws the initial board on the screen
		pygame.display.update()
		play_game(bd, game_mode)

'''@TODO: ATENÇÃO: teoricamente o play game roda indiferente do game mode pq eu n implementei nada, 
mas provavelmente vamos ter que fazer um if com as opçoes e codigos pra cada if'''

def play_game(bd, game_mode):
	print("enter play game")
	board = bd.get_board()	# pieces matrix
	rad = c.RADIUS
	game_over = False

	turns = itertools.cycle([1, 2])  # iteration between turns (player 1 and player 2)
	turn = next(turns)

	myfont = pygame.font.SysFont("Monospace", 50, bold=True)
	
	while not game_over:
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.MOUSEMOTION:
				pygame.draw.rect(bd.screen, c.BACKGROUND_COLOR, (0,0, bd.width, bd.pixels-14))
				posx = event.pos[0]
				pygame.draw.circle(bd.screen, c.PIECES_COLORS[turn], (posx, int(bd.pixels/2)-7), rad)
			pygame.display.update()

			if event.type == pygame.MOUSEBUTTONDOWN:
				pygame.draw.rect(bd.screen, c.BACKGROUND_COLOR, (0,0, bd.width, bd.pixels-14))
				posx = event.pos[0]
				col = int(math.floor(posx/bd.pixels)) - 2

				if game.is_valid_location(col):
					row = game.get_next_open_row(board, col)
					game.drop_piece(board, row, col, turn)	# adds the new piece to the data matrix
					
					bd.draw_new_piece(row+1, col+2, turn) 	# adds new piece to the screen
					if game.winning_move(board, turn):
						label = myfont.render("Player " + str(turn) +" wins!", 1, c.PIECES_COLORS[turn])
						bd.screen.blit(label, (350,15))
						game_over = True
						pygame.display.update()

					bd.print_board()
					turn = next(turns)

	pygame.time.wait(3500)
