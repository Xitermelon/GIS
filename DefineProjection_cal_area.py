import arcpy
arcpy.CheckOutExtension("Spatial")
from arcpy import env
from arcpy.sa import *
import numpy as np

outputfile=open("D:/LMAV_flooding/data/MAP/flood_new/flood_raster/w7.txt","w")

wid_1k = Raster(r"D:\precipitation\watershed\wid_1k.tif")
env.extent = wid_1k


mask_watershed = Con(wid_1k == 7, 1)
arcpy.env.cellSize = 463.3127165


for year in range(2001, 2019):
    for day in range(1,365,8):
        #inFLT = "D:/precipitation/composite_monthly/"+'y'+str(year)+'m'+str(mon)+".flt"

        #outRaster = "D:/precipitation/composite_monthly_albers/"+'y'+str(year)+'m'+str(mon)+".tif"

        #arcpy.FloatToRaster_conversion(inFLT, outRaster)

        #arcpy.DefineProjection_management(outRaster, "PROJCS['USA_Contiguous_Albers_Equal_Area_Conic_USGS_version',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Albers'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-96.0],PARAMETER['Standard_Parallel_1',29.5],PARAMETER['Standard_Parallel_2',45.5],PARAMETER['Latitude_Of_Origin',23.0],UNIT['Meter',1.0]]")
#translate from here
        area = Raster("D:/LMAV_flooding/data/MAP/flood_new/flood_raster/"+"new_flood_final"+str(year)+"d"+str(day)+".tif")

        area_new = area * mask_watershed
        area_nparr = arcpy.RasterToNumPyArray(area_new, nodata_to_value=0)
        
        area_new2 = area_nparr.sum() *463.3127165*463.3127165
        
    #print(str(year)+str(mon)+"  "+str(area_new2))
        outputfile.write(str(year)+"  "+str(area_new2)+"\n")


outputfile.close()



