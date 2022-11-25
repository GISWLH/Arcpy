# Copyright (c) 2022 Longhao Wang. hhuwlh@163.com All rights reserved.
# This work is licensed under the terms of the MIT license.  
# or a copy, see <https://opensource.org/licenses/MIT>.
import arcpy
from arcpy import env
import os

ws = r"D:\OneDrive\UCAS\courses\python2\final2\output"
env.outputCoordinateSystem = arcpy.SpatialReference(4326)

# Set local variables
outFeatureClass = os.path.join(ws,"grid.shp") 
polygonWidth = "0.25"
polygonHeight= "0.166666667"
originCoord = "115.5 39.5"
numberRows = "2"
numberColumns = "2"

# Execute GridIndexFeatures
arcpy.GridIndexFeatures_cartography(outFeatureClass, "", "", "", "",
                                    polygonWidth, polygonHeight, originCoord,
                                    numberRows, numberColumns)
expression = 'getmap(!PageNumber!)'
codeblock = '''
def getmap(x):
    if (x == 1):
        return 'J50E002007'
    elif (x == 3):
        return 'J50E003007'
    elif (x == 2):
        return 'J50E002008'
    else:
        return 'J50E003008'
'''
arcpy.CalculateField_management(outFeatureClass,"PageName",expression,"PYTHON_9.3",codeblock)

