import arcpy
from arcpy import env
import os
from os import listdir

env.workspace = "C:/Users/deepwinter/Documents/ArcGIS/Projects/NASQAN"
precip_path = "D:/GIS/NASQAN/precip_2009_2015"
#precip_path = "C:/Users/deepwinter/Documents/ArcGIS/Projects/NASQAN/remain"


for f in listdir(precip_path):

    fileName, fileExtension = os.path.splitext(f)
    print fileExtension
    if fileExtension != '.shp':
        continue;
    print f

    coordinateSystem = 'PROJCS["HRAP_Projected",GEOGCS["HRAP_GCS",DATUM["D_HRAP",SPHEROID["HRAP_Sphere",6371200.0,0.0]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Stereographic_North_Pole"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-105.0],PARAMETER["Standard_Parallel_1",60.0],UNIT["HRAP_Grid",4762.5]]'
    arcpy.Project_management(precip_path + "/" + f, env.workspace + '/reproj/' + f , coordinateSystem)