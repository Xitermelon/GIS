import numpy as np

flood_ann_all = np.ones(( 18, 2009, 764), dtype=np.float32)

i = 0

for year in range(2001,2019):
    flood_ann = np.fromfile('D:/LMAV_flooding/data/MAP/flood_final/flood_ann_final'+str(year)+'.flt',dtype=np.float32)
    flood_ann = np.reshape(flood_ann,(2009,764))
    
    flood_ann_all[i, :, :] = flood_ann
    i = i + 1
    
    
flood_ann_sum = np.sum(flood_ann_all, axis=0)
    
flood_frequency = flood_ann_sum / 18.0 * 100
flood_frequency = flood_frequency.astype(np.float32)

f = open("D:/LMAV_flooding/data/MAP/flood_final/results/flood_frequency.flt", "wb")    
f.write(flood_frequency)
f.close()      
    
