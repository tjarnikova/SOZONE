import pandas as pd
import xarray as xr
import glob
from datetime import datetime

# import netCDF4 as nc
# import matplotlib.pyplot as plt
# import sys
# sys.path.append('/gpfs/home/mep22dku/scratch/SOZONE')
# #list of models
# sys.path.append('/gpfs/home/mep22dku/scratch/SOZONE/UTILS')
# import lom
# import utils as ut
# %matplotlib inline
# import warnings
# warnings.filterwarnings('ignore')
# import cartopy.feature as cfeature
# from importlib import reload
# import matplotlib.path as mpath

print('catch a boat to England maybe to Spain')

def make_taux_newERA(yr, save = True):

    dtype = 'taux'
    #where to save remade file
    sdir = '/gpfs/data/greenocean/software/resources/winds_gooddates/'
    tnam = f'ERA5_v202303_{dtype}_{yr}_daily.nc'
    print(tnam)
    savenam = f'{sdir}{tnam}'
    
    ## 
    baseDir = f'/gpfs/home/mep22dku/scratch/test_eraforcing/'
    ty = f'{baseDir}/{dtype}*{yr}*daily.nc'
    
    
    t2 = glob.glob(ty)
    v = xr.open_dataset(t2[0] ,decode_times=False)
    times = pd.date_range(f"{yr}/01/01",f"{yr+1}/01/01",freq='D',closed='left')
    #times = times[~((times.month == 2) & (times.day == 29))] #exclude leap yrs; nvm don't have to

    data_vars = {'uflx':(['time_counter', 'y', 'x'], v.uflx.values,
    {'units': 'm/s',
    'long_name':'Surface ocean pCO2'}),
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
    
    print('the blues still run the game')
    
    ds = xr.Dataset(data_vars=data_vars,
    coords=coords,
    attrs=attrs)

    if save:
        ds.to_netcdf(savenam)
        
def make_taux_oldERA(yr, save = True):

    dtype = 'taux'
    #where to save remade file
    sdir = '/gpfs/data/greenocean/software/resources/winds_gooddates/'
    tnam = f'ERA5_v2022_{dtype}_{yr}_daily.nc'
    print(tnam)
    savenam = f'{sdir}{tnam}'
    
    ## 
    baseDir = f'/gpfs/data/greenocean/software/products/ERA5Forcing/daily/'
    ty = f'{baseDir}/{dtype}*{yr}*daily.nc'
    
    
    t2 = glob.glob(ty)
    v = xr.open_dataset(t2[0] ,decode_times=False)
    times = pd.date_range(f"{yr}/01/01",f"{yr+1}/01/01",freq='D',closed='left')
    #times = times[~((times.month == 2) & (times.day == 29))] #exclude leap yrs; nvm don't have to

    data_vars = {'uflx':(['time_counter', 'y', 'x'], v.uflx.values,
    {'units': 'm/s',
    'long_name':'Surface ocean pCO2'}),
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
    
    print('the blues still run the game')
    
    ds = xr.Dataset(data_vars=data_vars,
    coords=coords,
    attrs=attrs)

    if save:
        ds.to_netcdf(savenam)
        

# done on march 13, 2023
# for y in range(1959,1980):
#     make_taux_newERA(y)

#done 2023-03-17
# for y in range(1980,2022):
#     make_taux_oldERA(y)

def make_tauy_newERA(yr, save = True):

    dtype = 'tauy'
    #where to save remade file
    sdir = '/gpfs/data/greenocean/software/resources/winds_gooddates/'
    tnam = f'ERA5_v202303_{dtype}_{yr}_daily.nc'
    print(tnam)
    savenam = f'{sdir}{tnam}'
    
    ## 
    baseDir = f'/gpfs/home/mep22dku/scratch/test_eraforcing/'
    ty = f'{baseDir}/{dtype}*{yr}*daily.nc'
    
    
    t2 = glob.glob(ty)
    v = xr.open_dataset(t2[0] ,decode_times=False)
    times = pd.date_range(f"{yr}/01/01",f"{yr+1}/01/01",freq='D',closed='left')
    #times = times[~((times.month == 2) & (times.day == 29))] #exclude leap yrs; nvm don't have to

    data_vars = {'vflx':(['time_counter', 'y', 'x'], v.vflx.values,
    {'units': 'm/s',
    'long_name':'Surface ocean pCO2'}),
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
    
    print('the blues still run the game')
    
    ds = xr.Dataset(data_vars=data_vars,
    coords=coords,
    attrs=attrs)

    if save:
        ds.to_netcdf(savenam)
        
def make_tauy_oldERA(yr, save = True):

    dtype = 'tauy'
    #where to save remade file
    sdir = '/gpfs/data/greenocean/software/resources/winds_gooddates/'
    tnam = f'ERA5_v2022_{dtype}_{yr}_daily.nc'
    print(tnam)
    savenam = f'{sdir}{tnam}'
    
    ## 
    baseDir = f'/gpfs/data/greenocean/software/products/ERA5Forcing/daily/'
    ty = f'{baseDir}/{dtype}*{yr}*daily.nc'
    
    
    t2 = glob.glob(ty)
    v = xr.open_dataset(t2[0] ,decode_times=False)
    times = pd.date_range(f"{yr}/01/01",f"{yr+1}/01/01",freq='D',closed='left')
    #times = times[~((times.month == 2) & (times.day == 29))] #exclude leap yrs; nvm don't have to

    data_vars = {'vflx':(['time_counter', 'y', 'x'], v.vflx.values,
    {'units': 'm/s',
    'long_name':'Surface ocean pCO2'}),
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
    
    print('the blues still run the game')
    
    ds = xr.Dataset(data_vars=data_vars,
    coords=coords,
    attrs=attrs)

    if save:
        ds.to_netcdf(savenam)
        
        
#done on march 17, 2023
# for y in range(1959,1980):
#     make_tauy_newERA(y)
#     make_tauy_oldERA(y)

#done 2023-03-21
for y in range(1950,2022):
    make_tauy_oldERA(y)
    make_taux_oldERA(y)