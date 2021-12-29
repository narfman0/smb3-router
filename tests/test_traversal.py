import unittest

from smb3_router.parser import parse
from smb3_router.timing import frames_to_duration_string
from smb3_router.traversal import compute_path


class TestTraversal(unittest.TestCase):
    def test_compute_path(self):
        graph = parse()
        cost, path = compute_path(graph)
        self.assertEqual(67, len(path))
        self.assertEqual(166349, cost)
        print(f"Time: {frames_to_duration_string(cost)}")
