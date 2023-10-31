import pandas as pd
import xarray as xr
import time
import sys
sys.path.append('/gpfs/home/mep22dku/scratch/NEMO-related/')
from pyCDFTOOLS.cdfmocsig import *
import numpy as np
import glob
import netCDF4, copy


def make_nc(name, times, latV, sigma2000, dmoc2000):

    data_vars = {

                 'dmoc2000':(['time_counter', 'sigma2000', 'latV'], dmoc2000,
    {'units': 'Sv',
    'long_name':'sigma-coordinates overturning, ref pressure 2000 dbar'}),
    }

    coords = {'time_counter': (['time_counter'], times),
    'latV': (['latV'],latV),
    'sigma2000': (['sigma2000'], sigma2000),
             }

    attrs = {'made in':'/gpfs/home/mep22dku/scratch/SOZONE/overturning/scriptsSigmaOverturning/TOM-ot-1A.py',
    'desc': 'concatenate monthly overturning output into yearly and give good dates for later processing'
    }
    savenam = name
    ds = xr.Dataset(data_vars=data_vars,
    coords=coords,
    attrs=attrs)
    ds.to_netcdf(savenam)
    
    return 


def wrap_cdfmocsig(yr, tdir, tsig = 2000, **kwargs):
    
    fileV = f'ORCA2_1m_{yr}0101_{yr}1231_grid_V.nc'
    fileT = f'ORCA2_1m_{yr}0101_{yr}1231_grid_T.nc'
    bins = sigma_bins(tsig)
    # print(bins)#use the 2000 version. maybe look at where the sigma 
    data_dir = f'/gpfs/data/greenocean/software/runs/{tdir}/'
    # for putting extra options in
    #   -- kt       = number for using a specified time entry (python indexing)
    #   -- kz       = number for using a specified vertical level/layer (python indexing)
    #   -- lprint   = True   for printing out variable names in netcdf file
    #   -- lverb    = True   for printing out more information
    #   -- lg_vvl   = True   for using s-coord (time-varying metric)
    #   -- ldec     = True   decompose the MOC into some components
    #   -- leiv     = True   for adding the eddy induced velocity component
    #        eivv_var = string for EIV-v variable name
    #   -- lisodep  = True   (not yet implemented) output zonal averaged isopycnal depth
    #   -- lntr     = True   (not yet implemented) do binning with neutral density


    # generate a field
    sigma, depi, latV, dmoc, opt_dic = cdfmocsig(data_dir, fileV, "vomecrty", fileT, "votemper", "vosaline", bins, **kwargs)
    
    return sigma, depi, latV, dmoc, opt_dic

#sigma, depi, latV, dmoc, opt_dic = wrap_cdfmocsig(1950, 'TOM12_TJ_1AA6', **kwargs)


def get_overturning_TOM(year, run):

    w = time.time()
    tdir = '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/oceanFields/fullTOM_OT/'
    name1 = f'{run}_{year}_mocsig.nc'
    name = f'{tdir}{name1}'
    print(name)
    
    dmoc_stor = np.zeros([12, 158, 149])
    times = pd.date_range(f"{year}/01/01",f"{year+1}/01/01",freq='MS',closed='left')

    
    for i in range(0,12):

        kwargs =  {"kt"     : i,
                   "lprint" : False,
                   "lg_vvl" : False,
                   "ldec"   : False,
                   "leiv"   : False,  "eivv_var" : "voce_eiv",
                   "lisodep": False,
                   "lntr"   : False,
                   "lverb"  : True}
        
        sigma, depi, latV, dmoc, opt_dic = wrap_cdfmocsig(year, run, **kwargs)
        dmoc_stor[i,:,:] = dmoc

    make_nc(name, times, latV, sigma, dmoc_stor)
    
    w2 = time.time()
    print(w2-w)
    
    return
        
for k in range(1950,2100):
    get_overturning_TOM(k, 'TOM12_TJ_1AA6')        
    get_overturning_TOM(k, 'TOM12_TJ_1BA6')
    get_overturning_TOM(k, 'TOM12_TJ_2AA6')
    get_overturning_TOM(k, 'TOM12_TJ_2BA6')
    get_overturning_TOM(k, 'TOM12_TJ_3AA6')
    get_overturning_TOM(k, 'TOM12_TJ_3BA6')
