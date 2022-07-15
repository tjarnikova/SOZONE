import sys
sys.path.append('/gpfs/home/mep22dku/scratch/SOZONE/MO_pipeline/')
import scendict as sc
import netCDF4 as nc
import xarray as xr
import numpy as np
import warnings
import cartopy as cp
import cartopy.crs as ccrs
import cmocean as cm
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
import glob

def get_Cflx(trun):
    yrstart = 1940; yrend = 2100
    yrs = np.arange(yrstart,yrend+1,1)
    yearflx_ts = np.zeros([len(yrs),12,149,182])
    fnam = f'./ncs/run{trun}_Cflx_pG_month.nc'
    rdir = '/gpfs/afm/greenocean/software/runs/TOM12_TJ_'
    print(trun)
    for i in range(0,len(yrs)):
        yr = yrs[i]
        ncnam = 'diad'; varnam = 'Cflx'
        w = glob.glob(f'{rdir}{trun}/ORCA*{yr}01*{ncnam}_T.nc')

        try: 
            tnam = w[0]
            tfil = nc.Dataset(tnam)

            tq = tfil[varnam][:,:,:]
            sid = 60*60*24
        # now it's in petagrams total done by each cell 
            totflx = surfar_times_days_in_month * tq * sid * 12 * 1e-15
            
            yearflx_ts[i,:,:,:] = totflx
        except:
            yearflx_ts[i,:,:,:] = np.nan
                          
    ds = xr.Dataset(
     {"Cflx": (("yr", "mon", "y", "x" ), yearflx_ts)},
        coords={
            "yr": np.arange(1940,2101,1),
            "mon": np.arange(1,13,1),
            "x": np.arange(0,182,1),
            "y": np.arange(0,149,1),
        },
        attrs={
            "desc": "multiply Cflx by size of each box and days in month to get petagrams/month",
      },
       )
        
    ds.to_netcdf(fnam)
    
get_Cflx('1AS1') 
get_Cflx('1AW1') 
get_Cflx('1AC1') 
get_Cflx('2AS1') 
get_Cflx('2AW1') 
get_Cflx('2AC1') 