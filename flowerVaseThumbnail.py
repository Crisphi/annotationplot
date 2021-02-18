# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:48:47 2020

@author: CrisO
"""

import os
from PIL import Image

os.chdir("pathxy")

path = os.getcwd()
files = []
files = os.listdir(path)

size= (150,200)
thumbnails = []

for file in files:
    image = Image.open(file)
    img = image.resize(size)
    thumbnails.append(img)

os.chdir("pathxy")
for i in range(len(thumbnails)):
    thumbnails[i].save(str(i) + "_thumbnail.jpeg")
