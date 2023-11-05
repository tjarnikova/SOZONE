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

def make_better_dates(tnam, tdir, yr):

    #make better uflxs with nice dates (where to save):
    fnam = f'UKESM_{tnam}_taux_{yr}_daily.nc'
    sdir = '/gpfs/data/greenocean/software/resources/winds_gooddates/'
    fnam_tosave = f'{sdir}{fnam}'
    print(fnam)

    rdir = f'/gpfs/data/greenocean/software/resources/MetProcessed/MET_soft/{tdir}'
    t2 = glob.glob(f'{rdir}/taux_1d_{yr}_daily.nc')
    print(t2)
    v = xr.open_dataset(t2[0] ,decode_times=False)
    times = pd.date_range(f"{yr}/01/01",f"{yr+1}/01/01",freq='D',closed='left')
    times = times[~((times.month == 2) & (times.day == 29))] #exclude leap yrs; nvm don't have to

    data_vars = {'uflx':(['time_counter', 'y', 'x'], v.uflx.values,
    {'units': 'm/s',
    'long_name':'uflx'}),
    }
    # define coordinates
    coords = {'time_counter': (['time_counter'], times),
    'nav_lat': (['y','x'], v.nav_lat.values),
    'nav_lon': (['y','x'], v.nav_lon.values),
    }
    # define global attributes
    attrs = {'made in':'SOZONE/windAnalyis/compare_1959_old.ipynb',
    'desc': 'remaking era5 forcing with good dates so that we can analyze with xarray'
    }

    ds = xr.Dataset(data_vars=data_vars,
    coords=coords,
    attrs=attrs)
    ds.to_netcdf(fnam_tosave)

   
    #make better vflxs with nice dates (where to save):
    fnam = f'UKESM_{tnam}_tauy_{yr}_daily.nc'
    sdir = '/gpfs/data/greenocean/software/resources/winds_gooddates/'
    fnam_tosave = f'{sdir}{fnam}'
    print(fnam)

    rdir = f'/gpfs/data/greenocean/software/resources/MetProcessed/MET_soft/{tdir}'
    t2 = glob.glob(f'{rdir}/tauy_1d_{yr}_daily.nc')
    print(t2)
    v = xr.open_dataset(t2[0] ,decode_times=False)
    times = pd.date_range(f"{yr}/01/01",f"{yr+1}/01/01",freq='D',closed='left')
    times = times[~((times.month == 2) & (times.day == 29))] #exclude leap yrs; nvm don't have to

    data_vars = {'vflx':(['time_counter', 'y', 'x'], v.vflx.values,
    {'units': 'm/s',
    'long_name':'vflx'}),
    }
    # define coordinates
    coords = {'time_counter': (['time_counter'], times),
    'nav_lat': (['y','x'], v.nav_lat.values),
    'nav_lon': (['y','x'], v.nav_lon.values),
    }
    # define global attributes
    attrs = {'made in':'MO_pipeline/EXTRACT/dateReformatUKESM.py',
    'desc': 'remaking ukesm forcing with good dates so that we can analyze with xarray'
    }

    ds = xr.Dataset(data_vars=data_vars,
    coords=coords,
    attrs=attrs)
    ds.to_netcdf(fnam_tosave)


    return 
    
def runner(tnam, tdir, yrstart, yrend, PI = False):

    for yr in range(yrstart,yrend):
        make_better_dates(tnam, tdir,yr, PI)

    return 





tnam = 'scen_1H'; tdir = dir_1H; yrstart = 1940; yrend = 2015
runner(tnam, tdir, yrstart, yrend)

tnam = 'scen_2H'; tdir = dir_2H; yrstart = 1950; yrend = 2015
runner(tnam, tdir, yrstart, yrend)

tnam = 'scen_3H'; tdir = dir_1H; yrstart = 1940; yrend = 1990
runner(tnam, tdir, yrstart, yrend)

tnam = 'scen_3H'; tdir = dir_3H; yrstart = 1990; yrend = 2015
runner(tnam, tdir, yrstart, yrend)

tnam = 'scen_1FA'; tdir = dir_1FA; yrstart = 2015; yrend = 2101
runner(tnam, tdir, yrstart, yrend)

tnam = 'scen_2FA'; tdir = dir_2FA; yrstart = 2015; yrend = 2101
runner(tnam, tdir, yrstart, yrend)

tnam = 'scen_3FA'; tdir = dir_3FA; yrstart = 2015; yrend = 2101
runner(tnam, tdir, yrstart, yrend)

tnam = 'scen_1FB'; tdir = dir_1FB; yrstart = 2015; yrend = 2101
runner(tnam, tdir, yrstart, yrend)

tnam = 'scen_2FB'; tdir = dir_2FB; yrstart = 2015; yrend = 2101
runner(tnam, tdir, yrstart, yrend)

tnam = 'scen_3FB'; tdir = dir_3FB; yrstart = 2015; yrend = 2101
runner(tnam, tdir, yrstart, yrend)
