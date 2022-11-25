import os
import arcpy

# Copyright (c) 2022 Longhao Wang. hhuwlh@163.com All rights reserved.
# This work is licensed under the terms of the MIT license.  
# or a copy, see <https://opensource.org/licenses/MIT>.
def creat_box():
	try:
		#workspace
		ws = r"D:\OneDrive\UCAS\courses\python2\final2"
		outfile = os.path.join(ws,"output","region.shp")
		 
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

if __name__=="__main__":
     creat_box()
