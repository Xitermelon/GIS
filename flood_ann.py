
import numpy as np

i = 0
flood_all = np.ones(( 828, 2009, 764), dtype=np.float32)


for year in range(2001,2019):
    for day in range(1,365,8):
        
        print(str(year)+"  "+str(day))
        
        flood = np.fromfile('E:/work/publication_zhou/data/MAP4/flood_final/flood/new_flood_final'+str(year)+"d"+str(day)+'.flt', dtype=np.float32)
        flood = np.reshape(flood, (2009, 764))
        
        flood_all[i, :, :] = flood
        
        i = i + 1
        

waterbody = np.fromfile("E:/work/publication_zhou/data/MAP4/flood_final/flood/waterbody.flt", dtype=np.float32)
waterbody = np.reshape(waterbody, (2009, 764))

for year in range(2001,2019):
    
    start1 = (year - 2001) * 46
    end1 =  (year - 2001) * 46 + 45
    
    flood_ann_all = flood_all[start1:end1, :, :]
    
    flood_ann_sum = np.sum(flood_ann_all, axis=0)
    
    flood_ann = np.where(flood_ann_sum > 0, 1.0, 0.0)
    flood_ann = np.where( (waterbody == 1.0) & (flood_ann == 1.0), 3, flood_ann)
    flood_ann = np.where(flood_ann_sum < 0, -9999, flood_ann)
    
    flood_ann = flood_ann.astype(np.float32)
    
    fileout = 'E:/work/publication_zhou/data/MAP4/flood_final/flood/new_flood_ann_final'+str(year)+".flt"
    f=open(fileout,"wb")
    f.write(flood_ann)
    f.close()     
