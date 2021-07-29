
import numpy as np

for year in range(2001,2019):
    for day in range(1,365,8):

        map1 = np.fromfile("E:/work/publication_zhou/data/MAP4/map"+str(year)+"d"+str(day)+".flt", dtype=np.float32)
        map1 = np.reshape(map1, (2009, 764))
        
        # 0: no-water, 1: mixed, 2: flooding, 3: waterbody
        
    
        flood_final = np.where(map1 == -1, 0, map1)
        flood_final = np.where(map1 == -9999, -9999, flood_final)
        
        flood_final = flood_final.astype(np.float32)

    
        fileout = "E:/work/publication_zhou/data/MAP4/flood_final/flood_final"+str(year)+"d"+str(day)+".flt"
        f=open(fileout,"wb")
        f.write(flood_final)
        f.close() 
    
