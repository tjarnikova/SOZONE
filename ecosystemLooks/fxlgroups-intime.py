#put python script here
import numpy as np

import netCDF4 as nc
import xarray as xr
import sys

import warnings
from datetime import datetime
warnings.filterwarnings('ignore')

import glob
import pandas as pd


###

regs = ['ARCTIC', 'P1', 'P2', 'P3', 'P4', 'P5', 'A1', 'A2', 'A3', 'A4', 'A5', 'I3', 'I4', 'I5']

regdict = {'ARCTIC' : {'number' : 0.5},
           'P1' : {'number': 1.0},
          'P2' : {'number': 1.2},
           'P3' : {'number': 1.4},
           'P4' : {'number': 1.6},
           'P5' : {'number': 1.8},
            'A1' : {'number': 2.4},
          'A2' : {'number': 2.6},
           'A3' : {'number': 2.8},
           'A4' : {'number': 3},
           'A5' : {'number': 3.2},
           'I3' : {'number': 3.6},
           'I4' : {'number': 3.8},
           'I5' : {'number': 4},
           
          }
    
tics = []
tcm = 'Spectral'
tmask = nc.Dataset('/gpfs/data/greenocean/software/resources/breakdown/clq_basin_masks_ORCA.nc')

maskno = np.zeros([149,182])
for i in range(0, len(regs)):
    maskno[tmask[regs[i]][:] == 1] = regdict[regs[i]]['number']
    tics.append(regdict[regs[i]]['number'])
maskno[maskno == 0] = np.nan

mask_latbands = np.copy(maskno)

mask_latbands[maskno == 0.5] = 1
mask_latbands[(maskno == 1) | (maskno == 2.4)] = 2
mask_latbands[(maskno == 1.2) | (maskno == 2.6)] = 3
mask_latbands[(maskno == 1.4) | (maskno == 2.8) | (maskno == 3.6)] = 4
mask_latbands[(maskno == 1.6) | (maskno == 3.0) | (maskno == 3.8)] = 5
mask_latbands[(maskno == 1.8) | (maskno == 3.2) | (maskno == 4.0)] = 6

#####
tmesh = xr.open_dataset('/gpfs/data/greenocean/software/resources/regrid/mesh_mask3_6.nc')
tmesh['csize'] = tmesh.tmask[0,0,:,:] * tmesh.e1t[0,:,:] * tmesh.e2t[0,:,:]

csize_broad = np.zeros([31,149,182])
for i in range(0,31):
    csize_broad[i,:,:] = tmesh['csize'].values
cvol = csize_broad * tmesh['e3t_0'][0,:,:,:] * tmesh['tmask'][0,:,:,:]

cdepth = tmesh['e3t_0'][0,:,:,:] * tmesh['tmask'][0,:,:,:]
cdepth_broad = np.zeros([12,31,149,182])
for i in range(0,12):
    cdepth_broad[i,:,:,:] = cdepth
    
def make_yearlist(yrst, yrend, dtype, tr, baseDir = '/gpfs/afm/greenocean/software/runs'):
    yrs = np.arange(yrst,yrend+1,1)
    ylist = []
    for i in range(0,len(yrs)):
        ty = f'{baseDir}/{tr}/ORCA2_1m_{yrs[i]}*{dtype}*.nc'
        t2 = glob.glob(ty)
        #print(t2)
        ylist.append(t2[0])
    return ylist

def gimme_plant(ds, plant):
    '''
    takes ds of type ptrc, calculates seasonal by-lat depth-integrated means of different biological tracers.
    '''
    seas_lat_phyto = np.zeros([12,6]) #storage array
    #print(ds[plant].long_name)
    tmn = ds[plant] #.groupby('time_counter.season').mean('time_counter') #get seasonal mean1
    
    tmn_test = tmn*cdepth_broad*1000 #* cdepth * 1000 # units in mols/m2 = mols/L * m * L/m3, each depth cell now in mol/m2
    tmn_molm2 = np.nansum(tmn_test, axis = 1) #integrate, ie sum
    
    for s in range(0,12):        
        for b in range(0,6):
            tmn_molm2_formask = np.copy(tmn_molm2) #copy for manipulations
            tmn_molm2_formask_tseas = tmn_molm2_formask[s,:,:] # 
            tmn_molm2_formask_tseas[mask_latbands != b+1] = 0
            csize_formask = np.copy(csize_broad[0,:,:])
            csize_formask[mask_latbands != b+1] = 0
            seas_lat_phyto[s,b] = np.ma.average(tmn_molm2_formask_tseas[:,:], weights=csize_formask)

    return seas_lat_phyto

###
def make_tracer_seas_lat_ptrc(yrst, tr, baseDir = '/gpfs/afm/greenocean/software/runs/'):
    
    tdir = '/gpfs/home/mep22dku/scratch/SOZONE/ecosystemLooks/depthint-ptrc/'
    tnam = f'{tdir}{tr}-ptrc-{yrst}.nc'
    print(tnam)
    
    dtype = 'ptrc_T'
    baseDir = '/gpfs/afm/greenocean/software/runs/'
    yrend = yrst #
    ylist = make_yearlist(yrst, yrend, dtype, tr, baseDir)
    ds = xr.open_dataset(ylist[0])
    
    times = pd.date_range(f"{yrst}/01/01",f"{yrst+1}/01/01",freq='MS',closed='left')

    seas_lat_Alkalini = gimme_plant(ds, 'Alkalini')
    seas_lat_O2 = gimme_plant(ds, 'O2')
    seas_lat_DIC = gimme_plant(ds, 'DIC')
    seas_lat_PIIC = gimme_plant(ds, 'PIIC')    
    
    seas_lat_DOC = gimme_plant(ds, 'DOC')
    seas_lat_CaCO3 = gimme_plant(ds, 'CaCO3')
    seas_lat_ARA = gimme_plant(ds, 'ARA')
    seas_lat_POC = gimme_plant(ds, 'POC')   
    seas_lat_GOC = gimme_plant(ds, 'GOC')   
    
    seas_lat_NO3 = gimme_plant(ds, 'NO3')
    seas_lat_Si = gimme_plant(ds, 'Si')
    seas_lat_PO4 = gimme_plant(ds, 'PO4')
    seas_lat_Fer = gimme_plant(ds, 'Fer')   
    
    seas_lat_DIA = gimme_plant(ds, 'DIA') #phyto
    seas_lat_MIX = gimme_plant(ds, 'MIX')
    seas_lat_COC = gimme_plant(ds, 'COC')
    seas_lat_PIC = gimme_plant(ds, 'PIC')
    seas_lat_PHA = gimme_plant(ds, 'PHA')
    seas_lat_FIX = gimme_plant(ds, 'FIX')

    seas_lat_BAC = gimme_plant(ds, 'BAC') #bacterai

    seas_lat_PRO = gimme_plant(ds, 'PRO') #zoos
    seas_lat_PTE = gimme_plant(ds, 'PTE')
    seas_lat_MES = gimme_plant(ds, 'MES')
    seas_lat_GEL = gimme_plant(ds, 'GEL')
    seas_lat_MAC = gimme_plant(ds, 'MAC')
    
    
    
    data_vars = {
        
                 'Alkalini':(['time_counter',  'lat_band'], seas_lat_Alkalini,
                 {'units': 'mol/m2'}),
                
                 'O2':(['time_counter',  'lat_band'], seas_lat_O2,
                         {'units': 'mol/m2'}),
                 'DIC':(['time_counter',  'lat_band'], seas_lat_DIC,
                         {'units': 'mol/m2'}),
                 'PIIC':(['time_counter',  'lat_band'], seas_lat_PIIC,
                         {'units': 'mol/m2'}),
                 'DOC':(['time_counter',  'lat_band'], seas_lat_DOC,
                         {'units': 'mol/m2'}), 
                 'CaCO3':(['time_counter',  'lat_band'], seas_lat_CaCO3,
                         {'units': 'mol/m2'}),
                 
                 'ARA':(['time_counter',  'lat_band'], seas_lat_ARA,
                         {'units': 'mol/m2'}),
                 
                 'POC':(['time_counter',  'lat_band'], seas_lat_POC,
                         {'units': 'mol/m2'}),
                 'GOC':(['time_counter',  'lat_band'], seas_lat_GOC,
                         {'units': 'mol/m2'}),
                 'NO3':(['time_counter',  'lat_band'], seas_lat_NO3,
                         {'units': 'mol/m2'}),
                 'Si':(['time_counter',  'lat_band'], seas_lat_Si,
                         {'units': 'mol/m2'}),
                 'PO4':(['time_counter',  'lat_band'], seas_lat_PO4,
                         {'units': 'mol/m2'}),
                 'Fer':(['time_counter',  'lat_band'], seas_lat_Fer,
                         {'units': 'mol/m2'}),
                         
        
                 'DIA':(['time_counter',  'lat_band'], seas_lat_DIA,
                         {'units': 'mol/m2'}),
                
                 'MIX':(['time_counter',  'lat_band'], seas_lat_MIX,
                         {'units': 'mol/m2'}),
                 'COC':(['time_counter',  'lat_band'], seas_lat_COC,
                         {'units': 'mol/m2'}),
                 'PIC':(['time_counter',  'lat_band'], seas_lat_PIC,
                         {'units': 'mol/m2'}),
                 'PHA':(['time_counter',  'lat_band'], seas_lat_PHA,
                         {'units': 'mol/m2'}), 
                 'FIX':(['time_counter',  'lat_band'], seas_lat_FIX,
                         {'units': 'mol/m2'}),
                 
                 'BAC':(['time_counter',  'lat_band'], seas_lat_BAC,
                         {'units': 'mol/m2'}),
                 
                 'PRO':(['time_counter',  'lat_band'], seas_lat_PRO,
                         {'units': 'mol/m2'}),
                 'PTE':(['time_counter',  'lat_band'], seas_lat_PTE,
                         {'units': 'mol/m2'}),
                 'MES':(['time_counter',  'lat_band'], seas_lat_MES,
                         {'units': 'mol/m2'}),
                 'GEL':(['time_counter',  'lat_band'], seas_lat_GEL,
                         {'units': 'mol/m2'}),
                 'MAC':(['time_counter',  'lat_band'], seas_lat_MAC,
                         {'units': 'mol/m2'}),
                }

    # define coordinates
    coords = {'time_counter': (['time_counter'], times),\
             'lat_band': (['lat_band'], np.arange(1,7,1)),}

    # define global attributes
    attrs = {'made in':'SOZONE/ecosystemLooks/fxlgroups-intime.ipynb',
             'latitude bands': 'see notebook, 1 is arctic, 6 is SO',
            }
    
#     # create dataset
    ds2 = xr.Dataset(data_vars=data_vars,
                    coords=coords,
                    attrs=attrs)
    
    ds2.to_netcdf(f'{tnam}')
    
for i in range(1950,2100):
    make_tracer_seas_lat_ptrc(i, 'TOM12_TJ_1ASA')
    make_tracer_seas_lat_ptrc(i, 'TOM12_TJ_1BSA')
    make_tracer_seas_lat_ptrc(i, 'TOM12_TJ_1AA6')
    make_tracer_seas_lat_ptrc(i, 'TOM12_TJ_1BA6')
#####
