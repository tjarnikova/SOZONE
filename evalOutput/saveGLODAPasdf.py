## save data

import numpy as np
from cmocean import cm
import cartopy as cp
import cartopy.crs as ccrs
import netCDF4 as nc
import matplotlib.pyplot as plt
import xarray as xr
import sys
sys.path.append('/gpfs/home/mep22dku/scratch/SOZONE')

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


print('starting')

runhorse = True
if runhorse:

    tdir = '/gpfs/data/greenocean/observations/'
    print(tdir)
    glodap = pd.read_csv(f'{tdir}GLODAPv2.2022_Merged_Master_File.csv')
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    #print(glodap.head())
    print('managed2readcsv')
    
    tDIC = np.array(glodap['G2tco2'][:])
    tco2f = np.array(glodap['G2tco2f'][:])
    tco2qc = np.array(glodap['G2tco2qc'][:])

    tALK = np.array(glodap['G2talk'][:])
    talkf = np.array(glodap['G2talkf'][:])
    tco2f = np.array(glodap['G2tco2f'][:])
    tCAST = np.array(glodap['G2cast'][:])
    tSAL = np.array(glodap['G2salinity'][:])
    tTEMP = np.array(glodap['G2temperature'][:])
    tPRES = np.array(glodap['G2pressure'][:])
    tLAT = np.array(glodap['G2latitude'][:])
    tLON = np.array(glodap['G2longitude'][:])
    tYEAR = np.array(glodap['G2year'])
    tMONTH = np.array(glodap['G2month'])
    tSTATION = np.array(glodap['G2station'])
    tCRUISE = np.array(glodap['G2cruise'])
    #tAOU = np.array(glodap['aou'][:])

    dens = seawater.dens(tSAL,tTEMP,tPRES)
    tDIC=tDIC*dens/1000
    tALK=tALK*dens/1000

    tfilt = (tco2f == 2) & (talkf == 2) & ~np.isnan(tDIC) & ~np.isnan(tALK) 
    tDIC_SO = tDIC[tfilt]
    print(np.nanmin(tDIC_SO))
    print(np.nanmax(tDIC_SO))
    tco2f_SO =  tco2f[tfilt]
    tco2qc_SO = tco2qc[tfilt]
    tALK_SO = tALK[tfilt]
    talkf_SO = talkf[tfilt]
    tco2f_SO = tco2f[tfilt]

    tSAL_SO = tSAL[tfilt]
    tTEMP_SO = tTEMP[tfilt]
    tPRES_SO = tPRES[tfilt]
    tLAT_SO = tLAT[tfilt]
    tLON_SO = tLON[tfilt]
    tYEAR_SO = tYEAR[tfilt]
    tMONTH_SO = tMONTH[tfilt]
    tSTATION_SO = tSTATION[tfilt]
    tCAST_SO = tCAST[tfilt]
    tCRUISE_SO = tCRUISE[tfilt]
    tSECT_SO = np.zeros_like(tLON_SO)
    tSECT_SO[(tLON_SO <= -67) | (tLON_SO > 150)] = 4 #pacific
    tSECT_SO[(tLON_SO <= 20) &(tLON_SO > -67)] = 2 #atl
    tSECT_SO[(tLON_SO > 20) &(tLON_SO <= 150)] = 3 #indian

    print(np.shape(tYEAR_SO))
    df = pd.DataFrame([tYEAR_SO,tMONTH_SO,tDIC_SO,tALK_SO,tSAL_SO,tTEMP_SO,tPRES_SO,tLAT_SO,tLON_SO,tSECT_SO, tSTATION_SO, tCAST_SO, tCRUISE_SO]).T
    # df = df.sort_values(by = tYEAR_SO)
    df.columns = ['YR', 'MONTH', 'DIC', 'ALK', 'SAL', 'TEMP', 'PRES', 'LAT', 'LON', 'SECT', 'STATION', 'CAST', 'CRUISE']
    tnam = './datasets/GLODAPv2.2022_GLOBE_valid_DICTA_umolL.csv'
    df.to_csv(tnam)