import numpy as np

flood_all = np.ones(( 828, 2009, 764), dtype=np.float32)

i = 0

for year in range(2001,2019):
    for day in range(1,365,8):
        print(str(year)+"  "+str(day))
        
        flood = np.fromfile("D:/LMAV_flooding/data/MAP/flood_final/flood_final"+str(year)+"d"+str(day)+".flt", dtype=np.float32)
        flood = np.reshape(flood, (2009, 764))
        
        flood_all[i, :, :] = flood
        
        i = i + 1    
        
flood_all = np.where(flood_all > 0, 1.0, 0.0)
flood_all = flood_all.astype(np.float32)        

flood_days = np.ones(( 18, 2009, 764), dtype=np.float32)
        

for year in range(2001,2019):    
    
    start1 = (year - 2001) * 46
    end1 =  (year - 2001) * 46 + 45
    
    flood_ann = flood_all[start1:end1, :, :]    
    flood_days[year-2001, : , :] = np.sum(flood_ann , axis = 0) * 8

flood_days_avg = np.average(flood_days , axis = 0)
        
f = open("D:/LMAV_flooding/data/MAP/flood_final/results/flood_days.flt", "wb")    
f.write(flood_days_avg)
f.close()      
    