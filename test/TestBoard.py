import unittest

import numpy as np

from woodoku.Board import Board
from woodoku import tiles


class TestBoard(unittest.TestCase):

  def setUp(self) -> None:
    self.board = Board((3, 3))

  def test_place_tile(self) -> None:
    actual = self.board.place_tile(tiles.Z, (1, 0))
    expected = np.pad(tiles.Z, ((1, 0), (0, 0)))

    self.assertTrue((actual == expected).all())

  def test_pad_tile(self) -> None:
    tile = tiles.O_1

    actual = self.board.pad_tile(tile)
    expected = self.board.place_tile(tile)

    self.assertEqual(actual.shape, expected.shape)
    self.assertEqual(actual.sum(), expected.sum())

  def test_overlaps_true(self) -> None:
    self.board.place_tile(tiles.T_3)
    self.assertTrue(self.board.overlaps(tiles.D_3))

  def test_overlaps_false(self) -> None:
    self.board.place_tile(tiles.T_2)
    tile = self.board.pad_tile(tiles.L_2, 1)
    self.assertFalse(self.board.overlaps(tile))

  def test_can_fit_true(self) -> None:
    self.board.place_tile(tiles.D_3)
    self.assertTrue(self.board.can_fit(tiles.L_2))

  def test_can_fit_false(self) -> None:
    self.board.place_tile(tiles.T_3)
    self.assertFalse(self.board.can_fit(tiles.L_2))
