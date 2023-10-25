#put python script here

import time
import xarray as xr
import numpy as np

for y in range(1990,2023):
    eradir = '/gpfs/data/greenocean/software/products/windsFromComponents/ERA5_v202303_rawdat/'
    tv = xr.open_dataset(f'{eradir}/10m_v_component_of_wind_ERA5_{y}.nc', chunks={"time": 24})
    tu = xr.open_dataset(f'{eradir}/10m_u_component_of_wind_ERA5_{y}.nc', chunks={"time": 24})

    q = time.time()
    twind = xr.ufuncs.sqrt(xr.ufuncs.square(tu.u10) + xr.ufuncs.square(tv.v10))
    twind.name = 'windspeed'

    w5 = twind.to_dataset()
    w5.to_netcdf(f'{eradir}/10m_windspeed_ERA5_{y}.nc')

    q1 = time.time()
    print(q1-q)

