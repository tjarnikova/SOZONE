#yearly subset ptrc
import numpy as np
from cmocean import cm
import cartopy as cp
import cartopy.crs as ccrs
import netCDF4 as nc
import matplotlib.pyplot as plt
import xarray as xr
import sys
sys.path.append('/gpfs/home/mep22dku/scratch/SOZONE')
#list of models
sys.path.append('/gpfs/home/mep22dku/scratch/SOZONE/UTILS')
import lom
import utils as ut

import warnings
from datetime import datetime
warnings.filterwarnings('ignore')
import cartopy.feature as cfeature
from importlib import reload
import matplotlib.path as mpath
import glob
import pickle
import pandas as pd
import seawater
import time


def make_yearly_subset_ptrc_TADICCHL(yr,runname):

    #what is new file going to be called:
    savenam = f'/gpfs/data/greenocean/software/resources/MEDUSA/PROC2/medusa_{runname}_1y_{yr}ptrc-T-CHLTADIC.nc'
    print(savenam)
    
    #get by-month dimension for this year:
    times = pd.date_range(f"{yr}/01/01",f"{yr+1}/01/01",freq='M',closed='left')
    #get the spatial dimensions from a variable


    #get the files we are converting
    td = f'/gpfs/data/greenocean/software/resources/MEDUSA/ukesm_allscen_ptrcT_TADIC/medusa_{runname}*_1m_{yr}*01-*ptrc-T.nc'
    fils = glob.glob(td)
    fils.sort()
    
    if len(fils) != 12:
        print(f'missing files for year {yr} in {runname}: we have {len(fils)}')
        return

    else:
        ## define variables that we are saving
        
        q = xr.open_dataset(fils[0])
        #print(q)
        nav_lat = q['nav_lat'].values
        nav_lon = q['nav_lon'].values
        deptht = q['deptht'].values

        ALK = np.zeros([12,75,332,362])
        DIC = np.zeros([12,75,332,362])
        CHD = np.zeros([12,75,332,362])
        CHN = np.zeros([12,75,332,362])
        
        for i in range(0,12):
            tfil = xr.open_dataset(fils[i])
            ALK[i,:,:,:] = tfil['ALK'][:,:,:].values
            DIC[i,:,:,:] = tfil['DIC'][:,:,:].values
            CHD[i,:,:,:] = tfil['CHD'][:,:,:].values
            CHN[i,:,:,:] = tfil['CHN'][:,:,:].values
            
        # define data with variable attributes

        
        data_vars = {'ALK':(['time_counter','deptht','y', 'x'], ALK,
                                 {'units': 'mmol/m3',
                                  'long_name':''}),
                     'DIC':(['time_counter','deptht', 'y', 'x'], DIC,
                                 {'units': 'mmol/m3',
                                  'long_name':''}),   
                     'CHD':(['time_counter','deptht', 'y', 'x'], CHD,
                                 {'units': 'mg-Chl/m3',
                                  'long_name':''}), 
                     'CHN':(['time_counter','deptht', 'y', 'x'], CHN,
                                 {'units': 'mg-Chl/m3',
                                  'long_name':''}), 
                    }

        # define coordinates
        coords = {'time_counter': (['time_counter'], times),
            'nav_lat': (['y','x'], nav_lat),
            'nav_lon': (['y','x'], nav_lon),
            'deptht': (['deptht'], deptht)}


        # define global attributes
        attrs = {'made in':'SOZONE/MEDUSA/makeYearlyMEDUSAsubsetfiles.ipynb',
                'desc': 'yearly medusa files, saving only variables of interest'
                }

        ds = xr.Dataset(data_vars=data_vars,
                        coords=coords,
                        attrs=attrs)

        try:
            ds.to_netcdf(savenam)
        except:
            print(f'seems like {savenam} exists already')
    
#make_yearly_subset_nc(1954,'cj198')



#1h
runname = 'bc370'
yrs = np.arange(1950,2100,1)
for y in yrs:
    make_yearly_subset_ptrc_TADICCHL(y,runname)    

#1a
runname = 'be682'
yrs = np.arange(2015,2100,1)
for y in yrs:
    make_yearly_subset_ptrc_TADICCHL(y,runname)

#1b
runname = 'ce417'
yrs = np.arange(2015,2100,1)
for y in yrs:
    make_yearly_subset_ptrc_TADICCHL(y,runname)

#2h
runname = 'cj198'
yrs = np.arange(1950,2015,1)
for y in yrs:
    make_yearly_subset_ptrc_TADICCHL(y,runname)    

#2a
runname = 'cj880'
yrs = np.arange(2015,2100,1)
for y in yrs:
    make_yearly_subset_ptrc_TADICCHL(y,runname)
    
#2b
runname = 'cj881'
yrs = np.arange(2015,2100,1)
for y in yrs:
    make_yearly_subset_ptrc_TADICCHL(y,runname)
    
    
#3h
runname = 'cj200'
yrs = np.arange(1990,2015,1)
for y in yrs:
    make_yearly_subset_ptrc_TADICCHL(y,runname)    
    
#3a
runname = 'cj484'
yrs = np.arange(2015,2100,1)
for y in yrs:
    make_yearly_subset_ptrc_TADICCHL(y,runname)    
    
#3a
runname = 'cj504'
yrs = np.arange(2015,2100,1)
for y in yrs:
    make_yearly_subset_ptrc_TADICCHL(y,runname)   