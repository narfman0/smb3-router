import unittest
from smb3_router.main import compute


class TestMain(unittest.TestCase):
    def test_compute(self):
        compute()
