import numpy as np
import xarray as xr 
import matplotlib.pyplot as plt
from cmocean import cm
import cartopy as cp
import cartopy.crs as ccrs
import matplotlib.path as mpath
import cartopy.feature as cfeature

tdir = '/gpfs/data/greenocean/software/resources/windsProcessed/'

## regridding steps to make the starting nc:
# 0 ) SOZONE/windAnalyis/paperFigures/runnerMakeWspd.py
# 1) /gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/paperFigures/runnerLatLonsForRegrid.py
# 2) cdo remapbil,r360x180 /gpfs/data/greenocean/software/resources/windsProcessed/UKESM_1FA_wspd_2017_4regrid.nc
# 3) SOZONE/windAnalyis/paperFigures/runnerMakeClimatologyWspd.py


ukesm_clim = 'UKESM_1H_wspd_clim_1940-2020_regrid.nc'
era5_clim = 'ERA5_wspd_clim_1940-2020_regrid.nc'

ukesm_winds = xr.open_dataset(f'{tdir}/{ukesm_clim}')
era5_winds = xr.open_dataset(f'{tdir}/{era5_clim}')

spbot = 4; sptop = 12; spint = 2
difbot = -2; diftop = 2.1; difint = 1
tcm = 'Spectral_r'

lats = era5_winds.lat
lons = era5_winds.lon

#### plot southern!
def plot_southern(fig, ax1, lons, lats, tdat, tvmin, 
                  tvmax, tticks, fs = 12, 
                  tit = '', cbarlab = '', tcmap = 'viridis', lm = True, cbr = True):
   
    ax1.set_extent([-180, 180, -80, -28], ccrs.PlateCarree())
    #make that circle
    theta = np.linspace(0, 2*np.pi, 100)
    center, radius = [0.5, 0.5], 0.5
    verts = np.vstack([np.sin(theta), np.cos(theta)]).T
    circle = mpath.Path(verts * radius + center)
    ax1.set_boundary(circle, transform=ax1.transAxes)
    # lons = nav_lon[0:50,:]; lats = nav_lat[0:50,:]; 
    mesh = ax1.pcolormesh(lons, lats, tdat, cmap = tcmap, vmin = tvmin, vmax = tvmax, 
                     transform=ccrs.PlateCarree())
    
    ax1.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '110m', 
                                                 edgecolor='face', facecolor='k'))

    ax1.set_title(tit, fontsize = fs)
    cb = 0
    if cbr:
        cb = fig.colorbar(mesh, ax = ax1, orientation = 'horizontal',
                     pad = 0.06, fraction = 0.045, shrink = 0.9)
        cb.set_label(label=cbarlab,fontsize = 8)
        cb.set_ticks(tticks, fontsize = 80)
        cb.ax.tick_params(labelsize=8)
    return cb

fact = 1
fig = plt.figure(figsize=[8*fact, 10*fact])


tits = ['ERA5 full year', 'UKESM full year', 'ERA5-UKESM',
       'ERA5 DJF', 'UKESM DJF', 'ERA5-UKESM DJF','ERA5 MAM', 'UKESM MAM', 'ERA5-UKESM MAM',\
        'ERA5 JJA', 'UKESM JJA', 'ERA5-UKESM JJA','ERA5 SON', 'UKESM SON', 'ERA5-UKESM SON']

toplot = [era5_winds.wspd[0,:,:].values, ukesm_winds.wspd[0,:,:].values,\
          era5_winds.wspd[0,:,:].values -ukesm_winds.wspd[0,:,:].values,\
          era5_winds.wspd[1,:,:].values, ukesm_winds.wspd[1,:,:].values,\
          era5_winds.wspd[1,:,:].values -ukesm_winds.wspd[1,:,:].values,\
          era5_winds.wspd[2,:,:].values, ukesm_winds.wspd[2,:,:].values,\
          era5_winds.wspd[2,:,:].values -ukesm_winds.wspd[2,:,:].values,\
          era5_winds.wspd[3,:,:].values, ukesm_winds.wspd[3,:,:].values,\
          era5_winds.wspd[3,:,:].values -ukesm_winds.wspd[3,:,:].values,\
          era5_winds.wspd[4,:,:].values, ukesm_winds.wspd[4,:,:].values,\
          era5_winds.wspd[4,:,:].values -ukesm_winds.wspd[4,:,:].values,\
         ]
      
cms = [tcm, tcm, cm.balance, tcm, tcm, cm.balance, tcm, tcm, cm.balance, tcm, tcm, cm.balance, tcm, tcm, cm.balance]
bb = [spbot, spbot, difbot,spbot, spbot, difbot,spbot, spbot, difbot,spbot, spbot, difbot, spbot, spbot, difbot]
tb = [sptop, sptop, diftop,sptop, sptop, diftop,sptop, sptop, diftop,sptop, sptop, diftop, sptop, sptop, diftop]
intvl = [spint, spint, difint,spint, spint, difint,spint, spint, difint,spint, spint, difint,spint, spint, difint]
#test = seasmean_map_ts_ukesm[0,0,:,:]


for i in range(0,15):
    test = toplot[i]
    botbound = bb[i]
    topbound = tb[i]
    tint = intvl[i]
    if i < 3:
        tcbr = True
    else:
        tcbr = False
    ax1 = fig.add_subplot(5, 3, i+1, projection=ccrs.Orthographic(0, -90))
    bc = plot_southern(fig, ax1, lons, lats, test, botbound, 
                  topbound, np.arange(botbound,topbound,tint), fs = 12, 
                  tit = tits[i], cbarlab = 'm/s', tcmap = cms[i], lm = True, cbr = tcbr)
    
# plt.suptitle('seasonal wind speed climatology, 1950-2020', y = 0.90)
plt.tight_layout()
fig.savefig('./figs/Fig_climatologymap_UKESM_ERA_1940-2020.jpg', dpi = 300)

print('complete figure render')