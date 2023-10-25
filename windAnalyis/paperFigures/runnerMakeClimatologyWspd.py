#put python script here
#point: make lats and lons in a format that is usable by cdo regrid

import numpy as np
import pandas as pd
import xarray as xr
import glob
from datetime import datetime


def make_yearlist(yrst, yrend, tr = 'UKESM'):
    
    baseDir = '/gpfs/data/greenocean/software/resources/windsProcessed/'
    yrs = np.arange(yrst,yrend+1,1)
    ylist = []
    for i in range(0,len(yrs)):
        yr = yrs[i]
        if tr == 'UKESM':
            if yr <2015:
                scen = '1H'
            else:
                scen = '1FA'
            ty = f'{baseDir}/{tr}_{scen}*wspd*{yrs[i]}*regridded.nc'
            t2 = glob.glob(ty)
        if tr == 'ERA5':
            ty = f'{baseDir}/{tr}_v2023*wspd*{yrs[i]}*regridded.nc'
            t2 = glob.glob(ty)
        #print(t2[0])
        ylist.append(t2[0])
    return ylist

tylist_ukesm = make_yearlist(1940,2019)
w = xr.open_mfdataset(tylist_ukesm)

FY = w.wspd.groupby('time_counter.year').mean().mean(dim = ['year'])
DJF = w.wspd.sel(time_counter=(w['time_counter.season'] == 'DJF')).groupby('time_counter.year').mean().mean(dim = ['year'])
MAM = w.wspd.sel(time_counter=(w['time_counter.season'] == 'MAM')).groupby('time_counter.year').mean().mean(dim = ['year'])
JJA = w.wspd.sel(time_counter=(w['time_counter.season'] == 'JJA')).groupby('time_counter.year').mean().mean(dim = ['year'])
SON = w.wspd.sel(time_counter=(w['time_counter.season'] == 'SON')).groupby('time_counter.year').mean().mean(dim = ['year'])

wspd_save = np.zeros([5,180,360])
wspd_save[0,:,:] = FY
wspd_save[1,:,:] = DJF
wspd_save[2,:,:] = MAM
wspd_save[3,:,:] = JJA
wspd_save[4,:,:] = SON

savenam = '/gpfs/data/greenocean/software/resources/windsProcessed/UKESM_1H_wspd_clim_1940-2020_regrid.nc'

data_vars = {'wspd':(['season', 'lat', 'lon'], wspd_save,
{'units': 'm/s',
'long_name':'wind speed'}),
}
# define coordinates
coords = {'season': (['season'], ['FY','DJF','MAM','JJA','SON']),
    
'lat': (['lat'], w.lat),
'lon': (['lon'], w.lon),
}
# define global attributes
attrs = {'made in':'SOZONE/windAnalyis/paperFigures/runnerMakeClimatologyWspd.py',
'desc': 'yearly medusa files, saving only variables of interest'
}
ds = xr.Dataset(data_vars=data_vars,
coords=coords,
attrs=attrs)
ds.to_netcdf(savenam)


#####
tylist_era = make_yearlist(1940,2019, tr = 'ERA5')
w = xr.open_mfdataset(tylist_era)

FY = w.wspd.groupby('time_counter.year').mean().mean(dim = ['year'])
DJF = w.wspd.sel(time_counter=(w['time_counter.season'] == 'DJF')).groupby('time_counter.year').mean().mean(dim = ['year'])
MAM = w.wspd.sel(time_counter=(w['time_counter.season'] == 'MAM')).groupby('time_counter.year').mean().mean(dim = ['year'])
JJA = w.wspd.sel(time_counter=(w['time_counter.season'] == 'JJA')).groupby('time_counter.year').mean().mean(dim = ['year'])
SON = w.wspd.sel(time_counter=(w['time_counter.season'] == 'SON')).groupby('time_counter.year').mean().mean(dim = ['year'])

wspd_save = np.zeros([5,180,360])
wspd_save[0,:,:] = FY
wspd_save[1,:,:] = DJF
wspd_save[2,:,:] = MAM
wspd_save[3,:,:] = JJA
wspd_save[4,:,:] = SON

savenam = '/gpfs/data/greenocean/software/resources/windsProcessed/ERA5_wspd_clim_1940-2020_regrid.nc'

data_vars = {'wspd':(['season', 'lat', 'lon'], wspd_save,
{'units': 'm/s',
'long_name':'wind speed'}),
}
# define coordinates
coords = {'season': (['season'], ['FY','DJF','MAM','JJA','SON']),
    
'lat': (['lat'], w.lat),
'lon': (['lon'], w.lon),
}
# define global attributes
attrs = {'made in':'SOZONE/windAnalyis/paperFigures/runnerMakeClimatologyWspd.py',
'desc': 'yearly medusa files, saving only variables of interest'
}
ds = xr.Dataset(data_vars=data_vars,
coords=coords,
attrs=attrs)
ds.to_netcdf(savenam)