#!/usr/bin/env python3

"""
Python script to set bing image of the day as desktop wallpaper
OS: Ubuntu 16.04
Forked from: Anurag Rana
"""

import datetime
import json
import os
import subprocess
from shutil import which

import requests

IMAGE_PATH = "/home/alex/Imágenes/Wallpapers/bing/"

# get image url
response = requests.get(
    "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US")
image_data = json.loads(response.text)

image_url = image_data["images"][0]["url"]
image_url = image_url.split("&")[0]
full_image_url = "https://www.bing.com" + image_url

# image's name
image_name = datetime.date.today().strftime("%Y%m%d")
image_extension = image_url.split(".")[-1]
image_name = image_name + "." + image_extension
image_path = IMAGE_PATH + image_name

# download and save image
img_data = requests.get(full_image_url).content
with open(image_path, 'wb') as handler:
    handler.write(img_data)

try:
    os.environ["DISPLAY"] = ":1"
    a = subprocess.check_call([str(which("gsettings")),
                               "set",
                               "org.gnome.desktop.background",
                               "picture-uri",
                               "file://" + image_path])
    print(a)
except subprocess.CalledProcessError as e:
    print(e)
