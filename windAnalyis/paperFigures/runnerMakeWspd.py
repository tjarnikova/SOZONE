#put python script here
#point: for all taux and tauy files for the 6 UKESM scenarios, 1 PI scenario, and historic ERA5 record, remake them with a date format that allows processing with xarray
# careful, era5 respects leap years and UKESM does not

import numpy as np
import pandas as pd
import xarray as xr
import glob
from datetime import datetime

#root directory
rdir = '/gpfs/data/greenocean/software/'
dir_1H = 'resources/MetProcessed/MET_soft/hist/u-bc370_hist/'
dir_2H = 'resources/MetProcessed/MET_soft/hist/u-cj198_hist_1950start1950ozone/'
dir_3H = 'resources/MetProcessed/MET_soft/hist/u-cj200_hist_1990start1990ozone/'

dir_1FA = 'resources/MetProcessed/MET_soft/ssp126/u-be682_ssp126/'
dir_1FB = 'resources/MetProcessed/MET_soft/ssp370/u-ce417_ssp370/'

dir_2FA = 'resources/MetProcessed/MET_soft/ssp126/u-cj880_ssp126_1950start1950ozone/'
dir_2FB = 'resources/MetProcessed/MET_soft/ssp370/u-cj881_ssp370_1950start1950ozone/'

dir_3FA = 'resources/MetProcessed/MET_soft/ssp126/u-cj484_ssp126_1990start1990ozone/'
dir_3FB = 'resources/MetProcessed/MET_soft/ssp370/u-cj504_ssp370_1990start1990ozone/'

dir_PI = 'resources/MetProcessed-PI/u-aw310_pictrl/'

dir_ERA5 = 'products/ERA5_v202303_TJ/'

###
def make_wspd(tnam, yr):

    sdir = '/gpfs/data/greenocean/software/resources/windsProcessed/'
        
    #get and open
    fnamx = f'{tnam}_taux_{yr}_daily.nc'
    taux_dat = xr.open_dataset(f'{sdir}{fnamx}')

    fnamy = f'{tnam}_tauy_{yr}_daily.nc'
    tauy_dat = xr.open_dataset(f'{sdir}{fnamy}')

    fnam_tosave = f'/{sdir}/{tnam}_wspd_{yr}_daily.nc'

    taux = taux_dat.uflx.values
    tauy = tauy_dat.vflx.values

    wspd = np.sqrt(taux**2 + tauy**2)


    data_vars = {'wspd':(['time_counter', 'y', 'x'], wspd,
    {'units': 'm/s',
    'long_name':'wspd'}),
    }
    # define coordinates
    coords = {'time_counter': (['time_counter'], taux_dat.time_counter),
    'nav_lat': (['y','x'], taux_dat.nav_lat.values),
    'nav_lon': (['y','x'], taux_dat.nav_lon.values),
    }
    # define global attributes
    attrs = {'made in':'SOZONE/windAnalyis/paperFigures/runnerMakeWspd.py',
    'desc': 'wspd calculated as sqrt(taux**2 + tauy**2'
    }

    ds = xr.Dataset(data_vars=data_vars,
    coords=coords,
    attrs=attrs)
    ds.to_netcdf(fnam_tosave)


    return 

def runner(tnam, yrstart, yrend):

    for yr in range(yrstart,yrend):
        make_wspd(tnam, yr)

    return 

# tnam = 'UKESM_1H'; tdir = dir_1H; yrstart = 1940; yrend = 2015
# runner(tnam,  yrstart, yrend)

# tnam = 'UKESM_2H'; tdir = dir_1H; yrstart = 1940; yrend = 1950
# runner(tnam,  yrstart, yrend)

# tnam = 'UKESM_2H'; tdir = dir_2H; yrstart = 1950; yrend = 2015
# runner(tnam,  yrstart, yrend)

# tnam = 'UKESM_3H'; tdir = dir_1H; yrstart = 1940; yrend = 1990
# runner(tnam,  yrstart, yrend)

# tnam = 'UKESM_3H'; tdir = dir_3H; yrstart = 1990; yrend = 2015
# runner(tnam,  yrstart, yrend)

# tnam = 'UKESM_1FA'; tdir = dir_1FA; yrstart = 2015; yrend = 2101
# runner(tnam,  yrstart, yrend)

# tnam = 'UKESM_2FA'; tdir = dir_2FA; yrstart = 2015; yrend = 2101
# runner(tnam,  yrstart, yrend)

# tnam = 'UKESM_3FA'; tdir = dir_3FA; yrstart = 2015; yrend = 2101
# runner(tnam,  yrstart, yrend)

# tnam = 'UKESM_1FB'; tdir = dir_1FB; yrstart = 2015; yrend = 2101
# runner(tnam,  yrstart, yrend)

# tnam = 'UKESM_2FB'; tdir = dir_2FB; yrstart = 2015; yrend = 2101
# runner(tnam,  yrstart, yrend)

# tnam = 'UKESM_3FB'; tdir = dir_3FB; yrstart = 2015; yrend = 2101
# runner(tnam,  yrstart, yrend)

tnam = 'UKESM_PI'; tdir = dir_PI; yrstart = 1950; yrend = 2030
runner(tnam,  yrstart, yrend)

tnam = 'ERA5_v2023'; tdir = dir_ERA5; yrstart = 1940; yrend = 2023
runner(tnam,  yrstart, yrend)
