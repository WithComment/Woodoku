import random
import pygame

from woodoku.tiles import shapes
from util import draw_grid, gen_shape

# Initialize Pygame
pygame.init()

# Set the dimension used in the game.
window_w = 800
window_h = 1200
board_d = 720
l_cell_d = board_d // 9
s_cell_d = board_d // 2

# Set the colors used in the game.
BLACK = pygame.color.Color(0, 0, 0, 255)
GRAY = pygame.color.Color(120, 120, 120, 255)
F_TILE = pygame.color.Color(250, 150, 33, 255)

# Create the Pygame window
window = pygame.display.set_mode((window_w, window_h))
pygame.display.set_caption('Woodoku')

# Create the clock used to cap FPS
FPS = 30
clock = pygame.time.Clock()

# Create the game board
board = pygame.surface.Surface((board_d + 1, board_d + 1))
draw_grid(board, color=GRAY)
window.blit(board, (40, 40))
pygame.display.flip()

# Main game loop
tile_queue = []
running = True
while running:
  # Handle events
  for event in pygame.event.get():
    match event.type:
      case pygame.QUIT:
        running = False
      
      case pygame.KEYUP:
        match event.key:
          case pygame.K_SPACE:
            shape = gen_shape(random.choice(shapes), l_cell_d)
            board.fill((0, 0, 0))
            board.blit(shape, (0, 0))
            draw_grid(board, color=(127, 127, 127))
            window.blit(board, (40, 40))

            # Update the display
            pygame.display.flip()
          
          case _:
            pass
      
      case _:
        pass

  # Cap max FPS
  clock.tick(FPS)

# Quit Pygame
pygame.quit() 
