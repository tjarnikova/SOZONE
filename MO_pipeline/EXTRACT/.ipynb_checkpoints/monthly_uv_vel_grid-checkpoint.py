import netCDF4 as nc
import xarray as xr
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import sys
sys.path.append('..')
import scendict as sc

rdir = '/gpfs/home/mep22dku/scratch/MET_forcing/'
starts = np.array([0, 31,  59,  90, 120, 151, 181, 212, 243, 273, 304, 334])
ends = np.array([31,  59,  90, 120, 151, 181, 212, 243, 273, 304, 334, 365])

scens = ['1A','1B','2A','2B','3A','3B']

for s in range(0,6):
    scen = scens[s]
    t_stor_u = np.random.rand(161,15,149,182)
    t_stor_v = np.random.rand(161,15,149,182)
    ncnam = f'./ncs/scen_{scen}_monthly_u_v_vel.nc'
    print(ncnam)
    for yr in range(1940,2101):
        if yr%10 == 0:
            print(yr)
        try:
            tw = nc.Dataset(f'{rdir}scen_{scen}/MetOffice_tauy_y{yr}.nc') 
            t_nc_v = tw['vflx'][:]
            tw = nc.Dataset(f'{rdir}scen_{scen}/MetOffice_taux_y{yr}.nc') 
            t_nc_u = tw['uflx'][:]
            #t_nc = np.sqrt(t_nc1**2+t_nc2**2)

            for i in range(0,12):
                t_mon = t_nc_u[starts[i]:ends[i],:,:]
                t_avg = np.nanmean(t_mon, axis = 0)
                t_stor_u[yr-1940,i,:,:] = t_avg

            summer = np.concatenate((t_nc_u[0:59,:,:],t_nc_u[334:365,:,:]),axis = 0)
            t_stor_u[yr-1940,12,:,:] = np.nanmean(summer,axis =0)
            winter = (t_nc_u[151:243,:,:])
            t_stor_u[yr-1940,13,:,:] = np.nanmean(winter,axis = 0)
            t_stor_u[yr-1940,14,:,:] = np.nanmean(t_nc_u,axis = 0)
            
            for i in range(0,12):
                t_mon = t_nc_v[starts[i]:ends[i],:,:]
                t_avg = np.nanmean(t_mon, axis = 0)
                t_stor_v[yr-1940,i,:,:] = t_avg

            summer = np.concatenate((t_nc_v[0:59,:,:],t_nc_v[334:365,:,:]),axis = 0)
            t_stor_v[yr-1940,12,:,:] = np.nanmean(summer,axis =0)
            winter = (t_nc_v[151:243,:,:])
            t_stor_v[yr-1940,13,:,:] = np.nanmean(winter,axis = 0)
            t_stor_v[yr-1940,14,:,:] = np.nanmean(t_nc_v,axis = 0)
            
        except:
            t_stor_u[yr-1940,:,:,:] = np.nan
            t_stor_v[yr-1940,:,:,:] = np.nan


    ds = xr.Dataset(
        {
            "mean_uvel": (("yr", "mon", "y", "x" ), t_stor_u),
            "mean_vvel": (("yr", "mon", "y", "x" ), t_stor_v)
        },
        coords={
            "yr": np.arange(1940,2101,1),
            "mon": np.arange(1,16,1),
            "x": np.arange(0,182,1),
            "y": np.arange(0,149,1),
        },
        attrs={
            "desc": "mean monthly maps of u and v vel, made from ~/scratch/MET_forcing/",
            "desc2": "summer is month 13, winter is month 14, full year is month 15 (index 14)"
      }
       )
    
#     In [35]: ds = xr.Dataset(
#    ....:     {
#    ....:         "temperature": (["x", "y", "time"], temp),
#    ....:         "precipitation": (["x", "y", "time"], precip),
#    ....:     },
#    ....:     coords={
#    ....:         "lon": (["x", "y"], lon),
#    ....:         "lat": (["x", "y"], lat),
#    ....:         "time": pd.date_range("2014-09-06", periods=3),
#    ....:         "reference_time": pd.Timestamp("2014-09-05"),
#    ....:     },
#    ....: )
        
    ds.to_netcdf(ncnam)