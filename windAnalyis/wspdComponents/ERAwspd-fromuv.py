import xarray as xr
import numpy as np

tdir = '/gpfs/data/greenocean/software/products/windsFromComponents/ERA5_v202303_rawdat/'

mons = ['01','02','03','04','05','06','07','08','09','10','11','12']
scens = ['1A','1B','2A','2B','3A','3B']

for s in scens:
    for y in range(1940,2023):

        uwi = xr.open_dataset(f'{tdir}10m_u_component_of_wind_ERA5_{y}-daily_rg.nc')
        vwi = xr.open_dataset(f'{tdir}10m_v_component_of_wind_ERA5_{y}-daily_rg.nc')
        tnam = f'{tdir}10m_windspeed_ERA5_{y}-daily_rg.nc'
        print(tnam)
        wspd = xr.ufuncs.sqrt(uwi.u10**2 + vwi.v10**2)
        wspd.name = 'wspd10m'
        wspd = wspd.to_dataset()
        wspd.attrs = {'made in': '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/ERAwspd-fromuv.py'}
        wspd.to_netcdf(tnam)
