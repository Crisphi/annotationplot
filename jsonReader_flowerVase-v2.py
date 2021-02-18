# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 00:56:55 2020

@author: CrisO
"""
#import packages
import json
import csv
import os
from shapely.geometry import Polygon, LineString
from PIL import Image

#set up ditctionaries
metadataRelations = {
        "Ambrosiana_annotations.csv":"Ambrosiana_exported_finished_json.json" ,
        "Artstor_annotations.csv":"Artstor_exported_finished_json.json",
        "Ashmolean_annotations.csv":"Ashmolean_exported_finished_json.json",
        #"BeniCulturali_annotations.csv":"BeniCulturaliModified_exported_finished_json.json",
        "Boijmans_annotations.csv":"Bojimans_exported_finished_json.json",
        "British-Libraries_annotations.csv":"British_Libraries_exported_finished_json.json",
        "Cini_annotations.csv":"Cini_exported_finished_json.json",
        "Joconde_II_annotations.csv":"Joconde_exported_finished_json.json",
        "NGA_annotations.csv":"NGA_exported_finished_json.json",
        "RKD_annotations.csv":"RKD_exported_finished_json.json",
        "SLUB_annotations.csv":"SLUB_exported_finished_json.json",
        "STÄDEL_annotations.csv":"Staedel_exported_finished_json.json",
        "wga_annotations.csv":"wga_exported_finished_json.json"
        }

pictureRelations = {
        "Ambrosiana_annotations.csv": "Ambrosiana",
        "Artstor_annotations.csv":"Artstor",
        "Ashmolean_annotations.csv":"Ashmolean",
        #"BeniCulturali_annotations.csv":"BeniCulturali",
        "Boijmans_annotations.csv":"Boijmans",
        "British-Libraries_annotations.csv":"British Libraries",
        "Cini_annotations.csv":"Cini",
        "Joconde_II_annotations.csv":"Joconde_II",
        "NGA_annotations.csv":"_NGA",
        "RKD_annotations.csv":"RKD Auswahl",
        "SLUB_annotations.csv":"SLUB",
        "STÄDEL_annotations.csv":"Städel II",
        "wga_annotations.csv":"wga"
        }

datasetDict_flower = {
            "ambrosiana_flowers" : {"files": [], "csv_Metadata": "Ambrosiana_annotations.csv"},
            "artstor_flowers" : {"files": [], "csv_Metadata": "Artstor_annotations.csv"},
            "ashmolean_flowers" : {"files": [], "csv_Metadata": "Ashmolean_annotations.csv"},
            #"beniCulturali_flowers" : {"files": [], "csv_Metadata": "BeniCulturali_annotations.csv"},
            "boijmans_flowers" : {"files": [], "csv_Metadata": "Boijmans_annotations.csv"},
            "britishLibraries_flowers" : {"files": [], "csv_Metadata": "British-Libraries_annotations.csv"},
            "cini_flowers" : {"files": [], "csv_Metadata": "Cini_annotations.csv"},
            "joconde_flowers" : {"files": [], "csv_Metadata": "Joconde_II_annotations.csv"},
            "nga_flowers" : {"files": [], "csv_Metadata": "NGA_annotations.csv"},
            "rkd_flowers" : {"files": [], "csv_Metadata": "RKD_annotations.csv"},
            "slub_flowers" : {"files": [], "csv_Metadata": "SLUB_annotations.csv"},
            "staedel_flowers" : {"files": [], "csv_Metadata": "STÄDEL_annotations.csv"},
            "wga_flowers" : {"files": [], "csv_Metadata": "wga_annotations.csv"},
        }


os.chdir("pathxy")

#get all imagefiles, sort them according to associated dataset and save them in dict
with open("flowerVase.csv", newline="") as csvfile:
    flowers = csv.DictReader(csvfile, delimiter=",")
    for row in flowers:
        if(row["dataset"] == "Ambrosiana_annotations.csv"):
            datasetDict_flower["ambrosiana_flowers"]["files"].append({"filename": row["image_file"], "regions" :[]})
        elif(row["dataset"] == "Artstor_annotations.csv"):
            datasetDict_flower["artstor_flowers"]["files"].append({"filename":row["image_file"], "regions" :[]})
        elif(row["dataset"] == "Ashmolean_annotations.csv"):
            datasetDict_flower["ashmolean_flowers"]["files"].append({"filename":row["image_file"], "regions" :[]})
        #elif(row["dataset"] == "BeniCulturali_annotations.csv"):
           # datasetDict_flower["beniCulturali_flowers"]["files"].append({"filename":row["image_file"], "regions" :[]})
        elif(row["dataset"] == "Boijmans_annotations.csv"):
            datasetDict_flower["boijmans_flowers"]["files"].append({"filename":row["image_file"], "regions" :[]})
        elif(row["dataset"] == "British-Libraries_annotations.csv"):
            datasetDict_flower["britishLibraries_flowers"]["files"].append({"filename":row["image_file"], "regions" :[]})
        elif(row["dataset"] == "Cini_annotations.csv"):
            datasetDict_flower["cini_flowers"]["files"].append({"filename":row["image_file"], "regions" :[]})
        elif(row["dataset"] == "Joconde_II_annotations.csv"):
            datasetDict_flower["joconde_flowers"]["files"].append({"filename":row["image_file"], "regions" :[]})
        elif(row["dataset"] == "NGA_annotations.csv"):
            datasetDict_flower["nga_flowers"]["files"].append({"filename":row["image_file"], "regions" :[]})
        elif(row["dataset"] == "RKD_annotations.csv"):
            datasetDict_flower["rkd_flowers"]["files"].append({"filename":row["image_file"], "regions" :[]})
        elif(row["dataset"] == "SLUB_annotations.csv"):
            datasetDict_flower["slub_flowers"]["files"].append({"filename":row["image_file"], "regions" :[]})
        elif(row["dataset"] == "STÄDEL_annotations.csv"):
            datasetDict_flower["staedel_flowers"]["files"].append({"filename":row["image_file"], "regions" :[]})
        elif(row["dataset"] == "wga_annotations.csv"):
            datasetDict_flower["wga_flowers"]["files"].append({"filename":row["image_file"], "regions" :[]})
        else:
            print("No matching Dataset found: ", row["dataset"])
#for x,y in datasetDict_flower.items():
#    print(x,y)

os.chdir("pathxy")
#get all regions from the according json files tagged with "flower"
#convert polygon coordinates to rect coordinates
#save them in dict
failures = []
for values in datasetDict_flower.values():
    with open(metadataRelations[values["csv_Metadata"]], "r") as read_file:
        data = json.load(read_file)
    for file in values["files"]:
        for entry in data.values():
            if(entry["filename"] == file["filename"]):
                for region in entry["regions"]:
                    if "object/attribute/figure" in region["region_attributes"]:
                        if(region["region_attributes"]["object/attribute/figure"] == "flower vase"):
                            if(region["shape_attributes"]["name"] == "polygon"):
                                polytemp = [];
                                for i in range(len(region["shape_attributes"]["all_points_x"])):
                                    coordtemp = [region["shape_attributes"]["all_points_x"][i], region["shape_attributes"]["all_points_y"][i]]
                                    polytemp.append(coordtemp)
                                polygon = Polygon(polytemp)
                                poly_bbox = polygon.bounds

                                x = poly_bbox[0]
                                y = poly_bbox[1]
                                #width = poly_bbox[2] - poly_bbox[0]
                                height = poly_bbox[3] - poly_bbox[1]
                                width = height*0.75
                                rectRegion = {
                                    "name": "rect",
                                    "x": x,
                                    "y": y,
                                    "width": width,
                                    "height": height
                                    }
                                file["regions"].append(rectRegion)
                            elif(region["shape_attributes"]["name"] == "polyline"):
                                linetemp = [];
                                for i in range(len(region["shape_attributes"]["all_points_x"])):
                                    coordtemp = [region["shape_attributes"]["all_points_x"][i], region["shape_attributes"]["all_points_y"][i]]
                                    linetemp.append(coordtemp)
                                polyline = LineString(linetemp)
                                line_bbox = polyline.bounds

                                x = line_bbox[0]
                                y = line_bbox[1]
                                #width = line_bbox[3] - line_bbox[0]
                                height = line_bbox[3] - line_bbox[0]
                                width = height*0.75
                                rectRegion = {
                                    "name": "rect",
                                    "x": x,
                                    "y": y,
                                    "width": width,
                                    "height": height
                                    }
                                file["regions"].append(rectRegion)
                            else:
                                x = region["shape_attributes"]["x"]
                                y = region["shape_attributes"]["y"]
                                height = region["shape_attributes"]["height"]
                                width = height*0.75
                                rectRegion = {
                                    "name": "rect",
                                    "x": x,
                                    "y": y,
                                    "width": width,
                                    "height": height
                                    }
                                file["regions"].append(rectRegion)
                    else:
                        #print("failed to find object/attribute/figure: ", region)
                        failures.append(region);
print("All failures:")
print(failures)
print("Number of failures ", len(failures))

croppedList = []
testList = []
testList2 = []

for values in datasetDict_flower.values():
    os.chdir("pathxy")
    os.chdir(pictureRelations[values["csv_Metadata"]])
    for file in values["files"]:
        image = Image.open(file["filename"])
        #print(values["csv_Metadata"])
        #print(file["filename"])
        testList2.append(file)
        for region in file["regions"]:
            x = int(region["x"])
            y= int(region["y"])
            x2 = int(region["x"] + region ["width"])
            y2 = int(region["y"] + region["height"])
            #print(x,y,x2,y2)
            #print(image.size)
            testList.append(region)
            cropped = image.crop((x, y, x2, y2))
            croppedList.append(cropped)

print("Number of cropped images ", len(croppedList))
print("Number of regions ", len(testList))
print("Number of files ", len(testList2))
os.chdir("pathxy")

for i in range(len(croppedList)):
    filename = str(i) + "cropped_flowerVase.jpeg"
    croppedList[i].save(filename)
