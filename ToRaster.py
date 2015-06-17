import arcpy
from arcpy import env
import os
from os import listdir

env.workspace = "C:/Users/deepwinter/Documents/ArcGIS/Projects/NASQAN"
#precip_path = env.workspace + "/precip_2009_2015"
precip_path = env.workspace + "/reproj"

print precip_path

valField = "Globvalue"
assignmentType = "SUM"
priorityField = None
cellSize = 1

for f in listdir(precip_path):

    
    fileName, fileExtension = os.path.splitext(f)

    print fileExtension

    if fileExtension != '.shp':
        continue;

    print f

    
    #setup
    inFeatures = precip_path + "/" + f
    outRaster = env.workspace + "/precip_2009_2015_raster/" + fileName + ".tif"

    #execute PointToRaster
    arcpy.PointToRaster_conversion(inFeatures, valField, outRaster, assignmentType, priorityField, cellSize)