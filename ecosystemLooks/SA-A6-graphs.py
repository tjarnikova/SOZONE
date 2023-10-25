import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import warnings
from datetime import datetime
warnings.filterwarnings('ignore')
from importlib import reload
import matplotlib.path as mpath
import pandas as pd
import time
import glob
plt.rcParams.update({'font.size': 12})
font = {'family' : 'monospace',
'weight' : 'normal',
'size'   : 12}
plt.rc('font', **font)

print('init')
ml = True

def make_yearlist(yrst, yrend, tr, baseDir = '/gpfs/home/mep22dku/scratch/SOZONE/ecosystemLooks/depthint-ptrc'):
    yrs = np.arange(yrst,yrend+1,1)
    ylist = []
    for i in range(0,len(yrs)):
        ty = f'{baseDir}/TOM12_TJ_{tr}-ptrc-{yrs[i]}.nc'
        t2 = glob.glob(ty)
        #print(t2)
        ylist.append(t2[0])
    return ylist

fact = 0.9
fig, axs = plt.subplots(6,2, figsize=(15*fact, 17*fact), facecolor='w', edgecolor='k')
axs = axs.ravel()

p1AA6 = xr.open_mfdataset(make_yearlist(1950,2099,'1AA6'))
p1BA6 = xr.open_mfdataset(make_yearlist(1950,2099,'1BA6'))

tits = ['Arctic, 1A (low temp)', 'Arctic, 1B (high temp)',\
       'Subarctic, 1A (low temp)', 'Subarctic, 1B (high temp)',
       'North. Midlats, 1A (low temp)', 'North. Midlats, 1B (high temp)',
       'South. Midlats, 1A (low temp)', 'South. Midlats, 1B (high temp)',
       'Northern SO, 1A (low temp)', 'Northern SO, 1B (high temp)',
       'Southern Ocean, 1A (low temp)', 'Southern Ocean, 1B (high temp)',]

for i in range(0,12):
    axs[i].grid()
    axs[i].set_xlim([1950,2099])
    axs[i].set_title(tits[i])

if ml:
    for i in range(1,7):
        DIA = p1AA6.DIA.sel(lat_band = i).groupby('time_counter.year').mean()
        MIX = p1AA6.MIX.sel(lat_band = i).groupby('time_counter.year').mean()
        COC = p1AA6.COC.sel(lat_band = i).groupby('time_counter.year').mean()
        PHA = p1AA6.PHA.sel(lat_band = i).groupby('time_counter.year').mean()
        FIX = p1AA6.FIX.sel(lat_band = i).groupby('time_counter.year').mean()
        PIC = p1AA6.PIC.sel(lat_band = i).groupby('time_counter.year').mean()
        BAC = p1AA6.BAC.sel(lat_band = i).groupby('time_counter.year').mean()

        axs[(i-1)*2].plot(DIA.year,DIA, color = 'darkorchid', label = 'DIA')
        axs[(i-1)*2].plot(DIA.year,DIA+MIX, color = 'mediumblue', label = 'MIX')
        axs[(i-1)*2].plot(DIA.year,DIA+MIX+COC, color = 'steelblue', label = 'COC')
        axs[(i-1)*2].plot(DIA.year,DIA+MIX+COC+PHA, color = 'limegreen', label = 'PHA')
        axs[(i-1)*2].plot(DIA.year,DIA+MIX+COC+PHA+FIX, color = 'y', label = 'FIX')
        axs[(i-1)*2].plot(DIA.year,DIA+MIX+COC+PHA+FIX+PIC, color = 'orange', label = 'PIC')
        axs[(i-1)*2].plot(DIA.year,DIA+MIX+COC+PHA+FIX+PIC+BAC, color = 'r', label = 'BAC')

        axs[(i-1)*2].fill_between(DIA.year,DIA, 0, color = 'darkorchid', alpha = 0.2)
        axs[(i-1)*2].fill_between(DIA.year,DIA+MIX, DIA, color = 'mediumblue', alpha = 0.2)
        axs[(i-1)*2].fill_between(DIA.year,DIA+MIX+COC, DIA+MIX, color = 'steelblue', alpha = 0.2)
        axs[(i-1)*2].fill_between(DIA.year,DIA+MIX+COC+PHA, DIA+MIX+COC, color = 'limegreen', alpha = 0.2)
        axs[(i-1)*2].fill_between(DIA.year,DIA+MIX+COC+PHA+FIX, DIA+MIX+COC+PHA, color = 'y', alpha = 0.2)
        axs[(i-1)*2].fill_between(DIA.year,DIA+MIX+COC+PHA+FIX+PIC, DIA+MIX+COC+PHA+FIX, color = 'orange', alpha = 0.2)
        axs[(i-1)*2].fill_between(DIA.year,DIA+MIX+COC+PHA+FIX+PIC+BAC, DIA+MIX+COC+PHA+FIX+PIC, color = 'r', alpha = 0.2)

    for i in range(1,7):
        DIA = p1BA6.DIA.sel(lat_band = i).groupby('time_counter.year').mean()
        MIX = p1BA6.MIX.sel(lat_band = i).groupby('time_counter.year').mean()
        COC = p1BA6.COC.sel(lat_band = i).groupby('time_counter.year').mean()
        PHA = p1BA6.PHA.sel(lat_band = i).groupby('time_counter.year').mean()
        FIX = p1BA6.FIX.sel(lat_band = i).groupby('time_counter.year').mean()
        PIC = p1BA6.PIC.sel(lat_band = i).groupby('time_counter.year').mean()
        BAC = p1BA6.BAC.sel(lat_band = i).groupby('time_counter.year').mean()

        axs[(i-1)*2+1].plot(DIA.year,DIA, color = 'darkorchid')
        axs[(i-1)*2+1].plot(DIA.year,DIA+MIX, color = 'mediumblue')
        axs[(i-1)*2+1].plot(DIA.year,DIA+MIX+COC, color = 'steelblue')
        axs[(i-1)*2+1].plot(DIA.year,DIA+MIX+COC+PHA, color = 'limegreen')
        axs[(i-1)*2+1].plot(DIA.year,DIA+MIX+COC+PHA+FIX, color = 'y')
        axs[(i-1)*2+1].plot(DIA.year,DIA+MIX+COC+PHA+FIX+PIC, color = 'orange')
        axs[(i-1)*2+1].plot(DIA.year,DIA+MIX+COC+PHA+FIX+PIC+BAC, color = 'r')

        axs[(i-1)*2+1].fill_between(DIA.year,DIA, 0, color = 'darkorchid', alpha = 0.2)
        axs[(i-1)*2+1].fill_between(DIA.year,DIA+MIX, DIA, color = 'mediumblue', alpha = 0.2)
        axs[(i-1)*2+1].fill_between(DIA.year,DIA+MIX+COC, DIA+MIX, color = 'steelblue', alpha = 0.2)
        axs[(i-1)*2+1].fill_between(DIA.year,DIA+MIX+COC+PHA, DIA+MIX+COC, color = 'limegreen', alpha = 0.2)
        axs[(i-1)*2+1].fill_between(DIA.year,DIA+MIX+COC+PHA+FIX, DIA+MIX+COC+PHA, color = 'y', alpha = 0.2)
        axs[(i-1)*2+1].fill_between(DIA.year,DIA+MIX+COC+PHA+FIX+PIC, DIA+MIX+COC+PHA+FIX, color = 'orange', alpha = 0.2)
        axs[(i-1)*2+1].fill_between(DIA.year,DIA+MIX+COC+PHA+FIX+PIC+BAC, DIA+MIX+COC+PHA+FIX+PIC, color = 'r', alpha = 0.2)  

    axs[2].legend(ncol = 3, loc = 'best', fontsize = 10)
    
plt.suptitle('A6 series (CAL12)', fontsize = 18)
plt.tight_layout()
fig.savefig('./plots/Phyto-A6.jpg')