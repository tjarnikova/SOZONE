#put python script here
#point: make lats and lons in a format that is usable by cdo regrid

import numpy as np
import pandas as pd
import xarray as xr
import glob
from datetime import datetime


def convert_files_for_regrid(tnam, yr):
    
    wll = xr.open_dataset('/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/paperFigures/regrid_forcing/TOM12_1960_Cflx.nc')
    w3 = wll.drop_dims('time_counter')

    #add in 
    w = xr.open_dataset(f'/gpfs/data/greenocean/software/resources/windsProcessed/{tnam}_wspd_{yr}_daily.nc')
    w3 = w3.assign_coords({"time_counter": ("time_counter", w.time_counter.values)})
    w3['wspd'] = (['time_counter','y', 'x'], w.wspd.values,
    {'units': 'm/s',
    'long_name':''})

    w3.to_netcdf(f'/gpfs/data/greenocean/software/resources/windsProcessed/{tnam}_wspd_{yr}_4regrid.nc')
    
def runner(tnam,  yrstart, yrend):

    for yr in range(yrstart,yrend):
        convert_files_for_regrid(tnam, yr)

    return    
 
# tnam = 'UKESM_1H'; yrstart = 1940; yrend = 2015
# runner(tnam,  yrstart, yrend)

# tnam = 'UKESM_1FA'; yrstart = 2015; yrend = 2023
# runner(tnam,  yrstart, yrend)

# tnam = 'ERA5_v2023'; yrstart = 1940; yrend = 2023
# runner(tnam,  yrstart, yrend)

tnam = 'UKESM_1FA'; yrstart = 2023; yrend = 2101
runner(tnam,  yrstart, yrend)

tnam = 'UKESM_1FB'; yrstart = 2015; yrend = 2101
runner(tnam,  yrstart, yrend)

tnam = 'UKESM_2FA'; yrstart = 2015; yrend = 2101
runner(tnam,  yrstart, yrend)

tnam = 'UKESM_2FB'; yrstart = 2015; yrend = 2101
runner(tnam,  yrstart, yrend)

tnam = 'UKESM_3FA'; yrstart = 2015; yrend = 2101
runner(tnam,  yrstart, yrend)

tnam = 'UKESM_3FB'; yrstart = 2015; yrend = 2101
runner(tnam,  yrstart, yrend)