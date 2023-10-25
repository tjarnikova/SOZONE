import xarray as xr
import numpy as np
import pandas as pd


tdir = '/gpfs/data/greenocean/software/products/windsFromComponents/symlinked_hrly_UKESM/daily/'

mons = ['01','02','03','04','05','06','07','08','09','10','11','12']
scens = ['1A','1B','2A','2B','3A','3B']
scens = ['2B']

for s in scens:
    print(s)
    if s == 'PI':
        yst = 1950
    else:
        yst = 1940
    for y in range(yst,2101):
        print(y)

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
        
        DJF = np.zeros([90,180,360])
        DJF[0:30,:,:] = Dec.wspd10m.values
        DJF[30:60,:,:] = Jan.wspd10m.values
        DJF[60:90,:,:] = Feb.wspd10m.values
        
        MAM = np.zeros([90,180,360])
        MAM[0:30,:,:] = Mar.wspd10m.values
        MAM[30:60,:,:] = Apr.wspd10m.values
        MAM[60:90,:,:] = May.wspd10m.values
        
        JJA = np.zeros([90,180,360])
        JJA[0:30,:,:] = Jun.wspd10m.values
        JJA[30:60,:,:] = Jul.wspd10m.values
        JJA[60:90,:,:] = Aug.wspd10m.values
        
        SON = np.zeros([90,180,360])
        SON[0:30,:,:] = Sep.wspd10m.values
        SON[30:60,:,:] = Oct.wspd10m.values
        SON[60:90,:,:] = Nov.wspd10m.values
        
        seasns = np.zeros([4,180,360])
        seasns[0,:,:] = np.nanmean(DJF, axis = 0)
        seasns[1,:,:] = np.nanmean(MAM, axis = 0)
        seasns[2,:,:] = np.nanmean(JJA, axis = 0)
        seasns[3,:,:] = np.nanmean(SON, axis = 0)
        
        times = pd.to_datetime([f"{y}-01-15", f"{y}-04-15", f"{y}-07-15", f"{y}-10-15"])
        
        savenam = (f'{tdir}UKESM_{s}_y{y}_wspd10m_seas_rg.nc')
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
        attrs = {'made in':'/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/UKESM-seas-wspd.py',

        }
        ds = xr.Dataset(data_vars=data_vars,
        coords=coords,
        attrs=attrs)
        
        ds.to_netcdf(savenam)        
