import matplotlib.pyplot as plt
import netCDF4 as nc
import numpy as np
import glob
import warnings
import sys
warnings.filterwarnings('ignore')

'''
script for plotting surface variables

usage:
(standard modules must be loaded)
python test.py modname yearstart yearend filetype varname

filetype is one of grid_T, grid_T, ptrc_T, icemod, and grid_V
(varname must be in the filetype you chose)

creates plots in a directory called PLOTS (subdirectory of directory where this .py file is)

TJSJ 2022 (T.Jarnikova@uea.ac.uk) 
'''
modname = sys.argv[1]
yearstart = int(sys.argv[2])
yearend = int(sys.argv[3])
ncstr = sys.argv[4]
var = sys.argv[5]
depthind = int(sys.argv[6])

print(f'Plotting for run {modname}, years {yearstart}-{yearend}')
print(f'variable {var} (in filepattern {ncstr})')
print(f'depth level {depthind}')

#we assume that model output is in this directory tree
baseDir = '/gpfs/data/greenocean/software/runs/'


#access first file in timeseries, get out units 
w = glob.glob(f'{baseDir}{modname}/*{yearstart}*{ncstr}.nc')
ncnam = (w[0])
tnc = nc.Dataset(ncnam)
longname = tnc[var].long_name
units = tnc[var].units

### access depth 
tnc = nc.Dataset('/gpfs/data/greenocean/software/resources/regrid/mesh_mask3_6.nc')
tdepths = (tnc['gdept_1d'][0,:])
t_depth = tdepths[depthind]
#prepare array of years to loop through, and storage arrays for output
# and for max and min for plotting
yrs = np.arange(yearstart,yearend+1,1)
noyrs = len(yrs)

summer_stor = np.zeros([noyrs,149,182])
winter_stor = np.zeros([noyrs,149,182])
allyear_stor = np.zeros([noyrs,149,182])

plt_min = 0; plt_max = 0

for y in range(0,noyrs):
    
    ts_index = 0
    yr = yrs[y]
    #find relevant nc using wildcards and the glob package
    w = glob.glob(f'{baseDir}{modname}/*{yr}*{ncstr}.nc')
    ncnam = (w[0])
    
    #open dataset and extract relevant variable 
    tnc = nc.Dataset(ncnam)
    tvar0 = tnc[var][:]
    ## if array is 4 dimensional (Time, depth, y, x), slice to get relevant depth
    #else it should be 3dimensional and you just take whole array
    if (tvar0.ndim == 4):
        tvar = tvar0[:,depthind,:,:]
    else:
        tvar = tvar0[:]
    #set up some rough mins, maxs for for colourbar  
    tvar[tvar == 0] = np.nan
    #get out summer, ie months december, jan, feb, and average accross months
    this_summer = np.zeros([3,149,182])
    this_summer[0,:,:] = tvar[11,:,:]
    this_summer[1:3,:,:] = tvar[0:2,:,:]
    ## average accross the 3 months and put into storage array
    summer_stor[y,:,:] = np.nanmean(this_summer,axis = 0)
    #winter is months 6-8, so python indices 5-8 (8 isn't counted in python indexing here)
    winter_stor[y,:,:] = np.nanmean(tvar[5:8,:,:],axis = 0)
    allyear_stor[y,:,:] = np.nanmean(tvar[:,:,:],axis = 0)
    
## average out the stored arrays
winter_stor_mn = np.nanmean(winter_stor,axis =0)
summer_stor_mn = np.nanmean(summer_stor,axis =0)
allyear_stor_mn = np.nanmean(allyear_stor,axis =0)
plt_min = 0.8*np.nanmean(allyear_stor_mn)
plt_max = 1.2*np.nanmean(allyear_stor_mn)
# get only the SO
winter_stor_mn_SO = winter_stor_mn[0:50,:]
summer_stor_mn_SO = summer_stor_mn[0:50,:]
allyear_stor_mn_SO = allyear_stor_mn[0:50,:]
plt_min_SO = 0.9*np.nanmean(allyear_stor_mn_SO)
plt_max_SO = 1.1*np.nanmean(allyear_stor_mn_SO)

to_plt = [allyear_stor_mn, summer_stor_mn, winter_stor_mn,\
         allyear_stor_mn_SO, summer_stor_mn_SO, winter_stor_mn_SO]
seas = ['full year', 'austral summer (months 12-2)', 'austral winter (months 6-8)',\
       'full year', 'austral summer (months 12-2)', 'austral winter (months 6-8)',]
fact = 0.7
fig, axs = plt.subplots(2,3, figsize=(20*fact, 14*fact), facecolor='w', edgecolor='k')
axs = axs.ravel()
for i in range(0,3):
    pltmesh = axs[i].pcolormesh(to_plt[i], cmap = 'viridis', vmin = plt_min, vmax = plt_max)
    fig.colorbar(pltmesh, ax=axs[i], orientation = 'horizontal', label = units)
    axs[i].set_yticks([]); axs[i].set_xticks([]);
    axs[i].set_title(f'{seas[i]}\n Global')
    
for i in range(3,6):
    pltmesh = axs[i].pcolormesh(to_plt[i], cmap = 'viridis', vmin = plt_min_SO, vmax = plt_max_SO)
    fig.colorbar(pltmesh, ax=axs[i], orientation = 'horizontal', label = units)
    axs[i].set_yticks([]); axs[i].set_xticks([]);
    axs[i].set_title(f'{seas[i]}\n Southern Ocean (south of -30$^\circ$S)')

plt.suptitle(f'Mean {modname} {longname}\n years {yearstart}-{yearend}, depth level {depthind} ({int(t_depth)}m)')
fig.savefig(f'{modname}_{var}_{yearstart}-{yearend}_level_{depthind}.jpg')