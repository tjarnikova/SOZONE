import time
import xarray as xr
import numpy as np

# for y in range(1940,2023):
#     print(y)
#     eradir = '/gpfs/data/greenocean/software/products/windsFromComponents/ERA5_v202303_rawdat/'
#     tv = xr.open_dataset(f'{eradir}/10m_v_component_of_wind_ERA5_{y}.nc', chunks={"time": 24})
#     tu = xr.open_dataset(f'{eradir}/10m_u_component_of_wind_ERA5_{y}.nc', chunks={"time": 24})

#     q = time.time()
#     tuD = tu.u10.resample(time='1D').mean('time')
#     tuD = tuD.to_dataset()
#     tuD.attrs = {'made in': '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/ERAdailywinds.py'}
#     tuD.to_netcdf(f'{eradir}/10m_u_component_of_wind_ERA5_{y}-daily.nc')
#     tvD = tv.v10.resample(time='1D').mean('time')
#     tvD = tvD.to_dataset()
#     tvD.attrs = {'made in': '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/ERAdailywinds.py'}
#     tvD.to_netcdf(f'{eradir}/10m_v_component_of_wind_ERA5_{y}-daily.nc')
#     q1 = time.time()
#     print(q1-q)

for y in range(1990,2023):
    print(y)
    eradir = '/gpfs/data/greenocean/software/products/windsFromComponents/ERA5_v202303_rawdat/'
    tu = xr.open_dataset(f'{eradir}/10m_windspeed_ERA5_{y}.nc', chunks={"time": 24})

    q = time.time()
    tuD = tu.windspeed.resample(time='1D').mean('time')
    tuD = tuD.to_dataset()
    tuD.attrs = {'made in': '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/ERAdailywinds.py'}
    tuD.to_netcdf(f'{eradir}/daily/10m_windspeed_ERA5_{y}-daily.nc')

    q1 = time.time()
    print(q1-q)

    
