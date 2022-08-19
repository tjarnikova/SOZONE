import glob
import xarray as xr
import sys
sys.path.append('/gpfs/home/mep22dku/scratch/SOZONE/MODPROC_ROBOT/MultiModelMonitor/WORK_SCRIPTS')
sys.path.append('/gpfs/home/mep22dku/scratch/SOZONE/MO_pipeline/')
import scendict as sc
import breakdown as bp
import warnings
import numpy as np


def get_seas_co2(tr,tmin,tmax):
    print(tr)
    

    tmesh = xr.open_dataset('/gpfs/data/greenocean/software/resources/regrid/mesh_mask3_6.nc')
    tmesh['csize'] = tmesh.tmask[0,0,:,:] * tmesh.e1t[0,:,:] * tmesh.e2t[0,:,:]
    tmesh['csize'].attrs = dict(
        description="model cell area at surface, 0 if land",
        units="m^2",)
    print('done with csize')
    
    t_yearlist = \
    bp.make_yearlist(tmin,tmax,'diad', tr, '/gpfs/afm/greenocean/software/runs/')
    s1ASA = xr.open_mfdataset(t_yearlist)
    print('done loading')
    s1ASA['time_counter'] = s1ASA.indexes['time_counter'].to_datetimeindex()

    s1ASA_DJF = s1ASA['Cflx'].sel(time_counter=s1ASA.time_counter.dt.season == 'DJF').\
    groupby('time_counter.year').mean()
    s1ASA_MAM = s1ASA['Cflx'].sel(time_counter=s1ASA.time_counter.dt.season == 'MAM').\
    groupby('time_counter.year').mean()
    s1ASA_JJA = s1ASA['Cflx'].sel(time_counter=s1ASA.time_counter.dt.season == 'JJA').\
    groupby('time_counter.year').mean()
    s1ASA_SON = s1ASA['Cflx'].sel(time_counter=s1ASA.time_counter.dt.season == 'SON').\
    groupby('time_counter.year').mean()


    s1ASA_DJF_sz = s1ASA_DJF*tmesh.csize
    s1ASA_DJF_so = s1ASA_DJF_sz[:,0:37,:].values
    s1ASA_DJF_so = np.nansum(np.nansum(s1ASA_DJF_so, axis = 2),axis = 1)
    s1ASA_ts = np.zeros((4,np.shape(s1ASA_DJF_so)[0]))
    s1ASA_ts[0,:] = s1ASA_DJF_so

    s1ASA_MAM_sz = s1ASA_MAM*tmesh.csize
    s1ASA_MAM_so = s1ASA_MAM_sz[:,0:37,:].values
    s1ASA_MAM_so = np.nansum(np.nansum(s1ASA_MAM_so, axis = 2),axis = 1)
    s1ASA_ts[1,:] = s1ASA_MAM_so

    s1ASA_JJA_sz = s1ASA_JJA*tmesh.csize
    s1ASA_JJA_so = s1ASA_JJA_sz[:,0:37,:].values
    s1ASA_JJA_so = np.nansum(np.nansum(s1ASA_JJA_so, axis = 2),axis = 1)
    s1ASA_ts[2,:] = s1ASA_JJA_so

    s1ASA_SON_sz = s1ASA_SON*tmesh.csize
    s1ASA_SON_so = s1ASA_SON_sz[:,0:37,:].values
    s1ASA_SON_so = np.nansum(np.nansum(s1ASA_SON_so, axis = 2),axis = 1)
    s1ASA_ts[3,:] = s1ASA_SON_so

    ds = xr.Dataset(
     {"Cflx_seasonally": (("season","yr"), s1ASA_ts)},
        coords={
            "yr": s1ASA_DJF_sz.year.values,
            "season": np.arange(1,5,1)
        },
        attrs={
            "desc": "non-weighted by days in month, total SO mol/s seasonal cflx DJF is first",
      },
       )

    ds.to_netcdf(f'./ncs/{tr}_seasonal_cflx_total_SO.nc')

# get_seas_co2('TOM12_TJ_1ASA',1948,2100)
# get_seas_co2('TOM12_TJ_1BSA',1948,2100)
get_seas_co2('TOM12_TJ_2ASA',1948,2100)
get_seas_co2('TOM12_TJ_2BSA',1948,2100)
get_seas_co2('TOM12_TJ_3ASA',1948,2100)
# get_seas_co2('TOM12_TJ_3BSA',1948,2100)