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

print('funguje to?')
mapdir = '/gpfs/home/mep22dku/scratch/SOZONE/MEDUSA/BSUB_extractions/EXTRACT/'

t = pickle.load(open(f'{mapdir}UKESM_1A_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_1A_CO2FLUX_SO_DJF = t.sel(time_counter=(t['time_counter.season'] == 'DJF')).values
t = pickle.load(open(f'{mapdir}UKESM_1B_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_1B_CO2FLUX_SO_DJF = t.sel(time_counter=(t['time_counter.season'] == 'DJF')).values
t = pickle.load(open(f'{mapdir}UKESM_2A_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_2A_CO2FLUX_SO_DJF = t.sel(time_counter=(t['time_counter.season'] == 'DJF')).values
t = pickle.load(open(f'{mapdir}UKESM_2B_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_2B_CO2FLUX_SO_DJF = t.sel(time_counter=(t['time_counter.season'] == 'DJF')).values
t = pickle.load(open(f'{mapdir}UKESM_3A_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_3A_CO2FLUX_SO_DJF = t.sel(time_counter=(t['time_counter.season'] == 'DJF')).values
t = pickle.load(open(f'{mapdir}UKESM_3B_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_3B_CO2FLUX_SO_DJF = t.sel(time_counter=(t['time_counter.season'] == 'DJF')).values

pickle.dump(UKESM_1A_CO2FLUX_SO_DJF, open('./EXTRACT/UKESM_1A_CO2FLUX_SO_DJF_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_1B_CO2FLUX_SO_DJF, open('./EXTRACT/UKESM_1B_CO2FLUX_SO_DJF_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_2A_CO2FLUX_SO_DJF, open('./EXTRACT/UKESM_2A_CO2FLUX_SO_DJF_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_2B_CO2FLUX_SO_DJF, open('./EXTRACT/UKESM_2B_CO2FLUX_SO_DJF_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_3A_CO2FLUX_SO_DJF, open('./EXTRACT/UKESM_3A_CO2FLUX_SO_DJF_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_3B_CO2FLUX_SO_DJF, open('./EXTRACT/UKESM_3B_CO2FLUX_SO_DJF_vals_19500-2100.pkl', 'wb'))

t = pickle.load(open(f'{mapdir}TOM12_TJ_1ASA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_1A_CO2FLUX_SO_DJF= t.sel(time_counter=(t['time_counter.season'] == 'DJF')).values
t = pickle.load(open(f'{mapdir}TOM12_TJ_1BSA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_1B_CO2FLUX_SO_DJF= t.sel(time_counter=(t['time_counter.season'] == 'DJF')).values
t = pickle.load(open(f'{mapdir}TOM12_TJ_2ASA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_2A_CO2FLUX_SO_DJF= t.sel(time_counter=(t['time_counter.season'] == 'DJF')).values
t = pickle.load(open(f'{mapdir}TOM12_TJ_2BSA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_2B_CO2FLUX_SO_DJF= t.sel(time_counter=(t['time_counter.season'] == 'DJF')).values
t = pickle.load(open(f'{mapdir}TOM12_TJ_3ASA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_3A_CO2FLUX_SO_DJF= t.sel(time_counter=(t['time_counter.season'] == 'DJF')).values
t = pickle.load(open(f'{mapdir}TOM12_TJ_3BSA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_3B_CO2FLUX_SO_DJF= t.sel(time_counter=(t['time_counter.season'] == 'DJF')).values

pickle.dump(TOM12_1A_CO2FLUX_SO_DJF, open('./EXTRACT/TOM12_1A_CO2FLUX_SO_DJF_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_1B_CO2FLUX_SO_DJF, open('./EXTRACT/TOM12_1B_CO2FLUX_SO_DJF_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_2A_CO2FLUX_SO_DJF, open('./EXTRACT/TOM12_2A_CO2FLUX_SO_DJF_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_2B_CO2FLUX_SO_DJF, open('./EXTRACT/TOM12_2B_CO2FLUX_SO_DJF_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_3A_CO2FLUX_SO_DJF, open('./EXTRACT/TOM12_3A_CO2FLUX_SO_DJF_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_3B_CO2FLUX_SO_DJF, open('./EXTRACT/TOM12_3B_CO2FLUX_SO_DJF_vals_19500-2100.pkl', 'wb'))
###
t = pickle.load(open(f'{mapdir}UKESM_1A_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_1A_CO2FLUX_SO_MAM = t.sel(time_counter=(t['time_counter.season'] == 'MAM')).values
t = pickle.load(open(f'{mapdir}UKESM_1B_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_1B_CO2FLUX_SO_MAM = t.sel(time_counter=(t['time_counter.season'] == 'MAM')).values
t = pickle.load(open(f'{mapdir}UKESM_2A_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_2A_CO2FLUX_SO_MAM = t.sel(time_counter=(t['time_counter.season'] == 'MAM')).values
t = pickle.load(open(f'{mapdir}UKESM_2B_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_2B_CO2FLUX_SO_MAM = t.sel(time_counter=(t['time_counter.season'] == 'MAM')).values
t = pickle.load(open(f'{mapdir}UKESM_3A_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_3A_CO2FLUX_SO_MAM = t.sel(time_counter=(t['time_counter.season'] == 'MAM')).values
t = pickle.load(open(f'{mapdir}UKESM_3B_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_3B_CO2FLUX_SO_MAM = t.sel(time_counter=(t['time_counter.season'] == 'MAM')).values

pickle.dump(UKESM_1A_CO2FLUX_SO_MAM, open('./EXTRACT/UKESM_1A_CO2FLUX_SO_MAM_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_1B_CO2FLUX_SO_MAM, open('./EXTRACT/UKESM_1B_CO2FLUX_SO_MAM_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_2A_CO2FLUX_SO_MAM, open('./EXTRACT/UKESM_2A_CO2FLUX_SO_MAM_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_2B_CO2FLUX_SO_MAM, open('./EXTRACT/UKESM_2B_CO2FLUX_SO_MAM_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_3A_CO2FLUX_SO_MAM, open('./EXTRACT/UKESM_3A_CO2FLUX_SO_MAM_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_3B_CO2FLUX_SO_MAM, open('./EXTRACT/UKESM_3B_CO2FLUX_SO_MAM_vals_19500-2100.pkl', 'wb'))

####

t = pickle.load(open(f'{mapdir}TOM12_TJ_1ASA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_1A_CO2FLUX_SO_MAM= t.sel(time_counter=(t['time_counter.season'] == 'MAM')).values
t = pickle.load(open(f'{mapdir}TOM12_TJ_1BSA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_1B_CO2FLUX_SO_MAM= t.sel(time_counter=(t['time_counter.season'] == 'MAM')).values
t = pickle.load(open(f'{mapdir}TOM12_TJ_2ASA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_2A_CO2FLUX_SO_MAM= t.sel(time_counter=(t['time_counter.season'] == 'MAM')).values
t = pickle.load(open(f'{mapdir}TOM12_TJ_2BSA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_2B_CO2FLUX_SO_MAM= t.sel(time_counter=(t['time_counter.season'] == 'MAM')).values
t = pickle.load(open(f'{mapdir}TOM12_TJ_3ASA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_3A_CO2FLUX_SO_MAM= t.sel(time_counter=(t['time_counter.season'] == 'MAM')).values
t = pickle.load(open(f'{mapdir}TOM12_TJ_3BSA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_3B_CO2FLUX_SO_MAM= t.sel(time_counter=(t['time_counter.season'] == 'MAM')).values

pickle.dump(TOM12_1A_CO2FLUX_SO_MAM, open('./EXTRACT/TOM12_1A_CO2FLUX_SO_MAM_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_1B_CO2FLUX_SO_MAM, open('./EXTRACT/TOM12_1B_CO2FLUX_SO_MAM_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_2A_CO2FLUX_SO_MAM, open('./EXTRACT/TOM12_2A_CO2FLUX_SO_MAM_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_2B_CO2FLUX_SO_MAM, open('./EXTRACT/TOM12_2B_CO2FLUX_SO_MAM_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_3A_CO2FLUX_SO_MAM, open('./EXTRACT/TOM12_3A_CO2FLUX_SO_MAM_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_3B_CO2FLUX_SO_MAM, open('./EXTRACT/TOM12_3B_CO2FLUX_SO_MAM_vals_19500-2100.pkl', 'wb'))

###
t = pickle.load(open(f'{mapdir}UKESM_1A_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_1A_CO2FLUX_SO_JJA = t.sel(time_counter=(t['time_counter.season'] == 'JJA')).values
t = pickle.load(open(f'{mapdir}UKESM_1B_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_1B_CO2FLUX_SO_JJA = t.sel(time_counter=(t['time_counter.season'] == 'JJA')).values
t = pickle.load(open(f'{mapdir}UKESM_2A_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_2A_CO2FLUX_SO_JJA = t.sel(time_counter=(t['time_counter.season'] == 'JJA')).values
t = pickle.load(open(f'{mapdir}UKESM_2B_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_2B_CO2FLUX_SO_JJA = t.sel(time_counter=(t['time_counter.season'] == 'JJA')).values
t = pickle.load(open(f'{mapdir}UKESM_3A_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_3A_CO2FLUX_SO_JJA = t.sel(time_counter=(t['time_counter.season'] == 'JJA')).values
t = pickle.load(open(f'{mapdir}UKESM_3B_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_3B_CO2FLUX_SO_JJA = t.sel(time_counter=(t['time_counter.season'] == 'JJA')).values


pickle.dump(UKESM_1A_CO2FLUX_SO_JJA, open('./EXTRACT/UKESM_1A_CO2FLUX_SO_JJA_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_1B_CO2FLUX_SO_JJA, open('./EXTRACT/UKESM_1B_CO2FLUX_SO_JJA_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_2A_CO2FLUX_SO_JJA, open('./EXTRACT/UKESM_2A_CO2FLUX_SO_JJA_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_2B_CO2FLUX_SO_JJA, open('./EXTRACT/UKESM_2B_CO2FLUX_SO_JJA_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_3A_CO2FLUX_SO_JJA, open('./EXTRACT/UKESM_3A_CO2FLUX_SO_JJA_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_3B_CO2FLUX_SO_JJA, open('./EXTRACT/UKESM_3B_CO2FLUX_SO_JJA_vals_19500-2100.pkl', 'wb'))

t = pickle.load(open(f'{mapdir}TOM12_TJ_1ASA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_1A_CO2FLUX_SO_JJA= t.sel(time_counter=(t['time_counter.season'] == 'JJA')).values
t = pickle.load(open(f'{mapdir}TOM12_TJ_1BSA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_1B_CO2FLUX_SO_JJA= t.sel(time_counter=(t['time_counter.season'] == 'JJA')).values
t = pickle.load(open(f'{mapdir}TOM12_TJ_2ASA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_2A_CO2FLUX_SO_JJA= t.sel(time_counter=(t['time_counter.season'] == 'JJA')).values
t = pickle.load(open(f'{mapdir}TOM12_TJ_2BSA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_2B_CO2FLUX_SO_JJA= t.sel(time_counter=(t['time_counter.season'] == 'JJA')).values
t = pickle.load(open(f'{mapdir}TOM12_TJ_3ASA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_3A_CO2FLUX_SO_JJA= t.sel(time_counter=(t['time_counter.season'] == 'JJA')).values
t = pickle.load(open(f'{mapdir}TOM12_TJ_3BSA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_3B_CO2FLUX_SO_JJA= t.sel(time_counter=(t['time_counter.season'] == 'JJA')).values

pickle.dump(TOM12_1A_CO2FLUX_SO_JJA, open('./EXTRACT/TOM12_1A_CO2FLUX_SO_JJA_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_1B_CO2FLUX_SO_JJA, open('./EXTRACT/TOM12_1B_CO2FLUX_SO_JJA_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_2A_CO2FLUX_SO_JJA, open('./EXTRACT/TOM12_2A_CO2FLUX_SO_JJA_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_2B_CO2FLUX_SO_JJA, open('./EXTRACT/TOM12_2B_CO2FLUX_SO_JJA_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_3A_CO2FLUX_SO_JJA, open('./EXTRACT/TOM12_3A_CO2FLUX_SO_JJA_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_3B_CO2FLUX_SO_JJA, open('./EXTRACT/TOM12_3B_CO2FLUX_SO_JJA_vals_19500-2100.pkl', 'wb'))

t = pickle.load(open(f'{mapdir}UKESM_1A_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_1A_CO2FLUX_SO_SON = t.sel(time_counter=(t['time_counter.season'] == 'SON')).values
t = pickle.load(open(f'{mapdir}UKESM_1B_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_1B_CO2FLUX_SO_SON = t.sel(time_counter=(t['time_counter.season'] == 'SON')).values
t = pickle.load(open(f'{mapdir}UKESM_2A_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_2A_CO2FLUX_SO_SON = t.sel(time_counter=(t['time_counter.season'] == 'SON')).values
t = pickle.load(open(f'{mapdir}UKESM_2B_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_2B_CO2FLUX_SO_SON = t.sel(time_counter=(t['time_counter.season'] == 'SON')).values
t = pickle.load(open(f'{mapdir}UKESM_3A_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_3A_CO2FLUX_SO_SON = t.sel(time_counter=(t['time_counter.season'] == 'SON')).values
t = pickle.load(open(f'{mapdir}UKESM_3B_CO2FLUX_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_3B_CO2FLUX_SO_SON = t.sel(time_counter=(t['time_counter.season'] == 'SON')).values

pickle.dump(UKESM_1A_CO2FLUX_SO_SON, open('./EXTRACT/UKESM_1A_CO2FLUX_SO_SON_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_1B_CO2FLUX_SO_SON, open('./EXTRACT/UKESM_1B_CO2FLUX_SO_SON_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_2A_CO2FLUX_SO_SON, open('./EXTRACT/UKESM_2A_CO2FLUX_SO_SON_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_2B_CO2FLUX_SO_SON, open('./EXTRACT/UKESM_2B_CO2FLUX_SO_SON_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_3A_CO2FLUX_SO_SON, open('./EXTRACT/UKESM_3A_CO2FLUX_SO_SON_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_3B_CO2FLUX_SO_SON, open('./EXTRACT/UKESM_3B_CO2FLUX_SO_SON_vals_19500-2100.pkl', 'wb'))


t = pickle.load(open(f'{mapdir}TOM12_TJ_1ASA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_1A_CO2FLUX_SO_SON= t.sel(time_counter=(t['time_counter.season'] == 'SON')).values
t = pickle.load(open(f'{mapdir}TOM12_TJ_1BSA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_1B_CO2FLUX_SO_SON= t.sel(time_counter=(t['time_counter.season'] == 'SON')).values
t = pickle.load(open(f'{mapdir}TOM12_TJ_2ASA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_2A_CO2FLUX_SO_SON= t.sel(time_counter=(t['time_counter.season'] == 'SON')).values
t = pickle.load(open(f'{mapdir}TOM12_TJ_2BSA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_2B_CO2FLUX_SO_SON= t.sel(time_counter=(t['time_counter.season'] == 'SON')).values
t = pickle.load(open(f'{mapdir}TOM12_TJ_3ASA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_3A_CO2FLUX_SO_SON= t.sel(time_counter=(t['time_counter.season'] == 'SON')).values
t = pickle.load(open(f'{mapdir}TOM12_TJ_3BSA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_3B_CO2FLUX_SO_SON= t.sel(time_counter=(t['time_counter.season'] == 'SON')).values

pickle.dump(TOM12_1A_CO2FLUX_SO_SON, open('./EXTRACT/TOM12_1A_CO2FLUX_SO_SON_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_1B_CO2FLUX_SO_SON, open('./EXTRACT/TOM12_1B_CO2FLUX_SO_SON_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_2A_CO2FLUX_SO_SON, open('./EXTRACT/TOM12_2A_CO2FLUX_SO_SON_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_2B_CO2FLUX_SO_SON, open('./EXTRACT/TOM12_2B_CO2FLUX_SO_SON_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_3A_CO2FLUX_SO_SON, open('./EXTRACT/TOM12_3A_CO2FLUX_SO_SON_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_3B_CO2FLUX_SO_SON, open('./EXTRACT/TOM12_3B_CO2FLUX_SO_SON_vals_19500-2100.pkl', 'wb'))

t = pickle.load(open(f'{mapdir}TOM12_TJ_1ASA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_1A_CO2FLUX_SO_FY = t.groupby('time_counter.year').mean().values  
t = pickle.load(open(f'{mapdir}TOM12_TJ_1BSA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_1B_CO2FLUX_SO_FY = t.groupby('time_counter.year').mean().values  
t = pickle.load(open(f'{mapdir}TOM12_TJ_2ASA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_2A_CO2FLUX_SO_FY = t.groupby('time_counter.year').mean().values 
t = pickle.load(open(f'{mapdir}TOM12_TJ_2BSA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_2B_CO2FLUX_SO_FY = t.groupby('time_counter.year').mean().values  
t = pickle.load(open(f'{mapdir}TOM12_TJ_3ASA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_3A_CO2FLUX_SO_FY = t.groupby('time_counter.year').mean().values  
t = pickle.load(open(f'{mapdir}TOM12_TJ_3BSA_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
TOM12_3B_CO2FLUX_SO_FY = t.groupby('time_counter.year').mean().values  

pickle.dump(TOM12_1A_CO2FLUX_SO_FY, open('./EXTRACT/TOM12_1A_CO2FLUX_SO_FY_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_1B_CO2FLUX_SO_FY, open('./EXTRACT/TOM12_1B_CO2FLUX_SO_FY_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_2A_CO2FLUX_SO_FY, open('./EXTRACT/TOM12_2A_CO2FLUX_SO_FY_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_2B_CO2FLUX_SO_FY, open('./EXTRACT/TOM12_2B_CO2FLUX_SO_FY_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_3A_CO2FLUX_SO_FY, open('./EXTRACT/TOM12_3A_CO2FLUX_SO_FY_vals_19500-2100.pkl', 'wb'))
pickle.dump(TOM12_3B_CO2FLUX_SO_FY, open('./EXTRACT/TOM12_3B_CO2FLUX_SO_FY_vals_19500-2100.pkl', 'wb'))

t = pickle.load(open(f'{mapdir}UKESM_1A_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_1A_CO2FLUX_SO_FY = t.groupby('time_counter.year').mean().values  
t = pickle.load(open(f'{mapdir}UKESM_1B_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_1B_CO2FLUX_SO_FY = t.groupby('time_counter.year').mean().values  
t = pickle.load(open(f'{mapdir}UKESM_2A_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_2A_CO2FLUX_SO_FY = t.groupby('time_counter.year').mean().values  
t = pickle.load(open(f'{mapdir}UKESM_2B_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_2B_CO2FLUX_SO_FY = t.groupby('time_counter.year').mean().values  
t = pickle.load(open(f'{mapdir}UKESM_3A_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_3A_CO2FLUX_SO_FY = t.groupby('time_counter.year').mean().values  
t = pickle.load(open(f'{mapdir}UKESM_3B_Cflx_southocean-50_ts_1950_2100.pkl', 'rb'))
UKESM_3B_CO2FLUX_SO_FY = t.groupby('time_counter.year').mean().values  

pickle.dump(UKESM_1A_CO2FLUX_SO_FY, open('./EXTRACT/UKESM_1A_CO2FLUX_SO_FY_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_1B_CO2FLUX_SO_FY, open('./EXTRACT/UKESM_1B_CO2FLUX_SO_FY_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_2A_CO2FLUX_SO_FY, open('./EXTRACT/UKESM_2A_CO2FLUX_SO_FY_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_2B_CO2FLUX_SO_FY, open('./EXTRACT/UKESM_2B_CO2FLUX_SO_FY_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_3A_CO2FLUX_SO_FY, open('./EXTRACT/UKESM_3A_CO2FLUX_SO_FY_vals_19500-2100.pkl', 'wb'))
pickle.dump(UKESM_3B_CO2FLUX_SO_FY, open('./EXTRACT/UKESM_3B_CO2FLUX_SO_FY_vals_19500-2100.pkl', 'wb'))








