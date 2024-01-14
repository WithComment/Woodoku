import numpy as np
import doctest


class Board:

  w: int
  h: int
  board: np.ndarray

  def __init__(
      self,
      shape: tuple[int] = (9, 9),
      board: np.ndarray | None = None,
  ):
    if board is not None:
      self.h, self.w = board.shape
      self.board = board.copy()
    else:
      self.h, self.w = shape
      self.board = np.zeros(shape, dtype=np.int8)

  @property
  def shape(self) -> tuple:
    return self.board.shape

  def place_tile(
      self,
      tile: np.ndarray,
      top_left: tuple[int] = (0, 0)
  ) -> np.ndarray:
    '''
    Place the `tile` on the board
    '''
    top, left = top_left
    tile_h, tile_w = tile.shape
    bottom = top + tile_h
    right = left + tile_w

    if bottom > self.w or right > self.h:
      raise ValueError('The tile must be placed inside the board')

    self.board[top:bottom, left:right] += tile

    return self.board

  def pad_tile(
      self,
      tile: np.ndarray,
      top: int = 0,
      left: int = 0
  ) -> np.ndarray:
    '''
    Pad `tile` with `0`s and return a `np.ndarray` having the same 
    shape as `self.board`
    '''
    tile_h, tile_w = tile.shape

    padded = np.pad(
      tile,
      ((top, self.h - top - tile_h),
       (left, self.w - left - tile_w))
    )

    return padded

  def overlaps(
      self,
      tile: np.ndarray
  ) -> bool:
    '''
    Return `True` if `tile` overlaps with any existing tile on the 
    current board, `False` otherwise.

    Example
    -------
    >>> board = Board(board = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]]))
    >>> board.overlaps(np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]]))
    False
    >>> board.overlaps(np.array([[1, 0, 0], [1, 0, 0], [1, 0, 0]]))
    True
    '''
    return np.any(tile * self.board == 1)

  def can_fit(
      self,
      tile: np.ndarray
  ) -> bool:
    '''
    Return `True` if `tile` can fit on the current `board`.
    '''
    h_diff = self.h - tile.shape[0]
    w_diff = self.w - tile.shape[1]
    tile = self.pad_tile(tile)

    for i in range(h_diff + 1):
      for j in range(w_diff + 1):
        rolled = np.roll(tile, (i, j), axis=(0, 1))

        # Check if there isn't overlap between the tile and the board
        if not self.overlaps(rolled):
          return True

    return False


if __name__ == "__main__":
  doctest.testmod(verbose=True)
