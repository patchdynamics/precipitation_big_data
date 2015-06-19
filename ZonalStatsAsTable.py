# Name: ZonalStatisticsAsTable_Ex_02.py
# Description: Summarizes values of a raster within the zones of 
#              another dataset and reports the results to a table.
# Requirements: Spatial Analyst Extension
# Author: ESRI

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *
import os
from os import listdir

# Set environment settings
env.workspace = "C:/Users/deepwinter/Documents/ArcGIS/Projects/NASQAN"
arcpy.env.extent = "MAXOF"

shapePath = "/nasqan_shp_hrap"
precipRasterPath = "/precip_2009_2015_raster"
outputPath = "/zonal_stats_tables"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

for f in listdir(env.workspace + shapePath):
    fileNameZone, fileExtensionZone = os.path.splitext(f)
    if fileExtensionZone != '.shp':
        continue

    print f

    nameParts = fileNameZone.split('_')
    staid = nameParts[5]

    # Set local variables
    inZoneData = env.workspace + shapePath + "/" + f
    zoneField = "STAID"

    for f2 in listdir(env.workspace + precipRasterPath):
        fileNameRaster, fileExtensionRaster = os.path.splitext(f2)

        if(fileExtensionRaster != '.tif'):
            continue

        nameParts = fileNameRaster.split('_')
        dateString = nameParts[4]
        print dateString

        inValueRaster = env.workspace + precipRasterPath + "/" + f2
        outTable = fileNameZone + "_" + dateString + ".dbf"
        outDir = env.workspace + outputPath + "/" + staid + "/"
        outPath = outDir + outTable

        if not os.path.exists(outDir):
            os.makedirs(outDir)

        # Execute ZonalStatisticsAsTable
        outZSaT = ZonalStatisticsAsTable(inZoneData, zoneField, inValueRaster, 
                                        outPath, "DATA", "SUM")

        arcpy.AddField_management (outPath, "DATE", "text", "", "", "50")

        # Apply the filename to all entries       
        arcpy.CalculateField_management (outPath, "DATE", dateString)
