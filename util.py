import numpy as np
import pygame


def draw_grid(
    surface: pygame.Surface,
    num_of_cells: int = 9,
    color: tuple = (255, 255, 255),
    line_width: int = 2,
) -> None:

  w = surface.get_width() - 1
  h = surface.get_height() - 1
  if w % num_of_cells != 0 or h % num_of_cells != 0:
    raise ValueError('The width and height of the surface must be a multiple of the number of cells.')

  cell_w = w // num_of_cells
  cell_h = h // num_of_cells

  for i in range(num_of_cells + 1):
    pygame.draw.line(
      surface, color,
      start_pos=(0, i * cell_h),
      end_pos=(w, i * cell_h),
      width=line_width
    )
    pygame.draw.line(
      surface, color,
      start_pos=(i * cell_w, 0),
      end_pos=(i * cell_w, h),
      width=line_width
    )


def gen_shape(
    shape: np.ndarray,
    cell_size: int
) -> pygame.surface.Surface:
  width = shape.shape[1] * cell_size
  height = shape.shape[0] * cell_size

  container = pygame.surface.Surface((width, height))

  empty = pygame.surface.Surface((cell_size, cell_size))
  empty.set_alpha(0)

  filled = pygame.surface.Surface((cell_size, cell_size))
  filled.fill((200, 150, 0))

  for i in range(shape.shape[0]):
    for j in range(shape.shape[1]):
      dest = (j * cell_size, i * cell_size)
      if shape[i, j]:
        container.blit(filled, dest)
      else:
        container.blit(empty, dest)
  
  return container

def draw_in_center(
    obj: pygame.surface.Surface,
    target: pygame.surface.Surface,
    hori: bool = True,
    vert: bool = False
) -> None:
  width = width