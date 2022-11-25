# Copyright (c) 2022 Longhao Wang. hhuwlh@163.com All rights reserved.
# This work is licensed under the terms of the MIT license.  
# or a copy, see <https://opensource.org/licenses/MIT>.

import arcpy
import xlrd
from arcpy import env
import os
from arcpy.sa import *
rs = r"D:\OneDrive\UCAS\courses\python2\final2\input"
ws = r"D:\OneDrive\UCAS\courses\python2\final2\output"
def creat_box():
    try:
        #workspace
        #ws = r"D:\OneDrive\UCAS\courses\python2\final2"
        #outfile = os.path.join(ws,"output","region.shp")
        outfile = os.path.join(ws,"region.shp") 
        #WGS84
        outSR = arcpy.SpatialReference(4326)
        coordinates = [115.5, 39.5, 116, 39.83]
        LowerLeft = arcpy.Point(coordinates[0],coordinates[1])
        LowerRight = arcpy.Point(coordinates[2],coordinates[1])
        UpperLeft = arcpy.Point(coordinates[0],coordinates[3])
        UpperRight = arcpy.Point(coordinates[2],coordinates[3])
        #creat point
        array = arcpy.Array()
        array.add(LowerLeft)
        array.add(LowerRight)
        array.add(UpperRight)
        array.add(UpperLeft)
        array.add(LowerLeft)
        #creat polygon
        polygon = arcpy.Polygon(array)   
        #save
        arcpy.CopyFeatures_management(polygon, outfile)
        #define projection
        arcpy.DefineProjection_management(outfile, outSR)
        print('OK')
    except Exception, e:
        print str(e)

def clip_region():
    try:
        region = os.path.join(ws,"region.shp")
        inRaster = os.path.join(rs,'beijingDEM.tif') 
        outPolygons = os.path.join(ws,'beijing.shp')
        outPolygons2 = os.path.join(ws,'region_final.shp')
        beijings = arcpy.RasterDomain_3d(inRaster, outPolygons, "POLYGON")
        arcpy.Clip_analysis(beijings, region, outPolygons2)
        print('OK')
    except Exception, e:
        print str(e)

def creat_random():
    try:
        outGDB = ws
        numPoints = 200
        outName = 'random_point'
        fcExtent1 = os.path.join(ws,"region_final.shp")
        arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)
        random = arcpy.CreateRandomPoints_management(outGDB, outName, fcExtent1, '', numPoints)
        arcpy.env.outputCoordinateSystem = ""
        print "A Shape file is created!"
        fieldName1 = "code"
        fieldName2 = "name1"
        fieldName3 = "x"
        fieldName4 = "y"
        fieldName5 = "DEM"
        fieldName6 = "name2"
        fieldName7 = 'map'
        fieldLength = 30
        arcpy.AddField_management(random, fieldName1, "TEXT", "", "", fieldLength)
        arcpy.AddField_management(random, fieldName2, "TEXT", "", "", fieldLength)
        arcpy.AddField_management(random, fieldName3, "FLOAT", "", "", fieldLength)
        arcpy.AddField_management(random, fieldName4, "FLOAT", "", "", fieldLength)
        arcpy.AddField_management(random, fieldName5, "FLOAT", "", "", fieldLength)
        arcpy.AddField_management(random, fieldName6, "TEXT", "", "", fieldLength)
        arcpy.AddField_management(random, fieldName7, "TEXT", "", "", fieldLength)
        arcpy.AddMessage("Point shp has created")
        arcpy.CalculateField_management(random,"code",expression,"PYTHON_9.3",codeblock)
        arcpy.CalculateField_management(random,"name1",expression2,"PYTHON_9.3")
        arcpy.CalculateField_management(random,"x",'!shape.extent.XMax!',"PYTHON_9.3")
        arcpy.CalculateField_management(random,"y",'!shape.extent.YMax!',"PYTHON_9.3")
        arcpy.CalculateField_management(random,"name2",expression3,"PYTHON_9.3")
        arcpy.CalculateField_management(random,"map",expression4,"PYTHON_9.3",codeblock2)

    except Exception, e:
        print str(e)

codeblock = '''
rec=0
def autoIncrement():
    global rec
    pStart = 1 
    pInterval = 1 
    if (rec == 0): 
        rec = pStart 
    else: 
        rec = rec + pInterval 
    return rec
'''
codeblock2 = '''
def getmap(x,y):
    if (x < 115.75) & (y > 39.67):
        return 'J50E002007'
    elif (x < 115.75) & (y < 39.67):
        return 'J50E003007'
    elif (x > 115.75) & (y > 39.67):
        return 'J50E002008'
    else:
        return 'J50E003008'
'''


expression = "'Drandom' + str(autoIncrement())"
expression2 = "'random_north'"
expression3 = "'fangshan_north'"
expression4 = 'getmap(!x!, !y!)'
def extract_DEM():
    try:
        arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)
        in_point_features = os.path.join(ws,"random_point.shp")
        in_rasters = os.path.join(rs,"beijingDEM.tif")
        in_features = ExtractMultiValuesToPoints(in_point_features, 
            [in_rasters], "BILINEAR")
        arcpy.env.outputCoordinateSystem = ""
        arcpy.CalculateField_management(in_features,"DEM",'!beijingDEM!',"PYTHON_9.3")
        arcpy.DeleteField_management(in_features, 'beijingDEM')
        print('OK')
    except Exception, e:
        print str(e)

def creatshp(shapefilename):
    out_path,out_name=os.path.split(shapefilename)
    geometry_type = "POINT"
    has_m = "DISABLED"
    has_z = "DISABLED"
    spatial_reference = arcpy.SpatialReference(4326)
    if arcpy.Exists(shapefilename):
        arcpy.Delete_management(shapefilename)
        print shapefilename + " is deleted!"
    arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, "", has_m, has_z, spatial_reference)
    print "A Shape file is created!"
    fieldName1 = "code"
    fieldName2 = "name1"
    fieldName3 = "x"
    fieldName4 = "y"
    fieldName5 = "DEM"
    fieldName6 = "name2"
    fieldName7 = 'map'
    fieldLength = 30
    arcpy.AddField_management(shapefilename, fieldName1, "TEXT", "", "", fieldLength)
    arcpy.AddField_management(shapefilename, fieldName2, "TEXT", "", "", fieldLength)
    arcpy.AddField_management(shapefilename, fieldName3, "FLOAT", "", "", fieldLength)
    arcpy.AddField_management(shapefilename, fieldName4, "FLOAT", "", "", fieldLength)
    arcpy.AddField_management(shapefilename, fieldName5, "FLOAT", "", "", fieldLength)
    arcpy.AddField_management(shapefilename, fieldName6, "TEXT", "", "", fieldLength)
    arcpy.AddField_management(shapefilename, fieldName7, "TEXT", "", "", fieldLength)
    arcpy.AddMessage("Point shp has created")

def xlstoarcgis(excelfilename,shapefilename):
    pathdir = os.path.split(shapefilename)[0]
    filename = os.path.split(shapefilename)[1]

    table = xlrd.open_workbook(excelfilename)
    sheet = table.sheet_by_name('data')
    nrows = sheet.nrows
    ncols = sheet.ncols
    print "num of rows:{0}, num of cols:{1}".format(nrows, ncols)
    x = sheet.col_values(6, 1, nrows)
    y = sheet.col_values(7, 1, nrows)
    code = sheet.col_values(1, 1, nrows)
    name1 = sheet.col_values(3, 1, nrows)
    DEM = sheet.col_values(8, 1, nrows)
    name2 = sheet.col_values(9, 1, nrows)
    Map = sheet.col_values(10, 1, nrows)

    rows = arcpy.da.InsertCursor(shapefilename, ['name1', 'x', 'y', 'code',
        'name2', 'DEM', 'Map', 'SHAPE@XY'])
    
    for i in range(0,nrows-1):
        pointrow = (name1[i], x[i], y[i], code[i], name2[i], DEM[i], Map[i], (x[i], y[i]))
        rows.insertRow(pointrow)
    del rows
    spatial_reference = arcpy.SpatialReference(4326)
    arcpy.DefineProjection_management(shapefilename, spatial_reference)

def merge_table(shapefilename, shapefilename1):
    excel_table = shapefilename
    random_table = os.path.join(ws,"random_point.shp")
    arcpy.Merge_management([excel_table, random_table], shapefilename1)


if __name__=="__main__":
    excelfilename=arcpy.GetParameterAsText(0)
    shapefilename1=arcpy.GetParameterAsText(1)
    shapefilename=os.path.join(ws,"excel_table.shp")
    creat_box()
    clip_region()
    creat_random()
    extract_DEM()
    creatshp(shapefilename)
    xlstoarcgis(excelfilename,shapefilename)
    merge_table(shapefilename, shapefilename1)
