# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
from pyhdf.SD import SD, SDC
import os



directory = "D:/DATA2/"

for filename in os.listdir(directory):
    
    if filename.endswith(".hdf"):

        print ("D:/DATA2/"+filename)
        
        year = filename[9:13]
        day = filename[13:16]
        v = filename[21:23]
        h = filename[18:20]
        
        
        try:
            file = SD("D:/DATA2/"+filename,SDC.READ)
            datasets_dic = file.datasets()
      
            sds_obj1 = file.select('sur_refl_b01')
            sds_obj2 = file.select('sur_refl_b02')
            sds_obj3 = file.select('sur_refl_b03')
           
            data1 = sds_obj1.get()
            data2 = sds_obj2.get()
            data3 = sds_obj3.get()
           
            b1 = data1.astype(np.float32) / 10000.0
            b2 = data2.astype(np.float32) / 10000.0
            b3 = data3.astype(np.float32) / 10000.0
           
           
            evi = 2.5*(b2-b1)/((b2+6*b1-7.5*b3+1)+0.0000000001)
           
            f=open("evi"+year+"d"+day+"h"+h+"v"+v+".flt","wb")
            mydata= np.asarray(evi, dtype=np.float32)
        
            f.write(mydata)
            f.close()
            
            
            
            
            
        except:
            print("error")
            
        
            
        
        
    
