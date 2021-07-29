import arcpy
import numpy as np
arcpy.CheckOutExtension("Spatial")
from arcpy.sa import *
import pandas as pd

nlcd = Raster(r"D:\DEM\NLCD\nlcd_new_w1.tif")
nlcd_nparr = arcpy.RasterToNumPyArray(nlcd,nodata_to_value = 0)

k = 0
water_wetland3=np.zeros((601*266, 1),dtype=np.float32)
developed3=np.zeros((601*266, 1),dtype=np.float32)
woody3=np.zeros((601*266, 1),dtype=np.float32)

herbaceous3=np.zeros((601*266, 1),dtype=np.float32)
planted_cultivated3=np.zeros((601*266, 1),dtype=np.float32)
#std2=np.zeros((165*110, 1),dtype=np.float32)
#range2=np.zeros((165*110, 1),dtype=np.float32)

for i in range(0,12021-20,20):
    for j in range(0,5321-20,20):
        a = nlcd_nparr[i:(i+20),j:(j+20)]
        
        # a = np.reshape((1,400),a)
        
        water_wetland = np.count_nonzero(a==11) + np.count_nonzero(a==90)+ np.count_nonzero(a==95)
        #print(water_wetland)
        
        #water_wetland2 = float(water_wetland)/400.0
##
        developed = np.count_nonzero(a==12)+np.count_nonzero(a==21)+np.count_nonzero(a==22)+np.count_nonzero(a==23)+np.count_nonzero(a==24)
##        developed2 = developed/400

        woody = np.count_nonzero(a==51)+ np.count_nonzero(a==52)+np.count_nonzero(a==41)+np.count_nonzero(a==42)+np.count_nonzero(a==43)
##        barren2 = barren/400
##
        
##        forest2 = forest/400
##
        herbaceous = np.count_nonzero(a==71)+np.count_nonzero(a==72)+np.count_nonzero(a==73)+np.count_nonzero(a==74)
##        shrubland_herbaceous2 = shrubland_herbaceous/400
##
        planted_cultivated = np.count_nonzero(a==81)+np.count_nonzero(a==82)
##        planted_cultivated2 = planted_cultivated/400
##        
        water_wetland3[k,0] = water_wetland
        developed3[k,0] = developed
        woody3[k,0] = woody
        
        herbaceous3[k,0] = herbaceous
        planted_cultivated3[k,0] = planted_cultivated
        
    
        if water_wetland!=0 | developed!=0 | woody!=0 |  herbaceous!=0 | planted_cultivated!=0:
        
        
            
        
            result = np.concatenate((water_wetland3,developed3,woody3,herbaceous3,planted_cultivated3),axis = 1)
        k = k+1
        
        
np.savetxt("result_nlcd_new_w1.csv",result)
