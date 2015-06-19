import arcpy
import os
from os import listdir


arcpy.env.workspace = "C:/Users/deepwinter/Documents/ArcGIS/Projects/NASQAN"

# read in all the dbf files
dbfPath = arcpy.env.workspace + '/zonal_stats_tables'

for d in listdir(dbfPath):

    dbfData = []
    for f in listdir(dbfPath + '/' + d):

        fileName, fileExtension = os.path.splitext(f)
        if(fileExtension != '.dbf'):
            continue


    # A list of values that will be used to construct new rows
    #
    #row_values = [('Anderson', (1409934.4442000017, 1076766.8192000017)),
    #             ('Andrews', (752000.2489000037, 1128929.8114))]

        # read in data from DBF and create dictionary
        dbfFile = dbfPath + '/' + d + '/' + f
        with arcpy.da.SearchCursor(dbfFile, ['STAID','SUM','DATE']) as cursor:
            for row in cursor:
                dbfData.append(row)
        del cursor

    #print dbfData

    # write them out to a single file    
    # Open an InsertCursor
    #
    dbfFile = arcpy.env.workspace + '/zonal_stats_consolidated/' + d + '.dbf'
    arcpy.CreateTable_management(  arcpy.env.workspace + '/zonal_stats_consolidated/',
                                   d + '.dbf',
                                   arcpy.env.workspace + '/template.dbf'
                                 )
    cursor = arcpy.da.InsertCursor(dbfFile,
                               ("STAID", "SUM", "DATE"))

    # Insert new rows that include the county name and a x,y coordinate
    #  pair that represents the county center
    #
    for row in dbfData:
        #print 'row'
        #print row
        cursor.insertRow(row)

    # Delete cursor object
    #
    del cursor