import numpy as np
import netCDF4 as nc
import xarray as xr
import sys

from importlib import reload
import glob
import pandas as pd

print('pojd mi')

tmesh = xr.open_dataset('/gpfs/data/greenocean/software/resources/regrid/mesh_mask3_6.nc')
tmesh['csize'] = tmesh.tmask[0,0,:,:] * tmesh.e1t[0,:,:] * tmesh.e2t[0,:,:]
print('GEA0')
GEA0 = xr.open_dataset('/gpfs/data/greenocean/software/runs/TOM12_TJ_GEA0/C14-ptrc-1959-2003.nc')
GEA0_B14B = GEA0['B14B'].weighted(tmesh['csize']).mean(dim = ['x','y'])
GEA0_C14B = GEA0['C14B'].weighted(tmesh['csize']).mean(dim = ['x','y'])
print('GEA0')
GEB0 = xr.open_dataset('/gpfs/data/greenocean/software/runs/TOM12_TJ_GEB0/C14-ptrc-1959-2003.nc')
GEB0_B14B = GEB0['B14B'].weighted(tmesh['csize']).mean(dim = ['x','y'])
GEB0_C14B = GEB0['C14B'].weighted(tmesh['csize']).mean(dim = ['x','y'])
print('GEA0')
GEC0 = xr.open_dataset('/gpfs/data/greenocean/software/runs/TOM12_TJ_GEC0/C14-ptrc-1959-2003.nc')
GEC0_B14B = GEC0['B14B'].weighted(tmesh['csize']).mean(dim = ['x','y'])
GEC0_C14B = GEC0['C14B'].weighted(tmesh['csize']).mean(dim = ['x','y'])
print('GEA0')
GED0 = xr.open_dataset('/gpfs/data/greenocean/software/runs/TOM12_TJ_GED0/C14-ptrc-1959-2003.nc')
GED0_B14B = GED0['B14B'].weighted(tmesh['csize']).mean(dim = ['x','y'])
GED0_C14B = GED0['C14B'].weighted(tmesh['csize']).mean(dim = ['x','y'])

GEA0_B14B.to_netcdf('./extracted/GEA0_B14B.nc')
GEA0_C14B.to_netcdf('./extracted/GEA0_C14B.nc')
GEB0_B14B.to_netcdf('./extracted/GEB0_B14B.nc')
GEB0_C14B.to_netcdf('./extracted/GEB0_C14B.nc')
GEC0_B14B.to_netcdf('./extracted/GEC0_B14B.nc')
GEC0_C14B.to_netcdf('./extracted/GEC0_C14B.nc')
GED0_B14B.to_netcdf('./extracted/GED0_B14B.nc')
GED0_C14B.to_netcdf('./extracted/GED0_C14B.nc')
