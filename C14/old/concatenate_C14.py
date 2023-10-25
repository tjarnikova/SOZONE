import numpy as np
from cmocean import cm
import cartopy as cp
import cartopy.crs as ccrs
import netCDF4 as nc
import matplotlib.pyplot as plt
import xarray as xr
import sys

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
import time

print('pojd mi')

def make_yearlist(yrst, yrend, dtype, tr, baseDir):
    yrs = np.arange(yrst,yrend+1,1)
    ylist = []
    for i in range(0,len(yrs)):
        ty = f'{baseDir}/{tr}/ORCA2_1m_{yrs[i]}*{dtype}*.nc'
        t2 = glob.glob(ty)
        #print(t2)
        ylist.append(t2[0])
    return ylist


def conc_c14(yrst, yren, name, baseDir):
    GEA0_list = make_yearlist(yrst, yren, 'diad', name, baseDir)
    w = xr.open_mfdataset(GEA0_list)
    print(f'concatenating {name}')
    tnam = ['PPINT','Oflx','PICflx','D14RES','D14PRO',\
           'prococ', 'proara', 'GRAPTE', 'GRAGEL', 'ExpARA', 'ExpCO3',\
           'discarb','sinksil','vsink','DELO2','denitr','nitrfix',\
           'GRAMACPHY','GRAMESPHY','GRAMICPHY','Herbiv','Carniv',\
           'Detrit','EXP','GRAMIC','GRAMES','GRAMAC','PPTDOC',\
           'PPT','TChl','Detrit','DOCTRP']
    w2 = w.drop_vars(tnam)
    w2.to_netcdf(f'{baseDir}/{name}/C14-diad-{yrst}-{yren}.nc')

    GEA0_list = make_yearlist(yrst, yren, 'ptrc', name, baseDir)
    w = xr.open_mfdataset(GEA0_list)
    tnam = ['Alkalini','O2','DIC','PIIC','NO3',\
           'Si', 'PO4', 'Fer', 'DOC', 'CaCO3', 'ARA',\
           'POC','GOC','BAC','PRO','PTE','MES',\
           'GEL','MAC','DIA','MIX','COC',\
           'PIC','PHA','FIX','BSi','GON','C11']
    w2 = w.drop_vars(tnam)
    w2.to_netcdf(f'{baseDir}/{name}/C14-ptrc-{yrst}-{yren}.nc')

    
yrst = 1959;
yren = 2003;
baseDir = '/gpfs/data/greenocean/software/runs/'

name = 'TOM12_TJ_GEA0'
conc_c14(yrst, yren, name, baseDir)
name = 'TOM12_TJ_GEB0'
conc_c14(yrst, yren, name, baseDir)
name = 'TOM12_TJ_GEC0'
conc_c14(yrst, yren, name, baseDir)
name = 'TOM12_TJ_GED0'
conc_c14(yrst, yren, name, baseDir)