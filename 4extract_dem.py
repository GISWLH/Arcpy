# Copyright (c) 2022 Longhao Wang. hhuwlh@163.com All rights reserved.
# This work is licensed under the terms of the MIT license.  
# or a copy, see <https://opensource.org/licenses/MIT>.
import os
import arcpy
from arcpy.sa import *
def extract_DEM():
	try:
		arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)
		in_features = ExtractValuesToPoints("D:/OneDrive/UCAS/courses/python2/final2/output/random_point.shp", 
			"D:/OneDrive/UCAS/courses/python2/final2/input/beijingDEM.tif",
			"D:/OneDrive/UCAS/courses/python2/final2/output/DEM_points.shp","INTERPOLATE", "ALL")
		arcpy.env.outputCoordinateSystem = ""
		arcpy.CalculateField_management(in_features,"DEM",'!RASTERVALU!',"PYTHON_9.3")
		print('OK')
	except Exception, e:
		print str(e)
if __name__=="__main__":
     extract_DEM()
