#put python script here
import numpy as np
import netCDF4 as nc
import xarray as xr
import sys
from datetime import datetime
import glob
import pickle
import pandas as pd
import seawater


yr = 2002
GCB_DW_C_f = f'/gpfs/data/greenocean/software/runs/TOM12_DW_GC01/ORCA2_1m_{yr}0101_*_ptrc_T.nc'
GCB_DW_C = xr.open_dataset(glob.glob(GCB_DW_C_f)[0])

tmesh = xr.open_dataset('/gpfs/data/greenocean/software/resources/regrid/mesh_mask3_6.nc')
e3t_0 = tmesh.e3t_0


#e3t in the right shape
e3t_0 = tmesh.e3t_0
e3t_s = e3t_0.sel(t = 0)
data_vars = {'e3t_s':(['deptht', 'y', 'x'], e3t_s,
{'units': 'm',
'long_name':'depth, t grid'}),
}
# define coordinates
coords = {
'y': (['y'], tmesh.y.values),
'x': (['x'], tmesh.x.values),
'deptht': (['deptht'], GCB_DW_C.deptht.values)}
# define global attributes
attrs = {'made in':'SOZONE/GRO2_FORCING_EXPERIMENT/anthCarbonAccumulation_figx3.4.2.ipynb',
'desc': 'e3t in the right shape'
}
ds2 = xr.Dataset(data_vars=data_vars,
coords=coords,
attrs=attrs)



def make_yearlist(yrst, yrend, dtype, tr, baseDir = '/gpfs/data/greenocean/software/runs/'):
    yrs = np.arange(yrst,yrend,1)
    ylist = []
    for i in range(0,len(yrs)):
        ty = f'{baseDir}/{tr}/ORCA2_1m_{yrs[i]}*{dtype}*.nc'
        t2 = glob.glob(ty)
        #print(t2)
        ylist.append(t2[0])
    return ylist

def get_anthdic_mol_m2(model_name = 'TOM12_RW_GS00'):
    GS00_55 = xr.open_mfdataset(make_yearlist(1955, 1960, 'ptrc', model_name)) #name based on model GS00, can be anything
    GS00_00 = xr.open_mfdataset(make_yearlist(2000, 2005, 'ptrc', model_name))
    
    GS00_DIC_55_yr = GS00_55.DIC.groupby('time_counter.year').mean().mean(dim = 'year')
    GS00_DIC_00_yr = GS00_00.DIC.groupby('time_counter.year').mean().mean(dim = 'year')

    GS00_anthdic = GS00_DIC_00_yr-GS00_DIC_55_yr #subtract carbon content
    GS00_anthdic_molm2 = GS00_anthdic * ds2.e3t_s.load() * 1000 #from mol/L to mol/m3, with e3t get to mol/m2
    GS00_anthdic_molm2_2d = np.nansum(GS00_anthdic_molm2, axis = 0)
    GS00_anthdic_molm2_2d[GS00_anthdic_molm2_2d == 0] = np.nan
    GS00_anthdic_molm2_2d_3000 = np.nansum(GS00_anthdic_molm2[0:27,:,:], axis = 0)
    return GS00_anthdic_molm2_2d, GS00_anthdic_molm2_2d_3000

def get_relevant_metrics(model_name):
    
    print(f'relevant metrics for {model_name}')
    
    gridT = xr.open_mfdataset(make_yearlist(1955, 2005, 'grid_T', model_name))
    diadT = xr.open_mfdataset(make_yearlist(1955, 2005, 'diad_T', model_name))

    
    sos = gridT.sos.groupby('time_counter.year').mean().mean(dim = 'year')
    mldr10_1 = gridT.mldr10_1.groupby('time_counter.year').mean().mean(dim = 'year')
    somxl030 = gridT.somxl030.groupby('time_counter.year').mean().mean(dim = 'year')
    Cflx = diadT.Cflx.groupby('time_counter.year').mean().mean(dim = 'year')
    
    ###anthropogenic storage
    GS00_55 = xr.open_mfdataset(make_yearlist(1955, 1960, 'ptrc', model_name)) #name based on model GS00, can be anything
    GS00_00 = xr.open_mfdataset(make_yearlist(2000, 2005, 'ptrc', model_name))
    
    GS00_DIC_55_yr = GS00_55.DIC.groupby('time_counter.year').mean().mean(dim = 'year')
    GS00_DIC_00_yr = GS00_00.DIC.groupby('time_counter.year').mean().mean(dim = 'year')

    GS00_anthdic = GS00_DIC_00_yr-GS00_DIC_55_yr #subtract carbon content
    GS00_anthdic_molm2 = GS00_anthdic * ds2.e3t_s.load() * 1000 #from mol/L to mol/m3, with e3t get to mol/m2
    GS00_anthdic_molm2_2d = np.nansum(GS00_anthdic_molm2, axis = 0)
    GS00_anthdic_molm2_2d[GS00_anthdic_molm2_2d == 0] = np.nan
    GS00_anthdic_molm2_2d_3000 = np.nansum(GS00_anthdic_molm2[0:27,:,:], axis = 0)

    savenam = f'./extracted/anthdic_and_aux_{model_name}.nc'
    data_vars = {'sos':(['y', 'x'], sos),
                 'mldr10_1':(['y', 'x'], mldr10_1),
                 'somxl030':(['y', 'x'], somxl030),
                 'Cflx':(['y', 'x'], Cflx),
                 'anthdic_molm2':(['y', 'x'], GS00_anthdic_molm2_2d),
                 'anthdic_molm2_3000':(['y', 'x'], GS00_anthdic_molm2_2d_3000),
                 
    }
    # define coordinates
    coords = {'nav_lat': (['y','x'], sos.nav_lat),
    'nav_lon': (['y','x'], sos.nav_lon),
    }
    # define global attributes
    attrs = {'made in':'SOZONE/GRO2_FORCING_EXPERIMENT/runner.py',
    'desc': 'yearly medusa files, saving only variables of interest'
    }
    ds = xr.Dataset(data_vars=data_vars,
    coords=coords,
    attrs=attrs)
    ds.to_netcdf(savenam)
    return ds   

# ds_GS00 = get_relevant_metrics('TOM12_RW_GS00')
# ds_GRO2 = get_relevant_metrics('TOM12_RW_GRO2')
# ds_GERA = get_relevant_metrics('TOM12_RW_GERA')
# ds_GSER = get_relevant_metrics('TOM12_RW_GSER')
# ds_1ASA = get_relevant_metrics('TOM12_TJ_1ASA')
# ds_DGA1 = get_relevant_metrics('TOM12_TJ_DGA1')
ds_DGA1 = get_relevant_metrics('TOM12_DW_GA01')
ds_DGA1 = get_relevant_metrics('TOM12_RW_GS00')

