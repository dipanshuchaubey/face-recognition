import face_recognition
from PIL import Image, ImageDraw
import requests
import json
import base64

url = "http://192.168.43.169:5000/api/tooling/tools/product_insert"

def getImages(images):
    payload = {'image': f"{images}"}
    headers = {'content-type': 'application/json'}
    requests.post(url = 'http://192.168.43.169:5000/api/tooling/tools/face_recog', data = json.dumps(payload), headers=headers)

def getContent(data):
    print(data)

with open('./img/known/Bill Gates.jpg', "rb") as image_file:
    image = base64.b64encode(image_file.read())

# r = requests.get(url)
# print (r.status_code)

getImages(image)
