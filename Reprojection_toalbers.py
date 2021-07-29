import arcpy
arcpy.CheckOutExtension("Spatial")
from arcpy.sa import *
from arcpy import env
import shutil 

import multiprocessing
from joblib import Parallel, delayed

def processInput(year):
	for day in range(353, 362, 8):
		shutil.copyfile("E:\\work\\publication_zhou\\data\\precipitation\\composite\\test.prj", "E:\\work\\publication_zhou\\data\\precipitation\\composite\\y"+str(year)+"d"+str(day)+".prj")
		shutil.copyfile("E:\\work\\publication_zhou\\data\\precipitation\\composite\\test.hdr", "E:\\work\\publication_zhou\\data\\precipitation\\composite\\y"+str(year)+"d"+str(day)+".hdr")
		
		# Local variables:
		in_flt = "E:\\work\\publication_zhou\\data\\precipitation\\composite\\y"+str(year)+"d"+str(day)+".flt"
		out_tif = "E:\\work\\publication_zhou\\data\\precipitation\\composite_albers\\y"+str(year)+"d"+str(day)+".tif"

		# Process: Project Raster
		arcpy.ProjectRaster_management(in_flt, out_tif, "PROJCS['Albers_Conic_Equal_Area',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Albers'],PARAMETER['false_easting',0.0],PARAMETER['false_northing',0.0],PARAMETER['central_meridian',-96.0],PARAMETER['standard_parallel_1',29.5],PARAMETER['standard_parallel_2',45.5],PARAMETER['latitude_of_origin',23.0],UNIT['Meter',1.0]]", "NEAREST", "1000 1000", "WGS_1984_(ITRF00)_To_NAD_1983", "", "PROJCS['Lambert_Conformal_Conic_2SP',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['false_easting',0.0],PARAMETER['false_northing',0.0],PARAMETER['central_meridian',-100.0],PARAMETER['standard_parallel_1',25.0],PARAMETER['standard_parallel_2',60.0],PARAMETER['latitude_of_origin',42.5],UNIT['Meter',1.0]]", "NO_VERTICAL")

num_cores = multiprocessing.cpu_count()
results = Parallel(n_jobs=num_cores)(delayed(processInput)(year) for year in range(2016, 2017))        
