import unittest

from graphlib import bfs, TraceNode
from tests.simple_graphs import SimpleDictGraph


class TestSearch(unittest.TestCase):
    def test_bfs_empty_graph_goal_not_found(self):
        graph = SimpleDictGraph({
            "usa": []
        })
        goal = bfs(start="usa", goal="mexico", successors=graph.successors)
        self.assertIsNone(goal)

    def test_bfs_goal_not_found(self):
        graph = SimpleDictGraph({
            "usa": ["canada", "mexico", "cuba"],
            "canada": ["usa", "greenland"],
            "mexico": ["guatemala", "brazil", "cuba", "honduras", "usa"],
            "england": ["scotland", "france", "spain"]
        })
        goal = bfs(start="usa", goal="france", successors=graph.successors)
        self.assertIsNone(goal)

    def test_bfs_goal_found(self):
        graph = SimpleDictGraph({
            "usa": ["canada", "mexico", "cuba"],
            "canada": ["usa", "greenland"],
            "mexico": ["guatemala", "brazil", "cuba", "honduras", "usa"],
            "england": ["scotland", "france", "spain"]
        })
        goal: TraceNode = bfs(start="usa", goal="brazil", successors=graph.successors)

        self.assertEqual("brazil", goal.value)
        self.assertEqual(2, goal.steps)
        self.assertEqual("mexico", goal.parent.value)
        self.assertEqual("usa", goal.parent.parent.value)
        self.assertIsNone(goal.parent.parent.parent)
