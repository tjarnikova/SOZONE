import xarray as xr
import numpy as np

tdir = '/gpfs/data/greenocean/software/products/windsFromComponents/symlinked_hrly_UKESM/'

mons = ['01','02','03','04','05','06','07','08','09','10','11','12']
scens = ['1A','1B','2A','2B','3A','3B']
scens = ['2B']

for s in scens:
    for y in range(2037,2101):
        print(y)
        for i in range(0,12):
            uwi = xr.open_dataset(f'{tdir}scen{s}_wind_y{y}m{mons[i]}_rg.nc')
            #vwi = xr.open_dataset(f'{tdir}UKESM_{s}_y{y}m{mons[m]}_vwind10m_daily_rg.nc')
            tnam = f'{tdir}/daily/UKESM_{s}_y{y}m{mons[i]}_wspd10m_daily_rg.nc'
#             print(tnam)
            wspd = xr.ufuncs.sqrt(uwi.uwind10m**2 + uwi.vwind10m**2)
            wspd.name = 'wspd10m'
            w4 = wspd.groupby('time_counter.day').mean()
            w5 = w4.to_dataset()
            w5['day'] = np.arange(i*30+1,(i+1)*30+1,1)
            w5.attrs = {'made in': '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/UKESMwspd-from-regrid-highres.py'}
            w5.to_netcdf(tnam)

# scens = ['PI']
# for s in scens:
#     for y in range(2011,2101):
#         print(f'{s}, {y}')
#         for i in range(0,12):
#             uwi = xr.open_dataset(f'{tdir}scen{s}_wind_y{y}m{mons[i]}_rg.nc')
#             #vwi = xr.open_dataset(f'{tdir}UKESM_{s}_y{y}m{mons[m]}_vwind10m_daily_rg.nc')
#             tnam = f'{tdir}/daily/UKESM_{s}_y{y}m{mons[i]}_wspd10m_daily_rg.nc'
#             print(tnam)
#             wspd = xr.ufuncs.sqrt(uwi.uwind10m**2 + uwi.vwind10m**2)
#             wspd.name = 'wspd10m'
#             w4 = wspd.groupby('time_counter.day').mean()
#             w5 = w4.to_dataset()
#             w5['day'] = np.arange(i*30+1,(i+1)*30+1,1)
#             w5.attrs = {'made in': '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/UKESMwspd-from-regrid-highres.py'}
#             w5.to_netcdf(tnam)





