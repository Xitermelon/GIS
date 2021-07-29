import numpy as np
import scipy.signal
import shutil

dvel_all = np.ones((828, 2009, 764), dtype=np.float32)

i = 0
        
for year in range(2001, 2019):
    for day in range(1, 365, 8):
            
        print("D:/LMAV_flooding/data/DVEL/dvel"+str(year)+"d"+str(day)+".flt")
            
        dvel = np.fromfile("D:/LMAV_flooding/data/DVEL/dvel"+str(year)+"d"+str(day)+".flt", dtype=np.float32) 
        dvel2 = np.reshape(dvel, (2009, 764))
        
        dvel_all[i, :, :] = dvel2
        
        i = i + 1
        
for i in range(2, 828):
    dvel_all[i-1, :, :] = np.where(dvel_all[i-1, :, :] > 1 , (dvel_all[i-2, :, :] + dvel_all[i, :, :]) / 2.0 , dvel_all[i-1, :, :])
    dvel_all[i-1, :, :] = np.where(dvel_all[i-1, :, :] < -1 , (dvel_all[i-2, :, :] + dvel_all[i, :, :]) / 2.0 , dvel_all[i-1, :, :])
    

dvel2_all = np.full((828, 2009, 764), -9999.0, dtype=np.float32)
     
   
for irow in range(1, 2010):
    for icol in range(1, 765):
        if dvel_all[0, irow-1, icol-1] >= -1 and dvel_all[0, irow-1, icol-1] <= 1:
            
            print(str(irow)+"  "+str(icol))
            
            y = dvel_all[:, irow-1, icol-1]
            y_filter = scipy.signal.savgol_filter(y, 11, 3) # window size 5, polynomial order 3
            
            dvel2_all[:, irow-1, icol-1] = y_filter


i = 0
        
for year in range(2001, 2019):
    for day in range(1, 365, 8):

        fileout = "D:/LMAV_flooding/data/DVEL/filter/smoothdvel"+str(year)+"d"+str(day)+".flt"
        
        f=open(fileout,"wb")
        
        f.write(dvel2_all[i, :, :])
        
        i = i + 1
            
        f.close() 
        
        shutil.copyfile("D:/LMAV_flooding/data/DVEL/dvel"+str(year)+"d"+str(day)+".hdr", "D:/LMAV_flooding/data/DVEL/filter/smoothdvel"+str(year)+"d"+str(day)+".hdr")
        shutil.copyfile("D:/LMAV_flooding/data/DVEL/dvel"+str(year)+"d"+str(day)+".prj", "D:/LMAV_flooding/data/DVEL/filter/smoothdvel"+str(year)+"d"+str(day)+".prj")
        