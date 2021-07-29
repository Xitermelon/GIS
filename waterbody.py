
import numpy as np

i = 0
flood_all = np.ones(( 828, 2009, 764), dtype=np.float32)
print("test")

for year in range(2001,2019):
    for day in range(1,365,8):
        
        print(str(year)+"  "+str(day))
        
        flood = np.fromfile('E:/work/publication_zhou/data/MAP4/flood_final/flood_final'+str(year)+"d"+str(day)+'.flt', dtype=np.float32)
        flood = np.reshape(flood, (2009, 764))
        
        flood_all[i, :, :] = flood
        
        i = i + 1

flood_all = np.where(flood_all > 0, 1.0, 0.0)
flood_all = np.where(flood_all < 0, -9999, flood_all)
flood_sum = np.sum(flood_all, axis=0)
flood_sum = np.where(flood_sum < 0, -9999, flood_sum)
flood_sum = flood_sum.astype(np.float32)

waterbody = np.where(flood_sum >= 560, 1, -9999) # inundation is over 250 days each year
waterbody = waterbody.astype(np.float32)
    
fileout = 'E:/work/publication_zhou/data/MAP4/flood_final/flood/waterbody.flt'
f=open(fileout,"wb")
f.write(waterbody)
f.close()     
        
