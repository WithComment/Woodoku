import numpy as np

from woodoku.tiles import all_tiles


class Game:

  # Class attribute
  # Instance attributes
  w: int
  h: int
  board: np.ndarray
  points: int
  tile_queue: list[np.ndarray]

  def __init__(
      self,
      w: int = 9,
      h: int = 9
  ):
    self.w, self.h = w, h
    self.board = np.zeros((w, h), dtype=np.int8)
    self.points = 0
    self.tile_queue = []
