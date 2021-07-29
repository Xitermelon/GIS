import arcpy
arcpy.CheckOutExtension("Spatial")
from arcpy import env
from arcpy.sa import *
import numpy as np

outputfile=open("D:/temperature/tmax/tmax_mean/w7.txt","w")

wid_1k = Raster(r"D:\precipitation\watershed\wid_1k.tif")
env.extent = wid_1k

mask_watershed = Con(wid_1k == 7, 1)

for year in range(2001, 2019):
    for mon in range(1,13):
        prcp = Raster("D:/temperature/tmax/tmax_albers/tmax_cut/"+'y'+str(year)+"m"+str(mon)+".tif")
        
        prcp2 = prcp * mask_watershed
        prcp_stat = prcp2.mean
        
        print(str(year)+str(mon)+"  "+str(prcp_stat))
        outputfile.write(str(year)+str(mon)+"  "+str(prcp_stat)+"\n")
outputfile.close()


