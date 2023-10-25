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
start = 1950
end = 2100

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


def make_yearlist_tom(yrst, yrend, dtype, baseDir = '/gpfs/data/greenocean/software/runs/TOM12_TJ_1ASA'):
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

    for y in range(yrst,yren):
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
            #print(f'FAIL {tscen},{tstr}, {y}')
    return dslist

#tom12
tmesh = xr.open_dataset('/gpfs/data/greenocean/software/resources/regrid/mesh_mask3_6.nc')
tmesh['csize'] = tmesh.tmask[0,0,:,:] * tmesh.e1t[0,:,:] * tmesh.e2t[0,:,:]

ukmesh = xr.open_dataset('/gpfs/data/greenocean/software/resources/MEDUSA/mesh_mask_eORCA1_wrk.nc')
ukmesh['area'] = ukmesh.tmask[0,:,:] * ukmesh.e1t[:,:] * ukmesh.e2t[:,:]
print('lol yes the area is correct now')

def get_hovmols(ukscen,tomscen,start,end):
    ukesm = xr.open_mfdataset(make_yearlist_ukesm(start,end+1,ukscen, dtype = 'co2'))
    print(ukesm)
    tom = xr.open_mfdataset(make_yearlist_tom(start,end,'diad_T', baseDir = tomscen))
    tom['time_counter'] = \
    pd.date_range(f"{start}/01/01",f"{end+1}/01/01",freq='M',closed='left')

    varTOM = 'pCO2'
    varUKESM = 'OCN_PCO2'
    ukesm_fg = ukesm[varUKESM].weighted(ukmesh['area']).mean(dim = ['x'])
    tom_fg = tom[varTOM].weighted(tmesh['csize']).mean(dim = ['x'])
    uknam_fg = f'./EXTRACT/UKESM_{scenUKESM}_{varUKESM}_lathovmoller_{start}_{end}.pkl'
    tomnam_fg = f'./EXTRACT/{nameTOM}_{varTOM}_lathovmoller_{start}_{end}.pkl'
    pickle.dump(ukesm_fg, open(uknam_fg, 'wb'))
    pickle.dump(tom_fg, open(tomnam_fg, 'wb'))
    
    varTOM = 'Cflx'
    varUKESM = 'CO2FLUX'
    ukesm_fg = ukesm[varUKESM].weighted(ukmesh['area']).mean(dim = ['x'])
    tom_fg = tom[varTOM].weighted(tmesh['csize']).mean(dim = ['x'])
    uknam_fg = f'./EXTRACT/UKESM_{scenUKESM}_{varUKESM}_lathovmoller_{start}_{end}.pkl'
    tomnam_fg = f'./EXTRACT/{nameTOM}_{varTOM}_lathovmoller_{start}_{end}.pkl'
    pickle.dump(ukesm_fg, open(uknam_fg, 'wb'))
    pickle.dump(tom_fg, open(tomnam_fg, 'wb'))
    
    print(tomnam_fg)

scenUKESM = '1A'
nameTOM = 'TOM12_TJ_1ASA'
tomscen =  f'/gpfs/data/greenocean/software/runs/{nameTOM}'
get_hovmols(scenUKESM,tomscen,start,end)

scenUKESM = '1B'
nameTOM = 'TOM12_TJ_1BSA'
tomscen =  f'/gpfs/data/greenocean/software/runs/{nameTOM}'
get_hovmols(scenUKESM,tomscen,start,end)

scenUKESM = '2A'
nameTOM = 'TOM12_TJ_2ASA'
tomscen =  f'/gpfs/data/greenocean/software/runs/{nameTOM}'
get_hovmols(scenUKESM,tomscen,start,end)

scenUKESM = '2B'
nameTOM = 'TOM12_TJ_2BSA'
tomscen =  f'/gpfs/data/greenocean/software/runs/{nameTOM}'
get_hovmols(scenUKESM,tomscen,start,end)

scenUKESM = '3A'
nameTOM = 'TOM12_TJ_3ASA'
tomscen =  f'/gpfs/data/greenocean/software/runs/{nameTOM}'
get_hovmols(scenUKESM,tomscen,start,end)

scenUKESM = '3B'
nameTOM = 'TOM12_TJ_3BSA'
tomscen =  f'/gpfs/data/greenocean/software/runs/{nameTOM}'
get_hovmols(scenUKESM,tomscen,start,end)