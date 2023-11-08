import fn
import exif
from pymongo import MongoClient
from typing import Optional 
from fastapi import FastAPI, HTTPException, UploadFile, status
import glob, os, io
import os

app = FastAPI()

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["pythontest"]
mycol = mydb["image"]

@app.post("/rename_images")
def rename_images(directory_list: list[str], rename: Optional[bool] = None):
    images: list[str] = []
    result = []
    for i in directory_list:
        if not os.path.isdir(i):
            raise HTTPException(status_code = 422, detail = i + " is not a directory")
        images += glob.glob(i + '/*.jpg')
        images += glob.glob(i + '/*.JPG')
    for image in images:
        imagedata = exif.get_image_data(image)
        head, tail = os.path.split(image)
        if not fn.is_valid_File(tail) and imagedata.get('creationDate'):
            tail = fn.create_filename_from_datetime(imagedata.get('creationDate'))
            if rename:
                os.rename(image, os.path.join(head, tail))
        imagedata['filename'] = tail
        mycol.delete_one({'creationDate': imagedata.get('creationDate')})
        mycol.insert_one(imagedata.copy())
        result.append(imagedata)
    return result

@app.post("/analyze_image")
async def analyze_image(file: UploadFile):
    content = await file.read()
    result = exif.get_image_data(io.BytesIO(content))
    return result

