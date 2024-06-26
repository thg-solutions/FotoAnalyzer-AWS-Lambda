from PIL import Image as img
from PIL.ExifTags import IFD, Base, GPS
from datetime import datetime

class MissingExifDataException(Exception):
    pass

def get_exif_data(image):
    exif = image.getexif()
    if not exif.get(Base.DateTime):
        raise MissingExifDataException
    result = {}
    fields = { 'creationDate': Base.DateTime,
              'make': Base.Make,
              'model': Base.Model}
    for field in fields:
        value = fields.get(field)
        if value == Base.DateTime:
            result[field] = to_local_datetime(exif[value])
        else:
            result[field] = exif[value]

    return result

def get_gps_data(image):
    gps_ifd = image.getexif().get_ifd(IFD.GPSInfo)
    fields = { 'latitude': GPS.GPSLatitude, 'longitude': GPS.GPSLongitude}
    result = {}
    if gps_ifd != {}:
        for field in fields:
            result[field] = to_decimal_degrees(gps_ifd[fields.get(field)])
    return result

def to_decimal_degrees(x):
    return float((x[2]/60 + x[1])/60 + x[0])

def to_local_datetime(datestring):
    dt = datetime.strptime(datestring, '%Y:%m:%d %H:%M:%S')
    return dt
    
def get_image_data(file):
    result = {}
    image = img.open(file)
    try:
        result.update(get_exif_data(image))
        result.update(get_gps_data(image))
    except MissingExifDataException:
        result['image metadata'] = 'Not available'
    return result
