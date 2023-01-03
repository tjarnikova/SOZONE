import numpy as np
from cmocean import cm
import cartopy as cp
import cartopy.crs as ccrs
import netCDF4 as nc
import matplotlib.pyplot as plt
import xarray as xr
import sys
sys.path.append('/gpfs/home/mep22dku/scratch/SOZONE')
#list of models
sys.path.append('/gpfs/home/mep22dku/scratch/SOZONE/UTILS')
import lom
import utils as ut

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

w = glob.glob('./argo_processed/CHLMAX_*')
df1 = pd.read_csv(w[0])
df2 = pd.read_csv(w[1])

# print(df1)
# print(df2)
dfs = []
# df = pd.concat([df1, df2])
for i in range(0,len(w)):
    dfs.append(pd.read_csv(w[i]))
    
masterdf = pd.concat(dfs)

print('done nasterdf')

lat = np.array(masterdf['lat'])
lon = np.array(masterdf['lon'])
Y = np.zeros_like(lat)
X = np.zeros_like(lat)
for i in range(0,30000):
    if i%1000 == 0:
        print(i)
    Y[i], X[i] = ut.find_closest(lon[i], lat[i])

df = pd.DataFrame([Y,X]).T
            # df = df.sort_values(by = tYEAR)
df.columns = ['Y','X']
df.wheremade = 'evalOutput/BGC_subsurfacechla.ipynb'
df.to_csv(f'./argo_processed/chl_yx_0_30000.csv')

lat = np.array(masterdf['lat'])
lon = np.array(masterdf['lon'])
Y = np.zeros_like(lat)
X = np.zeros_like(lat)
for i in range(30000,len(lat)):
    if i%1000 == 0:
        print(i)
    Y[i], X[i] = ut.find_closest(lon[i], lat[i])

df = pd.DataFrame([Y,X]).T
            # df = df.sort_values(by = tYEAR)
df.columns = ['Y','X']
df.wheremade = 'evalOutput/BGC_subsurfacechla.ipynb'
df.to_csv(f'./argo_processed/chl_yx_30000_end.csv')