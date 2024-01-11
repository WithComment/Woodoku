import numpy as np

class Board:

  board: np.ndarray

  def __init__(self) -> None:
    self.board = np.zeros((9, 9), dtype=np.int8)
  

  def place_tiles(
      self,
      tiles: 
  )