# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:12:50 2020

@author: CrisO
"""

import csv
import os

os.chdir("pathxy") # Ordner mit CSV-Files, die
path = os.getcwd()
files = []
files = os.listdir(path)
flowerDict = {}
flowerVaseDict = {}

for file in files:
    with open(file, newline="") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            if(row["region_attributes"] == "flower"):
                flowerDict[row["filename"]] = file

            if(row["region_attributes"] == "flower vase"):
                flowerVaseDict[row["filename"]] = file

os.chdir("pathxy")
with open("flowers.csv", mode="w") as flower_file:
    fieldnames = ["image_file", "dataset"]
    flower_writer = csv.DictWriter(flower_file, fieldnames = fieldnames, delimiter=",", extrasaction="ignore")
    flower_writer.writeheader()

    for x, y in flowerDict.items():
        flower_writer.writerow({"image_file": x, "dataset": y})

with open("flowerVase.csv", mode="w") as flowerVase_file:
    fieldnames = ["image_file", "dataset"]
    flowerVase_writer = csv.DictWriter(flowerVase_file, fieldnames = fieldnames, delimiter=",", extrasaction="ignore")
    flowerVase_writer.writeheader()

    for x, y in flowerVaseDict.items():
        flowerVase_writer.writerow({"image_file": x, "dataset": y})
