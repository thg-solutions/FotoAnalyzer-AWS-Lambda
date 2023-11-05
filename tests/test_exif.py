import unittest
from exif import get_image_data
from datetime import datetime

class ExifTest(unittest.TestCase):

    def setUpClass(self):
        self.imagedata = get_image_data("/home/tom/Bilder/Uwe_und_Familie.jpg")

    def test_creationdate(self):
        dt = datetime.strptime(self.imagedata.get('creationDate'), '%Y-%m-%dT%H:%M:%S')
        self.assertIsInstance(dt, datetime)
        self.assertRegexpMatches(dt.strftime('%Y%m%d_%H%M%S'), '\\d{8}_\\d{6}')

    def test_gps_location(self):
        latitude = self.imagedata.get('latitude')
        longitude = self.imagedata.get('longitude')
        self.assertIsInstance(latitude, float)
        self.assertIsInstance(longitude, float)
