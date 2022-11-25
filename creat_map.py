# Copyright (c) 2022 Longhao Wang. hhuwlh@163.com All rights reserved.
# This work is licensed under the terms of the MIT license.  
# or a copy, see <https://opensource.org/licenses/MIT>.
import os
import arcpy
from arcpy.sa import *
mxd = arcpy.mapping.MapDocument("D:/OneDrive/UCAS/courses/python2/final2/workspace.mxd")
for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
    mxd.dataDrivenPages.currentPageID = pageNum
    graphiccode=str(mxd.dataDrivenPages.pageRow.getValue("pageName"))
    print "printing {}".format(mxd.dataDrivenPages.pageRow.getValue("pageName"))
    #设置图像标题为图幅编号
    for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
       if elm.name == "title":
          elm.text = "Beijing DEM(m)"+"("+graphiccode+")"
    name="D:/OneDrive/UCAS/courses/python2/final2/map/" + graphiccode + ".jpg"
    print name
    arcpy.mapping.ExportToJPEG(mxd,  name, resolution = 300, jpeg_quality =80)
del mxd
