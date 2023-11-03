import glob
import xarray as xr
import pandas as pd
import numpy as np


extract = True




def make_yearfiles_tom(yrst, yren, tscen, sig = False):
    #print(f'SCENARIO {tscen}')
    dslist = []
    
    for y in range(yrst,yren):
    
        tdir = '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/oceanFields/fullTOM_OT/'
        td = glob.glob(f'{tdir}/TOM12_TJ_{tscen}A6_{y}_mocsig.nc')
        dslist.append(td[0])

    return dslist


def make_mocsig_nc(yr,tscen):

    tdir = '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/oceanFields/max_OT/'
    savenam_seas = f'{tdir}/seas_OT_{yr}_{tscen}-TOMA6.nc'
    print(savenam_seas)

    mocf = (make_yearfiles_tom(yr, yr+1, tscen, sig = True))
    t = xr.open_dataset(mocf[0])
    times = pd.date_range(f"{yr}/01/01",f"{yr+1}/01/01",freq='MS',closed='left')
    times2 = [times[0], times[3], times[6], times[9]] 
    times3 = pd.to_datetime(times2)

    DJF_mn = t.isel(latV=slice(0,50)).sel(time_counter=(t['time_counter.season'] == 'DJF')).\
    groupby('time_counter.year').mean()
    MAM_mn = t.isel(latV=slice(0,50)).sel(time_counter=(t['time_counter.season'] == 'MAM')).\
    groupby('time_counter.year').mean()
    JJA_mn = t.isel(latV=slice(0,50)).sel(time_counter=(t['time_counter.season'] == 'JJA')).\
    groupby('time_counter.year').mean()
    SON_mn = t.isel(latV=slice(0,50)).sel(time_counter=(t['time_counter.season'] == 'SON')).\
    groupby('time_counter.year').mean()
    yr_mn = t.isel(latV=slice(0,50)).\
    groupby('time_counter.year').mean()

    max_OT = np.zeros(4)
    lat_OT = np.zeros(4)
    sigma2000_OT = np.zeros(4)

    ars = [DJF_mn, MAM_mn, JJA_mn, SON_mn]

    for m in range(0,4):

        t = ars[m]
        t2 = t.dmoc2000.isel(latV=slice(0,50))
        w = t2.where(t2==t2.max(), drop=True).squeeze()

        max_OT[m] = w.values
        lat_OT[m] = w.latV
        sigma2000_OT[m] = w.sigma2000


    t = yr_mn
    t2 = t.dmoc2000.isel(latV=slice(0,50))
    w = t2.where(t2==t2.max(), drop=True).squeeze()

    ### this is a stupid way to do it but i can't get it to be of dimension 1 so
    max_OT_yr = np.zeros(4)
    lat_OT_yr = np.zeros(4)
    sigma2000_OT_yr = np.zeros(4)

    max_OT_yr[:] = w.values
    lat_OT_yr[:] = w.latV
    sigma2000_OT_yr[:] = w.sigma2000



    savenam = savenam_seas
    data_vars = {
        'max_OT':(['time_counter'], max_OT, {'units': 'Sv',}),
        'lat_OT':(['time_counter'], lat_OT, {'units': 'deg',}),
        'sigma2000_OT':(['time_counter'], sigma2000_OT, {'units': 'sigma2000',}),
        'max_OT_yr':(['time_counter'], max_OT_yr, {'units': 'Sv',}),
        'lat_OT_yr':(['time_counter'], lat_OT_yr, {'units': 'deg',}),
        'sigma2000_OT_yr':(['time_counter'], sigma2000_OT_yr, {'units': 'sigma2000',}),
    }
    # define coordinates
    coords = {'time_counter': (['time_counter'], times3),
            }
    # define global attributes
    attrs = {'made in':'SOZONE/windAnalyis/oceanFields/extract_OT_tom.py',
    'desc': 'where and when does maximum overturning occur'
    }
    ds_seas = xr.Dataset(data_vars=data_vars,
    coords=coords,
    attrs=attrs)
    ds_seas.to_netcdf(savenam)

    return ds_seas


if extract:

    scen = ['1A','1B','2A','2B','3A','3B']
    for s in range(0,6):
        tscen = scen[s]
        for yr in range(1950,2100):

            ds_seas = make_mocsig_nc(yr,tscen)


