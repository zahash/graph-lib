import unittest
from typing import *

from graphlib import bft, dft
from tests.simple_graphs import SimpleBinaryGridGraph


class TestTraverser(unittest.TestCase):
    def test_breadth_first_traverse_empty(self):
        positions = bft(start=(0, 0), successors=SimpleBinaryGridGraph.always_empty_successor)
        self.assertTrue(isinstance(positions, Iterable))
        self.assertListEqual([(0, 0)], list(positions))

    def test_breadth_first_traverse(self):
        graph = SimpleBinaryGridGraph.from_integer_grid(
            [
                [1, 0, 0],
                [1, 1, 1],
                [0, 1, 1]
            ]
        )
        positions = bft(start=(0, 0), successors=graph.grid_successor)
        self.assertTrue(isinstance(positions, Iterable))
        self.assertListEqual([
            (0, 0),
            (1, 0),
            (1, 1),
            (2, 1),
            (1, 2),
            (2, 2)
        ], list(positions))

    def test_depth_first_traverse_empty(self):
        positions = dft(start=(0, 0), successors=SimpleBinaryGridGraph.always_empty_successor)
        self.assertTrue(isinstance(positions, Iterable))
        self.assertListEqual([(0, 0)], list(positions))

    def test_depth_first_traverse(self):
        graph = SimpleBinaryGridGraph.from_integer_grid(
            [
                [1, 0, 0],
                [1, 1, 1],
                [0, 1, 1]
            ]
        )
        positions = dft(start=(0, 0), successors=graph.grid_successor)
        self.assertTrue(isinstance(positions, Iterable))
        self.assertListEqual([
            (0, 0),
            (1, 0),
            (1, 1),
            (1, 2),
            (2, 2),
            (2, 1)
        ], list(positions))
