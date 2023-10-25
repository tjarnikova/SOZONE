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
import time

###
startyr = 1950
endyr = 2100

dtypeTOM = 'grid_T'
dtypeUKESM = '-TS'
### define scenarios
scendict = {
    # Baynes Sound
    '1A': {
        'hist_str': 'bc370',
        'fut_str': 'be682',
        'name': 'HIST.OZONE \n LOW TEMP.',
        'name2':'1A: NatlOzone-SSP126',
        'color':'#E8D215',
        'color2':'orange'},
    '1B': {
        'hist_str': 'bc370',
        'fut_str': 'ce417',
        'name': 'HIST. OZONE \n HIGH TEMP.',
        'name2':'1B: NatlOzone-SSP370',
        'color':'#87800A',
        'color2':'orangered'},
    '2A': {
        'hist_str': 'cj198',
        'fut_str': 'cj880',
        'name': 'FIXED OZONE \n LOW TEMP.',
        'name2':'2A: Ozone1950-SSP126',
        'color':'#2DC18E',
        'color2':'mediumseagreen'},
    '2B': {
        'hist_str': 'cj198',
        'fut_str': 'cj881',
        'name': 'FIXED OZONE \n HIGH TEMP.',
        'name2':'2B: Ozone1950-SSP370',
        'color':'#18765C',
        'color2':'green'},
    '3A': {
        'hist_str': 'cj200',
        'fut_str': 'cj484',
        'name': '1990 OZONE \n LOW TEMP.',
        'name2':'3A: Ozone1990-SSP126',
        'color':'#FF462B',
        'color2':'dodgerblue'},
    '3B': {
        'hist_str': 'cj200',
        'fut_str': 'cj504',
        'name': '1990 OZONE \n HIGH TEMP.',
        'name2':'3B: Ozone1990-SSP370',
        'color':'#822722',
        'color2':'mediumblue'}
}


### extract year lists
def make_yearlist_tom(yrst, yrend, dtype, baseDir = '/gpfs/data/greenocean/software/runs/'):
    yrs = np.arange(yrst,yrend+1,1)
    ylist = []
    for i in range(0,len(yrs)):
        ty = f'{baseDir}//ORCA2_1m_{yrs[i]}*{dtype}*.nc'
        t2 = glob.glob(ty)
        #print(t2)
        ylist.append(t2[0])
    return ylist

def make_yearlist_ukesm(yrst, yren, tscen, dtype = 'grid-T'):
    print(f'SCENARIO {tscen}')
    dslist = []

    for y in range(yrst,yren+1):
        if ((y<1990) & ((tscen == '3A') | (tscen == '3B'))):
            tstr = scendict['1A']['hist_str']
        elif y<2015:
            tstr = scendict[tscen]['hist_str']
        else:
            tstr = scendict[tscen]['fut_str']
        try:
            td = glob.glob(f'/gpfs/data/greenocean/software/resources/MEDUSA/PROC2/*{tstr}*{y}*{dtype}*')
            dslist.append(td[0])
        except:
            pass
    return dslist

### get areas
#tom12 area 
tommesh = xr.open_dataset('/gpfs/data/greenocean/software/resources/regrid/mesh_mask3_6.nc')
tommesh['area'] = tommesh.tmask[0,0,:,:] * tommesh.e1t[0,:,:] * tommesh.e2t[0,:,:]
#ukesm area 
ukmesh = xr.open_dataset('/gpfs/data/greenocean/software/resources/MEDUSA/ukesm_allscen_diadT_co2/cj198_1950/medusa_cj198o_1m_19500401-19500501_diad-T.nc')


def get_ts_3d(startyr,endyr,scenUKESM,dtypeUKESM,dtypeTOM, baseDirTOM,varUKESM,varTOM,lev = 0):
    ukesm = xr.open_mfdataset(make_yearlist_ukesm(startyr,endyr,scenUKESM,dtypeUKESM))
    tom = xr.open_mfdataset(make_yearlist_tom(startyr,endyr,dtypeTOM, baseDirTOM))
    ukesmvar = ukesm[varUKESM] #surface
    tomvar = tom[varTOM] #surface

    ukesm_fg = ukesmvar[:,lev,:,:].weighted(ukmesh['area'][:,:]).mean(dim = ['y', 'x'])
    tom_fg = tomvar[:,lev,:,:].weighted(tommesh['area'][:,:]).mean(dim = ['y', 'x'])

    print('nazdar')
    ukesm_latmax = 114
    tom_latmax = 37
    ukesm_so = ukesmvar[:,lev,0:ukesm_latmax,:].weighted(ukmesh['area'][0:ukesm_latmax,:]).mean(dim = ['y', 'x'])
    tom_so = tomvar[:,lev,0:tom_latmax,:].weighted(tommesh['area'][0:tom_latmax,:]).mean(dim = ['y', 'x'])
    print('yes')
    
    uknam_fg = f'./EXTRACT/UKESM_{scenUKESM}_{varUKESM}_fulldomain_ts_{startyr}_{endyr}.pkl'
    tomnam_fg = f'./EXTRACT/{nameTOM}_{varTOM}_fulldomain_ts_{startyr}_{endyr}.pkl'
    uknam_so = f'./EXTRACT/UKESM_{scenUKESM}_{varUKESM}_southocean-50_ts_{startyr}_{endyr}.pkl'
    tomnam_so = f'./EXTRACT/{nameTOM}_{varTOM}_southocean-50_ts_{startyr}_{endyr}.pkl'

    print(uknam_fg)
    print(tomnam_fg)

    pickle.dump(ukesm_fg, open(uknam_fg, 'wb'))
    pickle.dump(ukesm_so, open(uknam_so, 'wb'))
    pickle.dump(tom_fg, open(tomnam_fg, 'wb'))
    pickle.dump(tom_so, open(tomnam_so, 'wb'))

scenUKESM = '1A'
nameTOM = 'TOM12_TJ_1ASA'
baseDirTOM = f'/gpfs/data/greenocean/software/runs/{nameTOM}/'
varUKESM = 'thetao'
varTOM = 'votemper'
get_ts_3d(startyr,endyr,scenUKESM,dtypeUKESM,dtypeTOM, baseDirTOM,varUKESM,varTOM)
varUKESM = 'so'
varTOM = 'vosaline'
get_ts_3d(startyr,endyr,scenUKESM,dtypeUKESM,dtypeTOM, baseDirTOM,varUKESM,varTOM)

