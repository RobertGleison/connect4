import pygame 
import itertools
import sys
import constants as c
from board import Board
import game_logic as game
from dataclasses import dataclass
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


@dataclass
class Interface:
    rows: int = c.ROWS
    columns: int = c.COLUMNS
    pixels: int = c.SQUARESIZE
    width: int = c.WIDTH
    height: int = c.HEIGHT
    rad: float = c.RADIUS
    size: tuple = (width, height)
    screen: any = pygame.display.set_mode(size)
    pygame.display.set_caption("Connect4")


    def start_game(self, bd: Board) -> None:
        """Set up the conditions to the game, like choose game_mode and draw the pygame display"""
        pygame.init()
        self.draw_options_board()
        game_mode = self.choose_option()
        if game_mode != 0:
            bd.print_board()	
            self.draw_board()    
            pygame.display.update()
            self.play_game(bd, game_mode)

    def play_game(self, bd: Board, game_mode: int) -> None:
        """Run the game"""
        board = bd.get_board()	
        game_over = False
        myfont = pygame.font.SysFont("Monospace", 50, bold=True)
        turns = itertools.cycle([1, 2])  
        turn = next(turns)
        
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: quit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.screen, c.BACKGROUND_COLOR, (0,0, self.width, self.pixels-14))
                    posx = event.pos[0]
                    pygame.draw.circle(self.screen, c.PIECES_COLORS[turn], (posx, int(self.pixels/2)-7), self.rad)
                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:	
                    if turn == 1 or (turn == 2 and game_mode == 1):
                        game_over = game.human_move(bd, self, board, turn, myfont, event)
                        turn = next(turns)
                        if game_over:
                            break
                        continue

                if turn != 1 and game_mode != 1: 
                    game_over = game.ai_move(bd, self, game_mode, board, turn, myfont)
                    pygame.time.wait(1)                    
                    turn = next(turns)
        pygame.time.wait(2000)


    def draw_board(self) -> None:
        """Draw pygame board display"""
        self.screen.fill(c.BACKGROUND_COLOR)    

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


    def draw_options_board(self):
        """Draw the option board: player x player and player x IA"""
        self.screen.fill(c.BACKGROUND_COLOR)
        font = pygame.font.Font("./fonts/04B_30__.TTF", 60)
        text_surface = font.render("Connect 4", True, c.BUTTON_TEXT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.center = (560, 230)
        self.screen.blit(text_surface, text_rect)
        self.draw_button(self.height/2, 350, 300, 50, "Player x Player")
        self.draw_button(self.height/2, 450, 300, 50, "Player x IA")


    def draw_algorithms(self):
        self.screen.fill(c.BACKGROUND_COLOR)
        self.draw_button(self.height/2, 250, 300, 50, "A*")
        self.draw_button(self.height/2, 350, 300, 50, "MCTS")
        self.draw_button(self.height/2, 450, 300, 50, "Alpha Beta")

            
    def draw_new_piece(self, row: int, col: int, piece: int) -> None:
        center_of_circle = (int(col*self.pixels+self.pixels/2), self.height-int(row*self.pixels+self.pixels/2))
        pygame.draw.circle(self.screen, c.PIECES_COLORS[piece], center_of_circle, self.rad)


    def draw_button(self, x: int, y: int, width: int, height: int, text: str) -> None:
        """Draw the option buttons"""
        pygame.draw.rect(self.screen, c.SHADOW_COLOR, (x, y, width, height), 0, 30)
        font = pygame.font.Font("./fonts/Minecraft.ttf", 25)
        text_surface = font.render(text, True, c.BUTTON_TEXT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.center = (x + width / 2, y + height / 2)
        self.screen.blit(text_surface, text_rect)


    def choose_ai_option(self) -> int:
        """Draw the ai option board: A*, MCTS, Alpha Beta"""
        while True:
            game_mode = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT: quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if (self.width / 2 - 150) <= mouse_x <= (self.width / 2 + 150) and 250 <= mouse_y <= 300:
                        print("A*")
                        game_mode = 2
                    elif (self.width / 2 - 150) <= mouse_x <= (self.width / 2 + 150) and 350 <= mouse_y <= 400:
                        print("MCTS")
                        game_mode = 3
                    elif (self.width / 2 - 150) <= mouse_x <= (self.width / 2 + 150) and 450 <= mouse_y <= 500:
                        print("Alpha Beta")
                        game_mode = 4

                pygame.display.flip()
                if game_mode != 0:
                    return game_mode


    def choose_option(self) -> int:
        while True:
            game_mode = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT: quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if (self.width/2 - 150) <= mouse_x <= (self.width/2 + 150) and 350 <= mouse_y <= 400:
                        print("Player vs Player selected")
                        game_mode = 1
                    elif (self.width/2 - 150) <= mouse_x <= (self.width/2 + 150) and 450 <= mouse_y <= 500:
                        print("Player vs IA selected")
                        self.draw_algorithms()
                        game_mode = 2

            pygame.display.flip()

            if game_mode == 1:
                return game_mode
            
            if game_mode == 2:
                game_mode = self.choose_ai_option()
                return game_mode


    def quit() -> None:
        pygame.quit()
        sys.exit()

