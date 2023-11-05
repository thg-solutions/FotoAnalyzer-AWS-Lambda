import unittest
from datetime import datetime
from fn import is_valid_File, create_filename_from_datetime

class FilenameTest(unittest.TestCase):
    def test_valid(self):
        x = is_valid_File("20231029_141414.jpg")
        self.assertIsNotNone(x)

    def test_isNotValid(self):
        x = is_valid_File("20231029141414.jpg")
        self.assertIsNone(x)

    def test_create_filename(self):
        dt = datetime(2023, 11, 2, 9, 57)
        filename = create_filename_from_datetime(dt)
        self.assertEquals(filename, '20231102_095700.jpg')