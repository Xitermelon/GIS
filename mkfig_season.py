import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np

flood_season = np.ones(( 46, 1703, 883), dtype=np.float32)

i = 0
for day in range(1, 365, 8):

    temp = np.fromfile("D:/LMAV_flooding/data/MAP/flood_final/results/seasonality/geo1_avg_d"+str(day)+".flt", dtype=np.float32)   
    flood_season[i, :, : ] = np.reshape(temp, (1703, 883))
    i = i + 1

flood_season = np.where(flood_season < 0, 0, flood_season)


flood_season_lonsum = np.sum(flood_season, axis=2)
flood_season_lonsum_timesum = np.sum(flood_season_lonsum, axis=0)
flood_season_lonsum_timesum = np.where(flood_season_lonsum_timesum == 0, -1.0, flood_season_lonsum_timesum )

flood_season_frac = np.ones(( 46, 1703), dtype=np.float32)

i = 0
for day in range(1, 365, 8):

    flood_season_frac[i, :] = flood_season_lonsum[i, :] * 1.0 / flood_season_lonsum_timesum
    i = i + 1


levels = MaxNLocator(nbins=10).tick_values(flood_season_frac.min(), 0.10)

cmap = plt.get_cmap('RdYlBu')

lat, time = np.mgrid[slice(37.406, 28.891, -0.005), slice(5, 369, 8)]

ax1 = plt.axes()

cf = ax1.contourf( time, lat,  np.swapaxes(flood_season_frac, 0, 1), levels=levels, cmap=cmap)
plt.colorbar(cf, ax=ax1)
plt.title('')
plt.xlabel(r"Day of Year (DOY)")
plt.ylabel(r"Latitude ($^{o}$N)")

#plt.show()
plt.savefig(r"D:\LMAV_flooding\data\MAP\flood_final\results\figure\seasonality.tif", dpi=300)
