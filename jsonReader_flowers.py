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

#Relation between the precalculated label mappings for each imagefile in the dataset (csv) and the actual metadata of the dataset with the coordinates of the labels (json)
metadataRelations = {
        "Ambrosiana_annotations.csv":"Ambrosiana_exported_finished_json.json" ,
        "Artstor_annotations.csv":"Artstor_exported_finished_json.json",
        "Ashmolean_annotations.csv":"Ashmolean_exported_finished_json.json",
        #"BeniCulturali_annotations.csv":"BeniCulturaliModified_exported_finished_json.json", (There where some issues with the BeniCulturali Dataset. Because of deadlines the dataset was left out)
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

#Relation between the datasets and the folder names in which the associated images are stored
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

# custom dict structure for temporary storage of files, images and associated metadata per dataset
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


os.chdir("pathxy") #change directory to folder where results from csvReader.py are stored

#get all imagefiles, sort them according to associated dataset and save them in dict
with open("flowers.csv", newline="") as csvfile:
    flowers = csv.DictReader(csvfile, delimiter=",") #open generated csv file flowers.csv from csvReader.py
    for row in flowers: #loop through all entries in csv, sort them according to associated dataset and save them in dict
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


os.chdir("pathxy") #change directory to folder where annotation metadata is saved
#get all regions from the according json files tagged with "flower"
#convert polygon coordinates to rect coordinates
#save them in dict
for values in datasetDict_flower.values(): #loop through all datasets and their associated values
    with open(metadataRelations[values["csv_Metadata"]], "r") as read_file: # for each dataset: open associated json metadata file
        data = json.load(read_file) #convert json in python dict

    for file in values["files"]: #loop through all associated image files for the current dataset
        for entry in data.values(): #loop through all entries in the metadata (there is one entry for every annotated image file)
            if(entry["filename"] == file["filename"]): #If filenames of current image file and metadata entry are the same
                for region in entry["regions"]: #loop through all annotated regions in this specific entry for the image file
                    if(region["region_attributes"]["object/attribute/figure"] == "flower"): #if region has the wished label (flower)
                        if(region["shape_attributes"]["name"] == "polygon"): #if the region has the shape of a polygon (Polygons cannot be handled in later steps so they have to be converted into rects)
                            polytemp = [];
                            for i in range(len(region["shape_attributes"]["all_points_x"])): #get all points of the polygon
                                coordtemp = [region["shape_attributes"]["all_points_x"][i], region["shape_attributes"]["all_points_y"][i]]
                                polytemp.append(coordtemp) #save them in a list
                            polygon = Polygon(polytemp) #create a python polygon object out of them
                            poly_bbox = polygon.bounds #get the bounding box (a list of the coordinates of the surrounding rectangle) of this newly created polygon

                            x = poly_bbox[0] #save associated x value of bounding box
                            y = poly_bbox[1] #save associated y value of bounding box
                            width = poly_bbox[2] - poly_bbox[0] #calculate width out of bounding box coordinates
                            height = poly_bbox[3] - poly_bbox[1] #calculate height out of bounding box coordinates
                            rectRegion = { #create an artificial rect region to replace the polygon region
                                    "name": "rect",
                                    "x": x,
                                    "y": y,
                                    "width": width,
                                    "height": height
                                    }
                            file["regions"].append(rectRegion) #append this newly created rect region to regions of the current file
                        elif(region["shape_attributes"]["name"] == "polyline"): #if the region has the shape of a polyline (Polylines cannot be handled in later steps so they have to be converted into rects)
                            linetemp = [];
                            for i in range(len(region["shape_attributes"]["all_points_x"])): #get all points of the polyline
                                coordtemp = [region["shape_attributes"]["all_points_x"][i], region["shape_attributes"]["all_points_y"][i]]
                                linetemp.append(coordtemp) #save them in a list
                            polyline = LineString(linetemp) #create a python LineString object out of them
                            line_bbox = polyline.bounds #get the bounding box (a list of the coordinates of the surrounding rectangle) of this newly created linestring/polyline

                            x = line_bbox[0] #save associated x value of bounding box
                            y = line_bbox[1] #save associated y value of bounding box
                            width = line_bbox[3] - line_bbox[0] #calculate width out of bounding box coordinates
                            height = line_bbox[3] - line_bbox[0] #calculate height out of bounding box coordinates
                            rectRegion = { #create an artificial rect region to replace the polyline region
                                    "name": "rect",
                                    "x": x,
                                    "y": y,
                                    "width": width,
                                    "height": height
                                    }
                            file["regions"].append(rectRegion) #append this newly created rect region to regions of the current file
                        else: #the region is of the type rect
                            file["regions"].append(region["shape_attributes"]) #just append the attributes of the rect regions to regions of the current file

croppedList = [] #list for the individual images of flower regions

for values in datasetDict_flower.values(): #loop through each dataset and their values
    os.chdir("pathxy") #change directory to folder where images of each dataset is saved
    os.chdir(pictureRelations[values["csv_Metadata"]]) #change directory to image folder of current dataset
    for file in values["files"]: #loop through all image filenames of current dataset
        image = Image.open(file["filename"]) #open current imagefile as python image

        for region in file["regions"]: #loop through all region coordinates in current imagefile
            #get coordinates
            x = int(region["x"])
            y= int(region["y"])
            x2 = int(region["x"] + 150) #dirty solution to get the right image size see jsonReader_flowerVase_v2 for better solution
            y2 = int(region["y"] + 200) #dirty solution to get the right image size see jsonReader_flowerVase_v2 for better solution

            cropped = image.crop((x, y, x2, y2)) #crop image according to coordinates of current region
            croppedList.append(cropped) #append this cropped image to list

os.chdir("pathxy") #change directory to folder where you want to save the newly created images of all flower regions

for i in range(len(croppedList)): #loop through all cropped images and save them as jpeg
    filename = str(i) + "cropped_flower.jpeg"
    croppedList[i].save(filename)
