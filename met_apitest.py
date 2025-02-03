import pathlib

import requests
from PIL import Image
import os

object_id_input = input("Put in your object ID: ")

endpoint = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/{}'.format(object_id_input)

response = requests.get(endpoint)

print(response)

art = response.json()

print(art['title'])
print(art['primaryImageSmall'])

#for getting image from a url

#storing file name and saving picture
pictureFile =art['title']+'.jpg'
img_data = requests.get(art['primaryImageSmall']).content
with open(pictureFile, 'wb') as handler:
     handler.write(img_data)

directory_name = str(pathlib.Path().absolute())
print(directory_name)

image_file_path=directory_name + "/" + pictureFile
print(image_file_path)

#source: https://www.youtube.com/watch?v=v_raWlX7tZY
#defining characters

ascii_chars= ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=10)

def main():
     try:
          image=PIL.Image.open(image_file_path)
     except:
          print("something went wrong")

