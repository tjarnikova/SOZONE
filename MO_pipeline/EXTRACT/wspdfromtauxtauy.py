import numpy as np
import pandas as pd
import xarray as xr
import glob
from datetime import datetime
 
runhorse = False
runhorse2 = True
rdir = '/gpfs/data/greenocean/software/resources/MetProcessed/MET_soft/'
dir_1H = 'hist/u-bc370_hist/'
dir_2H = 'hist/u-cj198_hist_1950start1950ozone/'
dir_3H = 'hist/u-cj200_hist_1990start1990ozone/'

dir_1FA = 'ssp126/u-be682_ssp126/'
dir_1FB = 'ssp370/u-ce417_ssp370/'

dir_2FA = 'ssp126/u-cj880_ssp126_1950start1950ozone/'
dir_2FB = 'ssp370/u-cj881_ssp370_1950start1950ozone/'

dir_3FA = 'ssp126/u-cj484_ssp126_1990start1990ozone/'
dir_3FB = 'ssp370/u-cj504_ssp370_1990start1990ozone/'
    #rdir = '/gpfs/home/mep22dku/scratch/u-aw310_pictrl/' #preindustrial control

def make_wspd(yr):
    
    sdir = '/gpfs/home/mep22dku/scratch/u-aw310_pictrl_redo/'
    yrpi = yr + 270
    #get and open
    fnam = f'taux_{yrpi}_daily.nc'
    taux_dat = xr.open_dataset(f'{sdir}{fnam}')

    fnam = f'tauy_{yrpi}_daily.nc'
    tauy_dat = xr.open_dataset(f'{sdir}{fnam}')

    fnam_tosave = f'/gpfs/data/greenocean/software/resources/winds_gooddates/UKESM_PI_wspd_{yr}_daily.nc'

    taux = taux_dat.uflx.values
    tauy = tauy_dat.vflx.values

    wspd = np.sqrt(taux**2 + tauy**2)

    times = pd.date_range(f"{yr}/01/01",f"{yr+1}/01/01",freq='D',closed='left')
    times = times[~((times.month == 2) & (times.day == 29))] #exclude leap yrs; nvm don't have to

    data_vars = {'wspd':(['time_counter', 'y', 'x'], wspd,
    {'units': 'm/s',
    'long_name':'wspd'}),
    }
    # define coordinates
    coords = {'time_counter': (['time_counter'], times),
    'nav_lat': (['y','x'], taux_dat.nav_lat.values),
    'nav_lon': (['y','x'], taux_dat.nav_lon.values),
    }
    # define global attributes
    attrs = {'made in':'/gpfs/home/mep22dku/scratch/SOZONE/MO_pipeline/EXTRACT/wspdfromtauxtauy.py',
    'desc': 'remaking ukesm forcing with good dates so that we can analyze with xarray'
    }

    ds = xr.Dataset(data_vars=data_vars,
    coords=coords,
    attrs=attrs)
    ds.to_netcdf(fnam_tosave)
    


def runner(yrstart, yrend):

    for yr in range(yrstart,yrend):
        print('miluju a maluju')
        make_wspd(yr)

    return 



yrstart = 1950; yrend = 2020
runner(yrstart, yrend)

# tnam = 'scen_1H'; tdir = dir_1H; yrstart = 1940; yrend = 2015
# runner(tnam, tdir, yrstart, yrend)

# tnam = 'scen_2H'; tdir = dir_2H; yrstart = 1950; yrend = 2015
# runner(tnam, tdir, yrstart, yrend)

# tnam = 'scen_3H'; tdir = dir_1H; yrstart = 1940; yrend = 1990
# runner(tnam, tdir, yrstart, yrend)

# tnam = 'scen_3H'; tdir = dir_3H; yrstart = 1990; yrend = 2015
# runner(tnam, tdir, yrstart, yrend)

# tnam = 'scen_1FA'; tdir = dir_1FA; yrstart = 2015; yrend = 2101
# runner(tnam, tdir, yrstart, yrend)

# tnam = 'scen_2FA'; tdir = dir_2FA; yrstart = 2015; yrend = 2101
# runner(tnam, tdir, yrstart, yrend)

# tnam = 'scen_3FA'; tdir = dir_3FA; yrstart = 2015; yrend = 2101
# runner(tnam, tdir, yrstart, yrend)

# tnam = 'scen_1FB'; tdir = dir_1FB; yrstart = 2015; yrend = 2101
# runner(tnam, tdir, yrstart, yrend)

# tnam = 'scen_2FB'; tdir = dir_2FB; yrstart = 2015; yrend = 2101
# runner(tnam, tdir, yrstart, yrend)

# tnam = 'scen_3FB'; tdir = dir_3FB; yrstart = 2015; yrend = 2101
# runner(tnam, tdir, yrstart, yrend)




# tnam = 'scen_1H'; tdir = dir_1H; yrstart = 1940; yrend = 2015
# runner(tnam, tdir, yrstart, yrend)

# tnam = 'scen_2H'; tdir = dir_2H; yrstart = 1950; yrend = 2015
# runner(tnam, tdir, yrstart, yrend)

# tnam = 'scen_3H'; tdir = dir_1H; yrstart = 1940; yrend = 1990
# runner(tnam, tdir, yrstart, yrend)

# tnam = 'scen_3H'; tdir = dir_3H; yrstart = 1990; yrend = 2015
# runner(tnam, tdir, yrstart, yrend)

# tnam = 'scen_1FA'; tdir = dir_1FA; yrstart = 2015; yrend = 2101
# runner(tnam, tdir, yrstart, yrend)

# tnam = 'scen_2FA'; tdir = dir_2FA; yrstart = 2015; yrend = 2101
# runner(tnam, tdir, yrstart, yrend)

# tnam = 'scen_3FA'; tdir = dir_3FA; yrstart = 2015; yrend = 2101
# runner(tnam, tdir, yrstart, yrend)

# tnam = 'scen_1FB'; tdir = dir_1FB; yrstart = 2015; yrend = 2101
# runner(tnam, tdir, yrstart, yrend)

# tnam = 'scen_2FB'; tdir = dir_2FB; yrstart = 2015; yrend = 2101
# runner(tnam, tdir, yrstart, yrend)

# tnam = 'scen_3FB'; tdir = dir_3FB; yrstart = 2015; yrend = 2101
# runner(tnam, tdir, yrstart, yrend)
