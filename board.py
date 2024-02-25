import numpy as np
import constants as c
import pygame 

class Board:
    def __init__(self) -> None:
        self.rows = c.ROWS
        self.columns = c.COLUMNS
        self.pixels = c.SQUARESIZE
        self.width = c.WIDTH
        self.height = c.HEIGHT
        self.size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Connect4")
        self.board = np.zeros((self.rows, self.columns))
            
    def get_board(self) -> np.ndarray:
        return self.board

    def print_board(self) -> None:
        print(np.flip(self.board, 0), "\n")
        
    def draw_board(self) -> None:
        rad = c.RADIUS

        self.screen.fill(c.BACKGROUND_COLOR)    # turns the background "background color"

        shadow_coordinates = (2*self.pixels-10, self.pixels-10, self.columns*self.pixels+24, self.rows*self.pixels+24)
        board_coordinates = (2*self.pixels-10, self.pixels-10, self.columns*self.pixels+20, self.rows*self.pixels+20)
        pygame.draw.rect(self.screen, c.SHADOW_COLOR, shadow_coordinates, 0, 30)  # draws the shadow with rounded corners
        pygame.draw.rect(self.screen, c.BOARD_COLOR, board_coordinates, 0, 30)  # draws the board with rounded corners

        # draw the board empty spaces:
        for col in range(self.columns):
            for row in range(self.rows):
                center_of_circle = (int((col+5/2)*self.pixels), int((row+3/2)*self.pixels))
                pygame.draw.circle(self.screen, c.BACKGROUND_COLOR, center_of_circle, rad)
        pygame.display.update()     

    def draw_new_piece(self, row: int, col: int, piece: int) -> None:
        center_of_circle = (int(col*self.pixels+self.pixels/2), self.height-int(row*self.pixels+self.pixels/2))
        pygame.draw.circle(self.screen, c.PIECES_COLORS[piece], center_of_circle, c.RADIUS)

        

    



        
