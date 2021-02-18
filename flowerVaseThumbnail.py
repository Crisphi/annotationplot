# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:48:47 2020

@author: CrisO
"""

import os
from PIL import Image

os.chdir("pathxy") #change directory to folder where results from jsonReader_flowerVase-v2.py are stored

path = os.getcwd()
files = []
files = os.listdir(path) #get all filenames in folder as a list of strings

size= (150,200) #set size of thumbnail. I chose this size after some experimentation but one could choose other values
thumbnails = [] #initiate list for thumbnails

for file in files: #loop through all filenames in folder
    image = Image.open(file) #get image with current filename
    img = image.resize(size) #resize image with chosen values
    thumbnails.append(img) #save resized image in list

os.chdir("pathxy") #change directory to folder where you want to save the resized images (Replace with real path)
for i in range(len(thumbnails)): #loop through all resized pictures
    thumbnails[i].save(str(i) + "_thumbnail.jpeg") #save picture as jpeg
