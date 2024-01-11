import numpy as np

from Tiles import shapes

class Game:

  board: np.ndarray
  points: int
  tile_queue: list[np.ndarray]

  def __init__(self):
    self.board = np.zeros((9, 9), dtype=np.int8)
    self.points = 0
    self.tile_queue = []

  
  def gen_shapes(self):
    '''
    Generate three new tiles, one of which is guaranteed to fit
    on the board.
    '''
    all_shapes = shapes.copy()
    np.random.shuffle(all_shapes)
    