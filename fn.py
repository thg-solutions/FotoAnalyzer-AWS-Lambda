import re
from datetime import datetime

pattern = "\\d{8}_\\d{6}.jpg"

def is_valid_File(filename):
    '''checks if the given string matches the pattern of the desired filename'''
    return re.search(pattern, filename)

def create_filename_from_datetime(dt):
    '''transforms a datetime object into a filename'''
    return datetime.strftime(dt, '%Y%m%d_%H%M%S') + '.jpg'