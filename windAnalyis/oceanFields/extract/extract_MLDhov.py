import numpy as np
from cmocean import cm
import netCDF4 as nc
import xarray as xr

import warnings
from datetime import datetime
warnings.filterwarnings('ignore')
from importlib import reload
import glob
import pandas as pd
import seawater
import time

dtypeTOM = 'grid_T'
dtypeUKESM = '-TS'

varUKESM = 'somxl010'
varTOM = 'mldr10_1'

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

#     tdir = 
    for y in range(yrst,yren+1):
        
        tdir = '/gpfs/data/greenocean/software/resources/MEDUSA/ukesm_allscen_gridT_mld/'
        td = glob.glob(f'{tdir}nemo_scen_{tscen}_1m_{y}_fy_grid-T.nc')
        dslist.append(td[0])
#         except:
#             pass
    return dslist

tommesh = xr.open_dataset('/gpfs/data/greenocean/software/resources/regrid/mesh_mask3_6.nc')
tommesh['area'] = tommesh.tmask[0,0,:,:] * tommesh.e1t[0,:,:] * tommesh.e2t[0,:,:]
#ukesm area 
ukmesh = xr.open_dataset('/gpfs/data/greenocean/software/resources/MEDUSA/mesh_mask_eORCA1_wrk.nc')
ukmesh['area'] = ukmesh.tmask[0,:,:] * ukmesh.e1t[:,:] * ukmesh.e2t[:,:]

def get_ts_3d(startyr,endyr,scenUKESM,dtypeUKESM,dtypeTOM, baseDirTOM,varUKESM,varTOM,lev = 0):
    ukesm = xr.open_mfdataset(make_yearlist_ukesm(startyr,endyr,scenUKESM,dtypeUKESM))
    tom = xr.open_mfdataset(make_yearlist_tom(startyr,endyr,dtypeTOM, baseDirTOM))
    ukesmvar = ukesm[varUKESM] #surface
    tomvar = tom[varTOM] #surface

    print('nazdar')
    ukesm_latmax = 140
    tom_latmax = 50
    ukesm_so = ukesmvar[:,0:ukesm_latmax,:].weighted(ukmesh['area'][0:ukesm_latmax,:]).mean(dim = ['x'])
    tom_so = tomvar[:,0:tom_latmax,:].weighted(tommesh['area'][0:tom_latmax,:]).mean(dim = ['x'])
    print('yes')
    
    rdir = '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/oceanFields/extracted-summary/'
    tnam_ukesm = f'{rdir}/MLD_{scenUKESM}_ukesm_{startyr}-{endyr}.nc'
    tnam_tom = f'{rdir}/MLD_{scenUKESM}_tom_{startyr}-{endyr}.nc'
    
    ukesm_so.to_netcdf(tnam_ukesm)
    tom_so.to_netcdf(tnam_tom)
    
    return ukesm_so, tom_so

###
startyr = 1950
endyr = 2099

extract = True
if extract:

    scenUKESM = '2B'
    nameTOM = 'TOM12_TJ_2BA6'
    baseDirTOM = f'/gpfs/data/greenocean/software/runs/{nameTOM}/'
    ukesm_so, tom_so = get_ts_3d(startyr,endyr,scenUKESM,dtypeUKESM,dtypeTOM, baseDirTOM,varUKESM,varTOM)

    scenUKESM = '3B'
    nameTOM = 'TOM12_TJ_3BA6'
    baseDirTOM = f'/gpfs/data/greenocean/software/runs/{nameTOM}/'
    ukesm_so, tom_so = get_ts_3d(startyr,endyr,scenUKESM,dtypeUKESM,dtypeTOM, baseDirTOM,varUKESM,varTOM)

    scenUKESM = '2A'
    nameTOM = 'TOM12_TJ_2AA6'
    baseDirTOM = f'/gpfs/data/greenocean/software/runs/{nameTOM}/'
    ukesm_so, tom_so = get_ts_3d(startyr,endyr,scenUKESM,dtypeUKESM,dtypeTOM, baseDirTOM,varUKESM,varTOM)

    scenUKESM = '3A'
    nameTOM = 'TOM12_TJ_3AA6'
    baseDirTOM = f'/gpfs/data/greenocean/software/runs/{nameTOM}/'
    ukesm_so, tom_so = get_ts_3d(startyr,endyr,scenUKESM,dtypeUKESM,dtypeTOM, baseDirTOM,varUKESM,varTOM)

    scenUKESM = '1A'
    nameTOM = 'TOM12_TJ_1AA6'
    baseDirTOM = f'/gpfs/data/greenocean/software/runs/{nameTOM}/'
    ukesm_so, tom_so = get_ts_3d(startyr,endyr,scenUKESM,dtypeUKESM,dtypeTOM, baseDirTOM,varUKESM,varTOM)

    scenUKESM = '1B'
    nameTOM = 'TOM12_TJ_1BA6'
    baseDirTOM = f'/gpfs/data/greenocean/software/runs/{nameTOM}/'
    ukesm_so, tom_so = get_ts_3d(startyr,endyr,scenUKESM,dtypeUKESM,dtypeTOM, baseDirTOM,varUKESM,varTOM)


