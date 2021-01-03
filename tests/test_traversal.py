import unittest

from smb3_router.parser import parse
from smb3_router.traversal import compute_path


class TestTraversal(unittest.TestCase):
    def test_compute_path(self):
        graph = parse()
        cost, path = compute_path(graph.nodes)
        self.assertEqual(69, len(path))
        self.assertEqual(180911, cost)
