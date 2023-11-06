import fn
import exif
from pymongo import MongoClient
import glob
import os

filename = "20231029_141414.jpg"
file = "/home/tom/Bilder/Uwe_und_Familie.jpg"

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["pythontest"]
mycol = mydb["image"]

x = fn.is_valid_File(filename)
imagedata = exif.get_image_data('/home/tom/Bilder/Test/20160126_081152.jpg')
imagedata['filename'] = file

def rename_images(directory_list: list[str]):
    images: list[str] = []
    result = []
    for i in directory_list:
        images += glob.glob(i + '/*.jpg')
        images += glob.glob(i + '/*.JPG')
    for image in images:
        imagedata = exif.get_image_data(image)
        head, tail = os.path.split(image)
        if not fn.is_valid_File(tail):
            tail = fn.create_filename_from_datetime(imagedata.get('creationDate'))
            os.rename(image, os.path.join(head, tail))
        imagedata['filename'] = tail
        mycol.delete_one({'creationDate': imagedata.get('creationDate')})
        mycol.insert_one(imagedata)
        result.append(imagedata)
    return result

imagedatalist = rename_images(['/home/tom/Bilder/Gardasee_2 (Kopie)'])
