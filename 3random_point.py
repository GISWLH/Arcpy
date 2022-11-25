# Copyright (c) 2022 Longhao Wang. hhuwlh@163.com All rights reserved.
# This work is licensed under the terms of the MIT license.  
# or a copy, see <https://opensource.org/licenses/MIT>.
import os
import arcpy
#arcpy.CreateFileGDB_management('D:/OneDrive/UCAS/courses/python2/final2/output', 'table.gdb')
def creat_shp():
	try:
	    outGDB = "D:/OneDrive/UCAS/courses/python2/final2/output"
	    numPoints = 200
	    outName = 'random_point'
	    fcExtent1 = r"D:\OneDrive\UCAS\courses\python2\final2\output\region_final.shp"
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
	    fieldLength = 20
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
expression = "'Drandom' + str(autoIncrement())"
expression2 = "'随机点北'"


if __name__=="__main__":
     creat_shp()
