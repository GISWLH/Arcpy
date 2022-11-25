# Copyright (c) 2022 Longhao Wang. hhuwlh@163.com All rights reserved.
# This work is licensed under the terms of the MIT license.  
# or a copy, see <https://opensource.org/licenses/MIT>.

import arcpy
from arcpy import env
import os
from arcpy.sa import *
ws = r"D:\OneDrive\UCAS\courses\python2\final2\output"
def spline():
    try:
		inPointFeatures = os.path.join(ws,"data.shp") 
		region = os.path.join(ws,"region_final.shp") 
		zField = "DEM"
		outRaster = os.path.join(ws,"DEMspline.tif")
		extent = os.path.join(ws,"region_final.shp")
		cellSize = 0.00083333333
		splineType = "REGULARIZED"
		spline = arcpy.Spline_3d(inPointFeatures, zField, outRaster, cellSize, 
		                splineType)
		outExtractByMask = ExtractByMask(spline, region)
		extract = os.path.join(ws,"DEMspline_extract.tif")
		outExtractByMask.save(extract)
	except Exception, e:
	        print str(e)

if __name__=="__main__":
	spline()
	print('OK')