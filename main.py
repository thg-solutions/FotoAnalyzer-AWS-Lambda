import fn
import exif
from pymongo import MongoClient
from PIL import Image as img
from PIL.ExifTags import Base

directory = "directory"

#files = glob.glob(directory)

filename = "20231029_141414.jpg"
file = "/home/tom/Bilder/Uwe_und_Familie.jpg"

x = fn.is_valid_File(filename)
imagedata = exif.get_image_data(file)
imagedata['filename'] = file
print(imagedata)

# myclient = MongoClient("mongodb://localhost:27017/")
# mydb = myclient["pythontest"]
# mycol = mydb["image"]
# #mycol.insert_one(imagedata)
# for i in mycol.find():
#     print(i)

# image = img.open(file)
# exif = image.getexif()
# for i in Base:
#     if i.value in exif.keys():
#         print(i, exif[i])
# print(exif[Base.Model])

