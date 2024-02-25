import pygame
import sys
import constants as c

class OptionsBoard:
    
    def __init__(self):
        self.width = c.WIDTH
        self.height = c.HEIGHT
        self.size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size)

    def draw_button(self, x, y, width, height, text):
        pygame.draw.rect(self.screen, c.SHADOW_COLOR, (x, y, width, height), 0, 30)
        font = pygame.font.SysFont("Monospace", 20, bold=True)

        text_surface = font.render(text, True, c.BUTTON_TEXT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.center = (x + width / 2, y + height / 2)
        self.screen.blit(text_surface, text_rect)

    def draw_options_board(self):

        while True:
            game_mode = 0
            self.screen.fill(c.BACKGROUND_COLOR)

            # Draw buttons (self.height/2 = 400)
            self.draw_button(self.height/2, 50, 300, 50, "Player vs Player")
            self.draw_button(self.height/2, 150, 300, 50, "Player vs IA (A*)")
            self.draw_button(self.height/2, 250, 300, 50, "Player vs IA (MCTS)")

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