import unittest
from smb3_router.smb3_router import logic


class TestSMB3Router(unittest.TestCase):
    def test_logic(self):
        self.assertEqual("Hello World!", logic())
