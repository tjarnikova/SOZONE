import numpy as np
from cmocean import cm
import cartopy as cp
import cartopy.crs as ccrs
import netCDF4 as nc
import matplotlib.pyplot as plt
import xarray as xr

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

def plot_southern(fig, ax1, lons, lats, tdat, setlim = False, tvmin = 0, 
                  tvmax = 1, tticks = [0,1], northex = -50, fs = 12, 
                  tit = '', cbarlab = '', tcmap = 'viridis', lm = True, cbr = True):
   
    ax1.set_extent([-180, 180, -80, northex], ccrs.PlateCarree())
    #make that circle
    theta = np.linspace(0, 2*np.pi, 100)
    center, radius = [0.5, 0.5], 0.5
    verts = np.vstack([np.sin(theta), np.cos(theta)]).T
    circle = mpath.Path(verts * radius + center)
    ax1.set_boundary(circle, transform=ax1.transAxes)
    # lons = nav_lon[0:50,:]; lats = nav_lat[0:50,:]; 
    if setlim:
        mesh = ax1.pcolormesh(lons, lats, tdat, cmap = tcmap, vmin = tvmin, vmax = tvmax, 
                        transform=ccrs.PlateCarree())
    else:
        mesh = ax1.pcolormesh(lons, lats, tdat, cmap = tcmap,
                transform=ccrs.PlateCarree())
    ax1.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '110m', 
                                                 edgecolor='face', facecolor='k'))
    ax1.set_title(tit, fontsize = fs)
    cb = 0
    if cbr:
        cb = fig.colorbar(mesh, ax = ax1, orientation = 'horizontal',
                     pad = 0.06, fraction = 0.045, shrink = 0.9)
        cb.set_label(label=cbarlab,fontsize = 10)
        if setlim:
            cb.set_ticks(tticks, fontsize = 105)
            cb.ax.tick_params(labelsize=10)
    return cb

def make_yearlist_tom(yrst, yrend, dtype, tr, baseDir = '/gpfs/data/greenocean/software/runs'):
    yrs = np.arange(yrst,yrend+1,1)
    ylist = []
    for i in range(0,len(yrs)):
        ty = f'{baseDir}/{tr}/ORCA2_1m_{yrs[i]}*{dtype}*.nc'\
        
        t2 = glob.glob(ty)
        #print(t2)
        ylist.append(t2[0])
    return ylist    

def make_yearlist(yrst, yrend, rname = 'bc370', ftype = 'diad-T-aux'):
    yrs = np.arange(yrst,yrend+1,1)
    ylist = []
    for i in range(0,len(yrs)):
        ty = f'/gpfs/data/greenocean/software/resources/MEDUSA/PROC2/medusa_{rname}_1y_{yrs[i]}*{ftype}*.nc'

        t2 = glob.glob(ty)
        #print(t2)
        ylist.append(t2[0])
    return ylist

def plot_var(tomvar, ukvar, suptit, tvmin, tvmax, tticks, fact2 = 1, tcm = cm.balance, cbarlab = '', fname = ''):

    lons = tmesh['nav_lon'][0:50,:].values
    lats = tmesh['nav_lat'][0:50,:].values
    fact = 0.4
    tfig = plt.figure(figsize=[52*fact, 12*fact])

    ax1 = tfig.add_subplot(2, 13, 1, projection=ccrs.Orthographic(0, -90))
    tv = tomvar.groupby('time_counter.year').mean().sel(y=slice(0,50)).mean(dim = 'year')*fact2
    plot_southern(tfig, ax1, lons, lats, tv, tvmin, 
              tvmax, tticks, northex = -25, fs = 12, 
              tit = f'TOM, FY', cbarlab = cbarlab, tcmap = tcm, lm = True, cbr = True)

    for i in range(1,13):
        ax1 = tfig.add_subplot(2, 13, i+1, projection=ccrs.Orthographic(0, -90))
        tv = tomvar.groupby('time_counter.month').mean().sel(y=slice(0,50)).sel(month = i)*fact2


        plot_southern(tfig, ax1, lons, lats, tv, tvmin, 
                      tvmax, tticks, northex = -25, fs = 12, 
                      tit = f'm.{i}', cbarlab = '', tcmap = tcm, lm = True, cbr = True)

    ax1 = tfig.add_subplot(2, 13, 1+13, projection=ccrs.Orthographic(0, -90))

    tv = ukvar.groupby('time_counter.year').mean().sel(y=slice(0,140)).mean(dim = 'year')

    lons = ukmesh['nav_lon'][0:140,:].values
    lats = ukmesh['nav_lat'][0:140,:].values

    plot_southern(tfig, ax1, lons, lats, tv, tvmin, 
              tvmax, tticks, northex = -25, fs = 12, 
              tit = f'UKESM, FY', cbarlab = cbarlab, tcmap = tcm, lm = True, cbr = True)

    for i in range(1,13):
        tv = ukvar.groupby('time_counter.month').mean().sel(y=slice(0,140)).sel(month = i)

        ax1 = tfig.add_subplot(2, 13, i+14, projection=ccrs.Orthographic(0, -90))

        plot_southern(tfig, ax1, lons, lats, tv, tvmin, 
                      tvmax, tticks, northex = -25, fs = 12, 
                      tit = f'm.{i}', cbarlab = '', tcmap = tcm, lm = True, cbr = True)

    
    plt.suptitle(suptit)
    plt.tight_layout()
    tfig.savefig(f'./FIGS/{fname}')
