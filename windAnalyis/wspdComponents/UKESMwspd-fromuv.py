import xarray as xr
import numpy as np

tdir = '/gpfs/data/greenocean/software/products/windsFromComponents/UKESM_monthly_atdayres/'

mons = ['01','02','03','04','05','06','07','08','09','10','11','12']
scens = ['1A','1B','2A','2B','3A','3B']

# for s in scens:
#     for y in range(1940,2101):
#         for m in range(0,12):
#             uwi = xr.open_dataset(f'{tdir}UKESM_{s}_y{y}m{mons[m]}_uwind10m_daily_rg.nc')
#             vwi = xr.open_dataset(f'{tdir}UKESM_{s}_y{y}m{mons[m]}_vwind10m_daily_rg.nc')
#             tnam = f'{tdir}UKESM_{s}_y{y}m{mons[m]}_wspd10m_daily_rg.nc'
#             print(tnam)
#             wspd = xr.ufuncs.sqrt(uwi.uwind10m**2 + vwi.vwind10m**2)
#             wspd.name = 'wspd10m'
#             wspd = wspd.to_dataset()
#             wspd.attrs = {'made in': '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/UKESMwspdfromuv.py'}
#             wspd.to_netcdf(tnam)

#             mons = ['01','02','03','04','05','06','07','08','09','10','11','12']
scens = ['PI']

# for s in scens:
#     for y in range(2062,2101):
#         for m in range(0,12):
#             uwi = xr.open_dataset(f'{tdir}UKESM_{s}_y{y}m{mons[m]}_uwind10m_daily_rg.nc')
#             vwi = xr.open_dataset(f'{tdir}UKESM_{s}_y{y}m{mons[m]}_vwind10m_daily_rg.nc')
#             tnam = f'{tdir}UKESM_{s}_y{y}m{mons[m]}_wspd10m_daily_rg.nc'
#             print(tnam)
#             wspd = xr.ufuncs.sqrt(uwi.uwind10m**2 + vwi.vwind10m**2)
#             wspd.name = 'wspd10m'
#             wspd = wspd.to_dataset()
#             wspd.attrs = {'made in': '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/UKESMwspdfromuv.py'}
#             wspd.to_netcdf(tnam)
