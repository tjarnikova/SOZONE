import xarray as xr
import numpy as np
import pandas as pd



for y in range(1940,2023):
    
    tdir = '/gpfs/data/greenocean/software/products/windsFromComponents/ERA5_v202303_rawdat/daily/'
    tfil = f'10m_windspeed_ERA5_{y}-daily-rg.nc'
    w = xr.open_dataset(f'{tdir}{tfil}')
    tvar = w.windspeed.groupby('time.month').mean()

    times = pd.to_datetime([f"{y}-01-15", f"{y}-02-15",f"{y}-03-15",
                            f"{y}-04-15", f"{y}-05-15",f"{y}-06-15", 
                            f"{y}-07-15", f"{y}-08-15",f"{y}-09-15", 
                            f"{y}-10-15", f"{y}-11-15",f"{y}-12-15",])

    savenam = (f'{tdir}ERA5_y{y}_wspd10m_mon_rg.nc')
    data_vars = {'wspd10m':(['time_counter', 'lat', 'lon'], tvar.values,
    {'units': 'm/s',
    'long_name':'10m windspeed regridded'}),
    }
    # define coordinates
    coords = {'time_counter': (['time_counter'], times),

    'lon': (['lon'], w.lon.values),
    'lat': (['lat'], w.lat.values),
             }
    
    attrs = {'made in':'/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/ERA5-seas-wspd.py',

    }
    ds = xr.Dataset(data_vars=data_vars,
    coords=coords,
    attrs=attrs)
    
    ds.to_netcdf(savenam)  
