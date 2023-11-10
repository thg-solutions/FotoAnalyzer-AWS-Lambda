import unittest
from exif import get_image_data
from datetime import datetime

class ExifTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.imagedata = get_image_data("/home/tom/Bilder/Uwe_und_Familie.jpg")

    def test_creationdate(self):
        dt = self.imagedata.get('creationDate')
        self.assertIsInstance(dt, datetime)
        if isinstance(dt, datetime):
            self.assertRegex(dt.strftime('%Y%m%d_%H%M%S'), '\\d{8}_\\d{6}')

    def test_gps_location(self):
        latitude = self.imagedata.get('latitude')
        longitude = self.imagedata.get('longitude')
        self.assertIsInstance(latitude, float)
        self.assertIsInstance(longitude, float)
