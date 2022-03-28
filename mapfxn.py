
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.path as mpath


def plot_southern(fig, ax1, lons, lats, tdat, tvmin, 
                  tvmax, northex = -50, fs = 12,
                  tit = '', cbarlab = '', tcmap = 'viridis', lm = True):
   '''
   fxnal usage:
        tfig = plt.figure(figsize=[28*fact, 17*fact])
        ax1 = tfig.add_subplot(3, 8, 1, projection=ccrs.Orthographic(0, -90))
        tdat = NCEP_austral_summer_clim
        plot_southern(tfig, ax1, lons, lats, tdat, tvmin, 
                          tvmax, northex = -50, fs = 12,
                          tit = 'NCEP summer wspd clim. \n (1950-2020)', 
                      cbarlab = 'wspd m s$^-1$', tcmap = 'viridis', lm = True)
   '''
    ax1.set_extent([-180, 180, -80, -45], ccrs.PlateCarree())
    #make that circle
    theta = np.linspace(0, 2*np.pi, 100)
    center, radius = [0.5, 0.5], 0.5
    verts = np.vstack([np.sin(theta), np.cos(theta)]).T
    circle = mpath.Path(verts * radius + center)
    ax1.set_boundary(circle, transform=ax1.transAxes)
    lons = nav_lon[0:37,:]; lats = nav_lat[0:37,:]; 
    mesh = ax1.pcolormesh(lons, lats, tdat, cmap = tcmap, vmin = tvmin, vmax = tvmax,
                     transform=ccrs.PlateCarree())
    ax1.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '110m', 
                                                 edgecolor='face', facecolor='oldlace'))
    ax1.set_title(tit, fontsize = fs)
    cb = fig.colorbar(mesh, ax = ax1, orientation = 'horizontal',
                 pad = 0.06, fraction = 0.045, shrink = 0.9)
    cb.set_label(label=cbarlab,fontsize = fs-2)
    
    
# def plot_southern(fig, ax1, lons, lats, tdat, tvmin, 
#                   tvmax, intvl, northex = -50, fs = 12, tit = '', cbarlab = '', tcmap = 'viridis', lm = True):
    
#     '''standard plotting code for a southern ocean quantity 
#     non-default args:
#     fig = the figure
#     ax1 = the axis
#     lons, lats, tdat, tvmin, tvmax, 
#     intvl is interval for the contours
#     default args:
#     northex is the northern extent of the graph
#     fs is fontsize, tit is title (default to none), 
#     cbarlab is colorbarlabel (default to none)
#     tcmap is colormap, default to viridis
#     '''
    
    
#     ax1.set_extent([-180, 180, -80, northex], ccrs.PlateCarree())
    
#     #make that circle
#     theta = np.linspace(0, 2*np.pi, 100)
#     center, radius = [0.5, 0.5], 0.5
#     verts = np.vstack([np.sin(theta), np.cos(theta)]).T
#     circle = mpath.Path(verts * radius + center)
#     ax1.set_boundary(circle, transform=ax1.transAxes)
    
#     #plot data according to given levels
#     tlev = np.arange(tvmin,tvmax+intvl,intvl)
#     mesh = ax1.pcolormesh(lons, lats, tdat, cmap = tcmap, vmin = tvmin, vmax = tvmax,
#                  transform=ccrs.PlateCarree())
    
#     if lm:
#         ax1.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '110m', 
#                                                      edgecolor='face', facecolor='oldlace'))
#     ax1.set_title(tit, fontsize = fs)
#     cb = fig.colorbar(mesh, ax = ax1, orientation = 'horizontal',
#                  pad = 0.06, fraction = 0.045, shrink = 0.9)
#     cb.set_label(label=cbarlab,fontsize = fs-2)
    
#     plt.show()
