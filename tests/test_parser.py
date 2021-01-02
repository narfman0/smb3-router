import unittest

from smb3_router.parser import frames_from_mssff, parse


class TestParser(unittest.TestCase):
    def test_parse(self):
        parse()

    def test_frames_from_mssff(self):
        self.assertEqual(45, frames_from_mssff("45"))
        self.assertEqual(1, frames_from_mssff("1"))
        self.assertEqual(120, frames_from_mssff("200"))
        self.assertEqual(3600, frames_from_mssff("10000"))
