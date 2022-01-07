import unittest
from typing import *

from graphlib import TraceNode, traced_bft, traced_dft
from tests.simple_graphs import SimpleBinaryGridGraph


class TestTraceableTraverser(unittest.TestCase):
    def test_traced_breadth_first_traverse_empty(self):
        positions = traced_bft(start=(0, 0), successors=SimpleBinaryGridGraph.always_empty_successor)
        self.assertTrue(isinstance(positions, Iterable))
        self.assertListEqual([
            TraceNode(value=(0, 0), steps=0, parent=None)
        ], list(positions))

    def test_traced_breadth_first_traverse(self):
        graph = SimpleBinaryGridGraph.from_integer_grid(
            [
                [1, 0, 0],
                [1, 1, 1],
                [0, 1, 1]
            ]
        )
        positions = traced_bft(start=(0, 0), successors=graph.grid_successor)
        self.assertTrue(isinstance(positions, Iterable))

        self._assert_positions([
            ((0, 0), 0, None),
            ((1, 0), 1, (0, 0)),
            ((1, 1), 2, (1, 0)),
            ((2, 1), 3, (1, 1)),
            ((1, 2), 3, (1, 1)),
            ((2, 2), 4, (2, 1))
        ], list(positions))

    def test_traced_depth_first_traverse_empty(self):
        positions = traced_dft(start=(0, 0), successors=SimpleBinaryGridGraph.always_empty_successor)
        self.assertTrue(isinstance(positions, Iterable))
        self.assertListEqual([
            TraceNode(value=(0, 0), steps=0, parent=None)
        ], list(positions))

    def test_traced_depth_first_traverse(self):
        graph = SimpleBinaryGridGraph.from_integer_grid(
            [
                [1, 0, 0],
                [1, 1, 1],
                [0, 1, 1]
            ]
        )
        positions = traced_dft(start=(0, 0), successors=graph.grid_successor)
        self.assertTrue(isinstance(positions, Iterable))

        self._assert_positions([
            ((0, 0), 0, None),
            ((1, 0), 1, (0, 0)),
            ((1, 1), 2, (1, 0)),
            ((1, 2), 3, (1, 1)),
            ((2, 2), 4, (1, 2)),
            ((2, 1), 5, (2, 2))
        ], list(positions))

    def _assert_positions(self, expected_positions_as_tuples: List[Tuple[SimpleBinaryGridGraph.Position, int,
                                                                         SimpleBinaryGridGraph.Position]],
                          actual_positions: List[TraceNode]):
        for i, (value, step, parent_value) in enumerate(expected_positions_as_tuples):
            self.assertEqual(value, actual_positions[i].value)
            self.assertEqual(step, actual_positions[i].steps)
            if i == 0:
                self.assertIsNone(actual_positions[i].parent)
            else:
                self.assertIsInstance(actual_positions[i].parent, TraceNode)
                self.assertEqual(parent_value, actual_positions[i].parent.value)
