# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:12:50 2020

@author: CrisO
"""

import csv
import os

os.chdir("pathxy") # Change directory to folder with files for each dataset with precalculated label mappings for each imagefile in the dataset (csv)
path = os.getcwd()
files = []
files = os.listdir(path) #get all filenames in folder as a list of strings
flowerDict = {} #dict for all files with flower annotations and their respective datasets
flowerVaseDict = {} #dict for all files with flower vase annotations and their respective datasets

for file in files: #loop through all filenames (one file for each dataset) in folder and open respective files
    with open(file, newline="") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader: #loop through all rows in csv file
            if(row["region_attributes"] == "flower"): #if flower is the region attribute save the filename entry of the current row and the respective current dataset
                flowerDict[row["filename"]] = file

            if(row["region_attributes"] == "flower vase"): #if flower  vase is the region attribute save the filename entry of the current row and the respective current dataset
                flowerVaseDict[row["filename"]] = file

os.chdir("pathxy") #change directory to folder where you want to save the output files
with open("flowers.csv", mode="w") as flower_file:#create a new csv to save the list of all files with flower labels and their respective datasets
    fieldnames = ["image_file", "dataset"] #set fieldnames of csv
    flower_writer = csv.DictWriter(flower_file, fieldnames = fieldnames, delimiter=",", extrasaction="ignore") #instantiate csv.DictWriter
    flower_writer.writeheader()

    for x, y in flowerDict.items(): #loop through all value-key pairs of flowerDict and write them in a new row of the csv file
        flower_writer.writerow({"image_file": x, "dataset": y})

with open("flowerVase.csv", mode="w") as flowerVase_file: #create a new csv to save the list of all files with flower vase labels and their respective datasets
    fieldnames = ["image_file", "dataset"] #set fieldnames of csv
    flowerVase_writer = csv.DictWriter(flowerVase_file, fieldnames = fieldnames, delimiter=",", extrasaction="ignore")  #instantiate csv.DictWriter
    flowerVase_writer.writeheader()

    for x, y in flowerVaseDict.items(): #loop through all value-key pairs of flowerVasDict and write them in a new row of the csv file
        flowerVase_writer.writerow({"image_file": x, "dataset": y})
