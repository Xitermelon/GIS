import arcpy
arcpy.CheckOutExtension("Spatial")
from arcpy import env
from arcpy.sa import *


w2_prob_500m = Raster(r"D:\DEM\500_prob_w2.tif")
w2_slope_25m = Raster(r"D:\DEM\nlcd_w2.tif")



env.extent =  w2_prob_500m
w2_slope_25m = w2_slope_25m * 1.0

w2_slope_25m.save(r"D:\DEM\NLCD\nlcd_new_w2.tif")




 
