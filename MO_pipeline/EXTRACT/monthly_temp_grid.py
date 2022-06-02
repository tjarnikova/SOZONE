import scendict as sc
import netCDF4 as nc
import xarray as xr
import numpy as np
import warnings
warnings.filterwarnings('ignore')

rdir = '/gpfs/home/mep22dku/scratch/MET_forcing/'
starts = np.array([0, 31,  59,  90, 120, 151, 181, 212, 243, 273, 304, 334])
ends = np.array([31,  59,  90, 120, 151, 181, 212, 243, 273, 304, 334, 365])
var = 'air'; varpat = 'tair10m'

scens = ['1A','1B','2A','2B','3A','3B']

for s in range(0,6):
    scen = scens[s]
    t_stor = np.random.rand(161,14,149,182)
    ncnam = f'./ncs/scen_{scen}_monthly_airtemp.nc'
    print(ncnam)
    for yr in range(1940,2101):
        if yr%10 == 0:
            print(yr)
        try:
            tw = nc.Dataset(f'{rdir}scen_{scen}/MetOffice_{varpat}{yr}.nc') 
            t_nc = tw[var][:]

            for i in range(0,12):
                t_mon = t_nc[starts[i]:ends[i],:,:]
                t_avg = np.nanmean(t_mon, axis = 0)
                t_stor[yr-1940,i,:,:] = t_avg

            summer = np.concatenate((t_nc[0:59,:,:],t_nc[334:365,:,:]),axis = 0)
            t_stor[yr-1940,12,:,:] = np.nanmean(summer,axis =0)
            winter = (t_nc[151:243,:,:])
            t_stor[yr-1940,13,:,:] = np.nanmean(winter,axis = 0)
        except:
            t_stor[yr-1940,:,:,:] = np.nan

    ds = xr.Dataset(
     {"mean_tair": (("yr", "mon", "y", "x" ), t_stor)},
        coords={
            "yr": np.arange(1940,2101,1),
            "mon": np.arange(1,15,1),
            "x": np.arange(0,182,1),
            "y": np.arange(0,149,1),
        },
        attrs={
            "desc": "mean monthly maps of temp, made from ~/scratch/MET_forcing/",
            "desc2": "summer is month 13, winter is month 14"
      },
       )
        
    ds.to_netcdf(ncnam)