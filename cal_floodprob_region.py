import numpy as np
        
flood_prob_avg = np.fromfile("D:/MAP4/flood_final/stat/flooding_days_geo1.flt", dtype=np.float32)
flood_prob_avg = np.reshape(flood_prob_avg, (1703,883))

# north (34 N and north, index: 0 - )
flood_prob_all = flood_prob_avg
flood_prob_all[681:1702, : ] = -9999
flood_prob_north = flood_prob_all
flood_prob_masked = np.ma.masked_less(flood_prob_north, -1)
flood_prob_north = np.average(flood_prob_masked)

print(flood_prob_north)

# central (30 to 34 N)

flood_prob_avg = np.fromfile("D:/MAP4/flood_final/stat/flooding_days_geo1.flt", dtype=np.float32)
flood_prob_avg = np.reshape(flood_prob_avg, (1703,883))

flood_prob_all = flood_prob_avg
flood_prob_all[0:680, : ] = -9999
flood_prob_all[1481:1702, : ] = -9999

flood_prob_central = flood_prob_all
flood_prob_masked = np.ma.masked_less(flood_prob_central, -1)
flood_prob_central = np.average(flood_prob_masked)

print(flood_prob_central)

# south (29 to 30 N)

flood_prob_avg = np.fromfile("D:/MAP4/flood_final/stat/flooding_days_geo1.flt", dtype=np.float32)
flood_prob_avg = np.reshape(flood_prob_avg, (1703,883))

flood_prob_all = flood_prob_avg
flood_prob_all[0:1480, : ] = -9999
flood_prob_south = flood_prob_all
flood_prob_masked = np.ma.masked_less(flood_prob_south, -1)
flood_prob_south = np.average(flood_prob_masked)

print(flood_prob_south)






