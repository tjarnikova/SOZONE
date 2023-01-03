import netCDF4 as nc
import xarray as xr
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import sys
sys.path.append('..')
import scendict as sc

rdir = '//gpfs/data/greenocean/software/resources/MetProcessed/MET_forcing/'
starts = np.array([0, 31,  59,  90, 120, 151, 181, 212, 243, 273, 304, 334])
ends = np.array([31,  59,  90, 120, 151, 181, 212, 243, 273, 304, 334, 365])

scens = ['1A','1B','2A','2B','3A','3B']

runhorse = False
if runhorse:
    
    for s in range(0,6):
        scen = scens[s]
        t_stor = np.random.rand(161,15,149,182)
        ncnam = f'./ncs/scen_{scen}_monthly_wspd.nc'
        print(ncnam)
        for yr in range(1940,2101):
            if yr%10 == 0:
                print(yr)
            try:
                tw = nc.Dataset(f'{rdir}scen_{scen}/MetOffice_tauy_y{yr}.nc') 
                t_nc1 = tw['vflx'][:]
                tw = nc.Dataset(f'{rdir}scen_{scen}/MetOffice_taux_y{yr}.nc') 
                t_nc2 = tw['uflx'][:]
                t_nc = np.sqrt(t_nc1**2+t_nc2**2)

                for i in range(0,12):
                    t_mon = t_nc[starts[i]:ends[i],:,:]
                    t_avg = np.nanmean(t_mon, axis = 0)
                    t_stor[yr-1940,i,:,:] = t_avg

                summer = np.concatenate((t_nc[0:59,:,:],t_nc[334:365,:,:]),axis = 0)
                t_stor[yr-1940,12,:,:] = np.nanmean(summer,axis =0)
                winter = (t_nc[151:243,:,:])
                t_stor[yr-1940,13,:,:] = np.nanmean(winter,axis = 0)
                t_stor[yr-1940,14,:,:] = np.nanmean(t_nc,axis = 0)
            except:
                print(f'cannot find {scen} {yr}')
                t_stor[yr-1940,:,:,:] = np.nan

        ds = xr.Dataset(
         {"mean_wspd": (("yr", "mon", "y", "x" ), t_stor)},
            coords={
                "yr": np.arange(1940,2101,1),
                "mon": np.arange(1,16,1),
                "x": np.arange(0,182,1),
                "y": np.arange(0,149,1),
            },
            attrs={
                "desc": "mean monthly maps of wspd, made from ~/scratch/MET_forcing/",
                "desc2": "summer is month 13, winter is month 14, full year is month 15 (index 14)"
          },
           )

        ds.to_netcdf(ncnam)

runhorse = True
if runhorse:
    

    ncnam = f'./ncs/scen_PI_monthly_wspd.nc'
    print(ncnam)
    for yr in range(2220,2300):
        rdir = '/gpfs/home/mep22dku/scratch/u-aw310_pictrl'
        t_stor = np.random.rand(80,15,149,182)
        if yr%10 == 0:
            print(yr)
        try:
            tw = nc.Dataset(f'{rdir}/tauy_1d_{yr}_daily.nc') 
            t_nc1 = tw['vflx'][:]
            tw = nc.Dataset(f'{rdir}/taux_1d_{yr}_daily.nc') 
            t_nc2 = tw['uflx'][:]
            t_nc = np.sqrt(t_nc1**2+t_nc2**2)

            for i in range(0,12):
                t_mon = t_nc[starts[i]:ends[i],:,:]
                t_avg = np.nanmean(t_mon, axis = 0)
                t_stor[yr-2220,i,:,:] = t_avg

            summer = np.concatenate((t_nc[0:59,:,:],t_nc[334:365,:,:]),axis = 0)
            t_stor[yr-2220,12,:,:] = np.nanmean(summer,axis =0)
            winter = (t_nc[151:243,:,:])
            t_stor[yr-2220,13,:,:] = np.nanmean(winter,axis = 0)
            t_stor[yr-2220,14,:,:] = np.nanmean(t_nc,axis = 0)
        except:
            print(f'cannot find {yr}')
            t_stor[yr-1940,:,:,:] = np.nan

    ds = xr.Dataset(
     {"mean_wspd": (("yr", "mon", "y", "x" ), t_stor)},
        coords={
            "yr": np.arange(2220,2300,1),
            "mon": np.arange(1,16,1),
            "x": np.arange(0,182,1),
            "y": np.arange(0,149,1),
        },
        attrs={
            "desc": "mean monthly maps of wspd, made from ~/scratch/MET_forcing/",
            "desc2": "summer is month 13, winter is month 14, full year is month 15 (index 14)"
      },
       )

    ds.to_netcdf(ncnam)