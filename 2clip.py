# Copyright (c) 2022 Longhao Wang. hhuwlh@163.com All rights reserved.
# This work is licensed under the terms of the MIT license.  
# or a copy, see <https://opensource.org/licenses/MIT>.
import os
import arcpy

def clip_region():
	try:
		region = r'D:\OneDrive\UCAS\courses\python2\final2\output\region.shp'
		inRaster = r'D:\OneDrive\UCAS\courses\python2\final2\input\beijingDEM.tif'
		outPolygons = r'D:\OneDrive\UCAS\courses\python2\final2\output\beijing.shp'
		outPolygons2 = r'D:\OneDrive\UCAS\courses\python2\final2\output\region_final.shp'
		beijings = arcpy.RasterDomain_3d(inRaster, outPolygons, "POLYGON")
		arcpy.Clip_analysis(beijings, region, outPolygons2)
		print('OK')
	except Exception, e:
		print str(e)

if __name__=="__main__":
     clip_region()
