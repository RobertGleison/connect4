import numpy as np
import pygame
import sys
import math
import constants as c
import game_logic as game
from board import Board

def start_game(bd):
	pygame.init()
	rad = c.RADIUS
	myfont = pygame.font.SysFont("monospace", 75)
	game_over = False
	turn = 0
	

	board = bd.get_board()
	bd.print_board()
	bd.draw_board()
	pygame.display.update()

	while not game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEMOTION:
				pygame.draw.rect(bd.screen, c.BACKGORUND_COLOR, (0,0, bd.width, bd.pixels))
				posx = event.pos[0]
				if turn == 0:
					pygame.draw.circle(bd.screen, c.PLAYER_COLOR, (posx, int(bd.pixels/2)), rad)
				else: 
					pygame.draw.circle(bd.screen, c.IA_COLOR, (posx, int(bd.pixels/2)), rad)
			pygame.display.update()

			if event.type == pygame.MOUSEBUTTONDOWN:
				pygame.draw.rect(bd.screen, c.BACKGORUND_COLOR, (0,0, bd.width, bd.pixels))
				posx = event.pos[0]
				col = int(math.floor(posx/bd.pixels))
				if game.is_valid_location(board, col):
					row = game.get_next_open_row(board, col)
					if turn == 0:
						game.drop_piece(board, row, col, 1)
						if game.winning_move(board, 1):
							label = myfont.render("Player 1 wins!!", 1, c.PLAYER_COLOR)
							bd.screen.blit(label, (40,10))
							game_over = True


					# # Ask for Player 2 Input
					else:				
						game.drop_piece(board, row, col, 2)
						if game.winning_move(board, 2):
							label = myfont.render("Player 2 wins!!", 1, c.IA_COLOR)
							bd.screen.blit(label, (40,10))
							game_over = True

					bd.print_board()
					bd.draw_board()

					turn += 1
					turn = turn % 2

					if game_over:
						pygame.time.wait(3000)
