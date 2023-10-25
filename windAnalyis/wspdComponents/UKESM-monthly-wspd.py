import xarray as xr
import numpy as np
import pandas as pd


tdir = '/gpfs/data/greenocean/software/products/windsFromComponents/symlinked_hrly_UKESM/daily/'

mons = ['01','02','03','04','05','06','07','08','09','10','11','12']
scens = ['1A','1B','2A','2B','3A','3B']


for s in scens:
    print(s)
    if s == 'PI':
        yst = 1950
    else:
        yst = 1940
    for y in range(yst,2101):

        Jan = xr.open_dataset(f'{tdir}UKESM_{s}_y{y}m01_wspd10m_daily_rg.nc')
        Feb = xr.open_dataset(f'{tdir}UKESM_{s}_y{y}m02_wspd10m_daily_rg.nc')
        Mar = xr.open_dataset(f'{tdir}UKESM_{s}_y{y}m03_wspd10m_daily_rg.nc')
        Apr = xr.open_dataset(f'{tdir}UKESM_{s}_y{y}m04_wspd10m_daily_rg.nc')  
        May = xr.open_dataset(f'{tdir}UKESM_{s}_y{y}m05_wspd10m_daily_rg.nc')
        Jun = xr.open_dataset(f'{tdir}UKESM_{s}_y{y}m06_wspd10m_daily_rg.nc')
        Jul = xr.open_dataset(f'{tdir}UKESM_{s}_y{y}m07_wspd10m_daily_rg.nc')
        Aug = xr.open_dataset(f'{tdir}UKESM_{s}_y{y}m08_wspd10m_daily_rg.nc')
        Sep = xr.open_dataset(f'{tdir}UKESM_{s}_y{y}m09_wspd10m_daily_rg.nc')
        Oct = xr.open_dataset(f'{tdir}UKESM_{s}_y{y}m10_wspd10m_daily_rg.nc')  
        Nov = xr.open_dataset(f'{tdir}UKESM_{s}_y{y}m11_wspd10m_daily_rg.nc')
        Dec = xr.open_dataset(f'{tdir}UKESM_{s}_y{y}m12_wspd10m_daily_rg.nc')

        
        seasns = np.zeros([12,180,360])
        seasns[0,:,:] = np.nanmean(Jan.wspd10m.values, axis = 0)
        seasns[1,:,:] = np.nanmean(Feb.wspd10m.values, axis = 0)
        seasns[2,:,:] = np.nanmean(Mar.wspd10m.values, axis = 0)
        seasns[3,:,:] = np.nanmean(Apr.wspd10m.values, axis = 0)
        seasns[4,:,:] = np.nanmean(May.wspd10m.values, axis = 0)
        seasns[5,:,:] = np.nanmean(Jun.wspd10m.values, axis = 0)
        seasns[6,:,:] = np.nanmean(Jul.wspd10m.values, axis = 0)
        seasns[7,:,:] = np.nanmean(Aug.wspd10m.values, axis = 0)
        seasns[8,:,:] = np.nanmean(Sep.wspd10m.values, axis = 0)
        seasns[9,:,:] = np.nanmean(Oct.wspd10m.values, axis = 0)
        seasns[10,:,:] = np.nanmean(Nov.wspd10m.values, axis = 0)
        seasns[11,:,:] = np.nanmean(Dec.wspd10m.values, axis = 0)    


        times = pd.to_datetime([f"{y}-01-15", f"{y}-02-15",f"{y}-03-15",
                                f"{y}-04-15", f"{y}-05-15",f"{y}-06-15", 
                                f"{y}-07-15", f"{y}-08-15",f"{y}-09-15", 
                                f"{y}-10-15", f"{y}-11-15",f"{y}-12-15",])
        
        savenam = (f'{tdir}UKESM_{s}_y{y}_wspd10m_mon_rg.nc')
        data_vars = {'wspd10m':(['time_counter', 'lat', 'lon'], seasns,
        {'units': 'm/s',
        'long_name':'10m windspeed regridded'}),
        }
        # define coordinates
        coords = {'time_counter': (['time_counter'], times),
                
        'lon': (['lon'], Jan.lon.values),
        'lat': (['lat'], Jan.lat.values),
        }
        # define global attributes
        attrs = {'made in':'/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/UKESM-monthly-wspd.py',

        }
        ds = xr.Dataset(data_vars=data_vars,
        coords=coords,
        attrs=attrs)
        
        ds.to_netcdf(savenam)        
