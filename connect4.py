import pygame
import sys
import math
from board import Board
from gameLogic import GameLogic
import colors

class Connect4:
    """Classe para criar a imagem da interface do tabuleiro"""
    

    def __init__(self, rows = 6, columns = 7):
        self.rows = rows
        self.columns = columns
        self.board = Board()
        self.game_over = False 
        self.turn = 0

    def print_board(self):
        print(self.board)

    def play_game(self):
        pygame.init()

        square_size = self.board.square_size
        width = self.board.width
        height = self.board.height
        radius = self.board.radius
        data = self.board.data
        size = (width, height)
        screen = pygame.display.set_mode(size)

        # self.board.draw_board(screen)

        # myfont = pygame.font.SysFont("monospace", 75)

        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, colors.WHITE, (0, 0, width, square_size))
                    posx = event.pos[0]
                    if self.turn == 0:
                        pygame.draw.circle(screen, colors.RED, (posx, int(square_size / 2)), radius)
                    else:
                        pygame.draw.circle(screen, colors.YELLOW, (posx, int(square_size / 2)), radius)
                    pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(screen, colors.WHITE, (0, 0, width, square_size))
                    posx = event.pos[0]
                    col = int(math.floor((posx + 2) / square_size))



                    ### NOTA: acho que dá pra resumir esses dois próximos blocos num só, tá tudo muito repetido aqui
                    if self.turn == 0:
                        if self.board.is_valid_location(col):
                            row = self.board.get_next_open_row(col) + 1
                            self.board.drop_piece(row, col, 1)
                            if GameLogic.winning_move(data, 1, self.rows, self.columns):
                                # label = myfont.render("Player 1 wins!!", 1, colors.RED)
                                # screen.blit(label, (40, 10))
                                self.game_over = True
                    else:
                        if self.board.is_valid_location(col):
                            row = self.board.get_next_open_row(col) + 1
                            self.board.drop_piece(row, col, 2)
                            if GameLogic.winning_move(data, 2, self.rows, self.columns):
                                # label = myfont.render("Player 2 wins!!", 1, colors.YELLOW)
                                # screen.blit(label, (40, 10))
                                self.game_over = True

                self.print_board()
                self.draw_board(data)

                self.turn += 1
                self.turn = self.turn % 2

                if self.game_over:
                    pygame.time.wait(3000)


    def draw_board(self, data):
        square_size = self.board.square_size
        width = self.board.width
        height = self.board.height
        radius = self.board.radius
        data = self.board.data
        size = (width, height)
        screen = pygame.display.set_mode(size)

        pygame.draw.rect(screen, colors.WHITE, (0, 0, width, height)) 		# cria fundo branco 
        pygame.draw.rect(screen, colors.GRAY, (2*square_size-10, square_size-10, self.columns*square_size+24, self.rows*square_size+24), 0, 30)
        pygame.draw.rect(screen, colors.BLUE, (2*square_size-10, square_size-10, self.columns*square_size+20, self.rows*square_size+20), 0, 30)		# cria colors.GRAYs azuis

        for c in range(self.columns):
            for r in range(self.rows):
                pygame.draw.circle(screen, colors.WHITE, (int(c*square_size+5*square_size/2), int(r*square_size+square_size+square_size/2)), radius) 	 # cria círculos (espaços)

    # 
    # for c in range(self.columns):
    #     for r in range(self.rows):		
    #         if data[r][c] == PLAYER_PIECE:
    #             pygame.draw.circle(screen, colors.RED, (int(c*square_size+square_size/2), height-int((r+3/2)*square_size)), radius)
    #         elif data[r][c] == AI_PIECE: 
    #             pygame.draw.circle(screen, colors.YELLOW, (int(c*square_size+square_size/2), height-int((r+3/2)*square_size)), radius)

    # VERSAO SEM IA     
        for c in range(self.columns):
            for r in range(self.rows):		
                if data[r][c] == 1:
                    pygame.draw.circle(screen, colors.RED, (int(c*square_size+square_size/2), height-int(r*square_size+square_size/2)), radius)
                elif data[r][c] == 2: 
                    pygame.draw.circle(screen, colors.YELLOW, (int(c*square_size+square_size/2), height-int(r*square_size+square_size/2)), radius)
        pygame.display.update()




