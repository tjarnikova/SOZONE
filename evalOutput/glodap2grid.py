import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import xarray as xr
import sys
sys.path.append('/gpfs/home/mep22dku/scratch/SOZONE')
#list of models
sys.path.append('/gpfs/home/mep22dku/scratch/SOZONE/UTILS')
import lom

import warnings
from datetime import datetime
warnings.filterwarnings('ignore')
import cartopy.feature as cfeature
from importlib import reload
import matplotlib.path as mpath
import glob
import pickle
import pandas as pd
import seawater

#import mapfxn as mf
#reload(mf)
####
tmask = nc.Dataset('/gpfs/data/greenocean/software/resources/breakdown/clq_basin_masks_ORCA.nc')

maskno = np.zeros([149,182])

maskno[tmask['P1'][:] == 1] = 1.
maskno[tmask['P2'][:] == 1] = 1.15
maskno[tmask['P3'][:] == 1] = 1.3
maskno[tmask['P4'][:] == 1] = 1.45
maskno[tmask['P5'][:] == 1] = 1.6

maskno[tmask['A1'][:] == 1] = 2.
maskno[tmask['A2'][:] == 1] = 2.15
maskno[tmask['A3'][:] == 1] = 2.3
maskno[tmask['A4'][:] == 1] = 2.45
maskno[tmask['A5'][:] == 1] = 2.6


maskno[tmask['I3'][:] == 1] = 3.3
maskno[tmask['I4'][:] == 1] = 3.45
maskno[tmask['I5'][:] == 1] = 3.6


maskno[maskno == 0] = np.nan
maskno[tmask['ARCTIC'][:] == 1] = 0.5
####
df = pd.read_csv('/gpfs/home/mep22dku/scratch/SOZONE/evalOutput/datasets/GLODAPv2.2022_GLOBE_valid_DICTA_umolL.csv')
df = df.sort_values(by = 'YR')

print(df.columns)
tDIC = np.array(df['DIC'][:])
print(len(tDIC))
tALK = np.array(df['ALK'][:])


tSAL = np.array(df['SAL'][:])
tTEMP = np.array(df['TEMP'][:])
tPRES = np.array(df['PRES'][:])
tLAT = np.array(df['LAT'][:])
tLON = np.array(df['LON'][:])
tYEAR = np.array(df['YR'])
tMONTH = np.array(df['MONTH'])
tSECT = np.array(df['SECT'])
tDP = np.zeros_like(tSECT)

### seasons
tSEAS = np.zeros_like(tMONTH)
tSEAS[(tMONTH == 12) | (tMONTH <3)] = 1 #summer
tSEAS[(tMONTH >= 3) & (tMONTH <6)] = 2 #autumn
tSEAS[(tMONTH >= 6) & (tMONTH <9)] = 3 #winter
tSEAS[(tMONTH >= 9) & (tMONTH <12)] = 4
###
np.shape(np.unique(tLAT))
np.shape(tLAT)

uniq_LATS = np.unique(tLAT)

dpcount = 1
for i in range(0, len(uniq_LATS)):
    slat = uniq_LATS[i]  
    
    corlons = np.unique(tLON[tLAT == slat])
    for j in range(0, len(corlons)):
        slon = corlons[j]
        coryrs = np.unique(tYEAR[(tLAT == slat) & (tLON == slon)])
        for k in range(0, len(coryrs)):
            syr = coryrs[k]
            cormos = np.unique(tMONTH[(tLAT == slat) & (tLON == slon) & (tYEAR == syr)])
            tw = (np.shape(cormos)[0])
            for l in range(0, len(cormos)):
                smo = cormos[l]
                tDP[(tLAT == slat) & (tLON == slon) & (tYEAR == syr) & (tMONTH == smo)] = dpcount
                dpcount = dpcount+1

print('unique depth profiles, globally')
print(dpcount-1)
tDP = tDP.astype(int)

###
def haversine(lon1, lat1, lon2, lat2):
    """Calculate the great-circle distance in kilometers between two points
    on a sphere from their longitudes and latitudes.
    Reference: http://www.movable-type.co.uk/scripts/latlong.html
    :arg lon1: Longitude of point 1.
    :type lon1: float or :py:class:`numpy.ndarray`
    :arg lat1: Latitude of point 1.
    :type lat1: float or :py:class:`numpy.ndarray`
    :arg lon2: Longitude of point 2.
    :type lon2: float or :py:class:`numpy.ndarray`
    :arg lat2: Latitude of point 2.
    :type lat2: float or :py:class:`numpy.ndarray`
    :returns: Great-circle distance between two points in km
    :rtype: float or :py:class:`numpy.ndarray`
    """
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km

def find_closest(lon1, lat1):
    w = nc.Dataset('/gpfs/data/greenocean/software/runs/TOM12_TJ_1ASA/ORCA2_1m_20500101_20501231_ptrc_T.nc')
    lats = (w['nav_lat'][:])
    lons = w['nav_lon'][:]
    km = haversine(lon1, lat1, lons, lats)
    q = (np.where(km == np.min(km)))
    tY = q[0][0]
    tX = q[1][0]

    return tY, tX


## just find xs 367661 390670
chunksize = 20000
for q in range(16,19):
    ind = q*chunksize
    print(ind)
    tX = np.zeros_like(tTEMP)
    tY = np.zeros_like(tTEMP)
    tZdep = np.zeros_like(tTEMP)


    for i in range(ind,ind+chunksize):
        if i%1000 == 0:
            print(i)
        lon1 = tLON[i]; lat1 = tLAT[i]
        tY[i], tX[i] = find_closest(lon1, lat1)

    df = pd.DataFrame([tYEAR,tMONTH,tDIC,tALK,tSAL,tTEMP,tPRES,tLAT,tLON, tDP, tY, tX]).T
        # df = df.sort_values(by = tYEAR)
    df.columns = ['YR', 'MONTH', 'DIC', 'ALK', 'SAL', 'TEMP', 'PRES', 'LAT', 'LON','DP', 'Y', 'X']
    df.wheremade = 'SOpCO2Cycle/GLODAP_carbon_fullglobe.ipynb'
    df.to_csv(f'./datasets/GLODAPv2.2022_GLOBAL_valid_DICTA_umolL_togrid_part{q}.csv') 

### last lil bit
tX = np.zeros_like(tTEMP)
tY = np.zeros_like(tTEMP)
q = 19
for i in range(380000,390670):
    if i%1000 == 0:
        print(i)
    lon1 = tLON[i]; lat1 = tLAT[i]
    tY[i], tX[i] = find_closest(lon1, lat1)

df = pd.DataFrame([tYEAR,tMONTH,tDIC,tALK,tSAL,tTEMP,tPRES,tLAT,tLON, tDP, tY, tX]).T
    # df = df.sort_values(by = tYEAR)
df.columns = ['YR', 'MONTH', 'DIC', 'ALK', 'SAL', 'TEMP', 'PRES', 'LAT', 'LON','DP', 'Y', 'X']
df.wheremade = 'SOpCO2Cycle/GLODAP_carbon_fullglobe.ipynb'
df.to_csv(f'./datasets/GLODAPv2.2022_GLOBAL_valid_DICTA_umolL_togrid_part{q}.csv') 
