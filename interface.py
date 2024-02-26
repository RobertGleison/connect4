import pygame
import itertools
import sys
import constants as c
from board import Board
import game_logic as game

class Interface:

    def __init__(self) -> None:
        self.rows = c.ROWS
        self.columns = c.COLUMNS
        self.pixels = c.SQUARESIZE
        self.width = c.WIDTH
        self.height = c.HEIGHT
        self.rad = c.RADIUS
        self.size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Connect4")


    def start_game(self, bd: Board) -> None:
        pygame.init()
        self.draw_options_board()
        game_mode = self.choose_option()

        if game_mode != 0:
            bd.print_board()	# prints the current matrix to the terminal
            self.draw_board()    # draws the initial board on the screen
            pygame.display.update()
            self.play_game(bd, game_mode)


    def draw_options_board(self):
            self.screen.fill(c.BACKGROUND_COLOR)

            # Draw buttons (self.height/2 = 400)
            self.draw_button(self.height/2, 50, 300, 50, "Player vs Player")
            self.draw_button(self.height/2, 150, 300, 50, "Player vs IA (A*)")
            self.draw_button(self.height/2, 250, 300, 50, "Player vs IA (MCTS)")

    def draw_button(self, x: int, y: int, width: int, height: int, text: str) -> None:
        pygame.draw.rect(self.screen, c.SHADOW_COLOR, (x, y, width, height), 0, 30)
        font = pygame.font.SysFont("Monospace", 20, bold=True)

        text_surface = font.render(text, True, c.BUTTON_TEXT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.center = (x + width / 2, y + height / 2)
        self.screen.blit(text_surface, text_rect)

    def choose_option(self) -> int:
        while True:
            game_mode = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    
                    # Check if buttons are clicked
                    if (self.width/2 - 150) <= mouse_x <= (self.width/2 + 150) and 50 <= mouse_y <= 100:
                        print("Player vs Player selected")
                        game_mode = 1
                    elif (self.width/2 - 150) <= mouse_x <= (self.width/2 + 150) and 150 <= mouse_y <= 200:
                        print("Player vs IA (A*) selected")
                        game_mode = 2
                    elif (self.width/2 - 150) <= mouse_x <= (self.width/2 + 150) and 250 <= mouse_y <= 300:
                        print("Player vs IA (MCTS) selected")
                        game_mode = 3

            pygame.display.flip()

            if game_mode != 0:
                return game_mode


    def play_game(self, bd: Board, game_mode: int) -> None:
        board = bd.get_board()	# pieces matrix
        game_over = False

        turns = itertools.cycle([1, 2])  # iteration between turns (player 1 and player 2)
        turn = next(turns)

        myfont = pygame.font.SysFont("Monospace", 50, bold=True)
        
        while not game_over:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.screen, c.BACKGROUND_COLOR, (0,0, self.width, self.pixels-14))
                    posx = event.pos[0]
                    pygame.draw.circle(self.screen, c.PIECES_COLORS[turn], (posx, int(self.pixels/2)-7), self.rad)
                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:	
                    if game_mode == 1:
                        game_over = game.handle_human_move(bd, self, board, turn, myfont, event)

                    elif game_mode == 2:
                        if turn == 1:
                            game_over = game.handle_human_move(bd, self, board, turn, myfont, event)
                        game_over = game.handle_ia_move(2)
                        
                    elif game_mode == 3:
                        if turn == 1:
                            game_over = game.handle_human_move(bd, self, board, turn, myfont, event)
                        game_over = game.handle_ia_move(3)

                    turn = next(turns)
        pygame.time.wait(3500)


    def draw_board(self) -> None:
        self.screen.fill(c.BACKGROUND_COLOR)    # turns the background "background color"

        # draw the board and its shadow:
        shadow_coordinates = (2*self.pixels-10, self.pixels-10, self.columns*self.pixels+24, self.rows*self.pixels+24)
        board_coordinates = (2*self.pixels-10, self.pixels-10, self.columns*self.pixels+20, self.rows*self.pixels+20)
        pygame.draw.rect(self.screen, c.SHADOW_COLOR, shadow_coordinates, 0, 30)  # draws the shadow with rounded corners
        pygame.draw.rect(self.screen, c.BOARD_COLOR, board_coordinates, 0, 30)  # draws the board with rounded corners

        # draw the board empty spaces:
        for col in range(self.columns):
            for row in range(self.rows):
                center_of_circle = (int((col+5/2)*self.pixels), int((row+3/2)*self.pixels))
                pygame.draw.circle(self.screen, c.BACKGROUND_COLOR, center_of_circle, self.rad)
        pygame.display.update()     


    def draw_new_piece(self, row: int, col: int, piece: int) -> None:
        center_of_circle = (int(col*self.pixels+self.pixels/2), self.height-int(row*self.pixels+self.pixels/2))
        pygame.draw.circle(self.screen, c.PIECES_COLORS[piece], center_of_circle, self.rad)
