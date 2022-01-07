import unittest
from typing import *

from graphlib import untraced_bft, untraced_dft
from tests.simple_graphs import SimpleBinaryGridGraph


class TestUnTracedTraverser(unittest.TestCase):
    def test_untraced_bft_empty(self):
        positions = untraced_bft(start=(0, 0), successors=SimpleBinaryGridGraph.always_empty_successor)
        self.assertTrue(isinstance(positions, Iterable))
        self.assertListEqual([(0, 0)], list(positions))

    def test_untraced_bft(self):
        graph = SimpleBinaryGridGraph.from_integer_grid(
            [
                [1, 0, 0],
                [1, 1, 1],
                [0, 1, 1]
            ]
        )
        positions = untraced_bft(start=(0, 0), successors=graph.grid_successor)
        self.assertTrue(isinstance(positions, Iterable))
        self.assertListEqual([
            (0, 0),
            (1, 0),
            (1, 1),
            (2, 1),
            (1, 2),
            (2, 2)
        ], list(positions))

    def test_untraced_dft_empty(self):
        positions = untraced_dft(start=(0, 0), successors=SimpleBinaryGridGraph.always_empty_successor)
        self.assertTrue(isinstance(positions, Iterable))
        self.assertListEqual([(0, 0)], list(positions))

    def test_untraced_dft(self):
        graph = SimpleBinaryGridGraph.from_integer_grid(
            [
                [1, 0, 0],
                [1, 1, 1],
                [0, 1, 1]
            ]
        )
        positions = untraced_dft(start=(0, 0), successors=graph.grid_successor)
        self.assertTrue(isinstance(positions, Iterable))
        self.assertListEqual([
            (0, 0),
            (1, 0),
            (1, 1),
            (1, 2),
            (2, 2),
            (2, 1)
        ], list(positions))
