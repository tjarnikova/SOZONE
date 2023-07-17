#put python script here
#syntax  python runSigmaOverturning.py bc370o 1950-01-01 2014-12-01 
import sys
import arrow
import numpy as np
import xarray as xr
import pandas as pd
import glob
sys.path.append('/gpfs/home/mep22dku/scratch/NEMO-related/')
import pyCDFTOOLS
from pyCDFTOOLS.cdfmocsig import *

tvars = sys.argv
exp = tvars[1]
start  = tvars[2]
end = tvars[3]

print(f' running sigma moc extraction on {exp}, {start} to {end}')

data_dir = '/gpfs/data/greenocean/software/resources/MEDUSA/'
resdir = '/gpfs/data/greenocean/software/resources/MEDUSA/ukesm_allscen_mocsig/'

##### helperfunctions
def wrap_cdfmocsig(fileV, fileT, tsig = 2000):
    bins = sigma_bins(tsig)
    # print('')
    # print('bins')
    # print(bins)#use the 2000 version. maybe look at where the sigma 
    data_dir = '/gpfs/data/greenocean/software/resources/MEDUSA/'
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
    kwargs =  {"kt"     : 0,
               "lprint" : False,
               "lg_vvl" : False,
               "ldec"   : False,
               "leiv"   : False,  "eivv_var" : "voce_eiv",
               "lisodep": False,
               "lntr"   : False,
               "lverb"  : True}

    # generate a field
    sigma, depi, latV, dmoc, opt_dic = cdfmocsig(data_dir, fileV, "vo", fileT, "thetao", "so", bins, **kwargs)
    
    return sigma, depi, latV, dmoc, opt_dic



def make_nc(name, times, latV, sigma0, dmoc0, sigma1000, dmoc1000, sigma2000, dmoc2000):

    data_vars = {'dmoc0':(['time_counter', 'sigma0', 'latV'], dmoc0,
    {'units': 'Sv',
    'long_name':'sigma-coordinates overturning, ref pressure 0 dbar'}),

                 'dmoc1000':(['time_counter', 'sigma1000', 'latV'], dmoc1000,
    {'units': 'Sv',
    'long_name':'sigma-coordinates overturning, ref pressure 1000 dbar'}),

                 'dmoc2000':(['time_counter', 'sigma2000', 'latV'], dmoc2000,
    {'units': 'Sv',
    'long_name':'sigma-coordinates overturning, ref pressure 2000 dbar'}),
    }

    coords = {'time_counter': (['time_counter'], times),
 #       'time_centered': (['time_centered'], times),
    'latV': (['latV'],latV),
    'sigma0': (['sigma0'], sigma0),
    'sigma1000': (['sigma1000'], sigma1000),
    'sigma2000': (['sigma2000'], sigma2000),
             }

    attrs = {'made in':'overturning/overturning/sigma_overturning.ipynb',
    'desc': 'concatenate monthly overturning output into yearly and give good dates for later processing'
    }
    savenam = name
    ds = xr.Dataset(data_vars=data_vars,
    coords=coords,
    attrs=attrs)
    ds.to_netcdf(savenam)
    
    return 

### script

start_run = arrow.get(start)
end_run = arrow.get(end)
arrow_array = []
for r in arrow.Arrow.span_range('month', start_run, end_run):
    arrow_array.append(r)

dayslen = len(arrow_array)
for i in range(0,dayslen):
    tdate = arrow_array[i][0]
    ddmmmyy = tdate.format('DDMMMYY').lower()
    ymd = tdate.format('YYYYMM')
    month = (tdate.format('MM'))
    year = (tdate.format('YYYY'))
    times = pd.date_range(f"{year}/{month}/01",f"{year}/{month}/02",freq='D',closed='left')

    
    t_fil = glob.glob(f'{data_dir}/ukesm_allscen_gridT_TS/nemo_{exp}_1m_{ymd}*grid-T.nc')
    q = (t_fil[0])
    w = q.rsplit('/gpfs/data/greenocean/software/resources/MEDUSA/', 1)
    tstr = (w[1])

    v_fil = glob.glob(f'{data_dir}/ukesm_allscen_gridV_vo/nemo_{exp}_1m_{ymd}*grid-V.nc')
    q = (v_fil[0])
    w = q.rsplit('/gpfs/data/greenocean/software/resources/MEDUSA/', 1)
    vstr = (w[1])
    
    tfil = (tstr)
    vfil = (vstr)
    fnam = f'{resdir}/nemo_{exp}_1m_{ymd}_mocsig.nc'
    print(fnam)
    sigma0, depi, latV0, dmoc0, opt_dic0 = wrap_cdfmocsig(vfil, tfil, 0)
    sigma1000, depi, latV1000, dmoc1000, opt_dic1000 = wrap_cdfmocsig(vfil, tfil, 1000)
    sigma2000, depi, latV2000, dmoc2000, opt_dic2000 = wrap_cdfmocsig(vfil, tfil, 2000)
    make_nc(fnam, times, latV0, sigma0, dmoc0, sigma1000, dmoc1000, sigma2000, dmoc2000)
    