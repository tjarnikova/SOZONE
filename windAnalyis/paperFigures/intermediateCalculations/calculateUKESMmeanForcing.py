import xarray as xr
import glob
import numpy as np

tmesh = xr.open_dataset('/gpfs/data/greenocean/software/resources/regrid/mesh_mask3_6.nc')
tmesh['csize'] = tmesh.tmask[0,0,:,:] * tmesh.e1t[0,:,:] * tmesh.e2t[0,:,:]


#meshmask for nemo3.6

def make_yearlist(yrst, yrend, hist_scen, fut_scen, dtype = 'taux'):
    yrs = np.arange(yrst,yrend+1,1)
    ylist = []
    for i in range(0,len(yrs)):
        y = yrs[i]
        if y < 2015:
             ty = f'/gpfs/data/greenocean/software/resources/windsProcessed/UKESM_{hist_scen}_{dtype}_{y}_daily.nc'
        if y >= 2015:
             ty = f'/gpfs/data/greenocean/software/resources/windsProcessed/UKESM_{fut_scen}_{dtype}_{y}_daily.nc'
        t2 = glob.glob(ty)
        #print(t2)
        ylist.append(t2[0])
    return ylist

def make_yearlist_era(yrst, yrend, dtype = 'taux'):
    yrs = np.arange(yrst,yrend+1,1)
    ylist = []
    for i in range(0,len(yrs)):
        y = yrs[i]
        ty = f'/gpfs/data/greenocean/software/resources/windsProcessed/ERA5_v2023_{dtype}_{y}_daily.nc'
        t2 = glob.glob(ty)
        #print(t2)
        ylist.append(t2[0])
    return ylist

tdir = '/gpfs/data/greenocean/software/resources/windsProcessed/'

# tauy_1A = xr.open_mfdataset(make_yearlist(1940, 2100, '1H', '1FA', dtype = 'tauy'))
yrst = 1940; yren = 2100

# sc = '1A'
# td = xr.open_mfdataset(make_yearlist(yrst, yren, '1H', '1FA', dtype = 'wspd'))
# v = td.wspd.sel(y=slice(0,37)).weighted(tmesh['csize'].sel(y=slice(0,37))).mean(dim = ['x','y'])
# v.name = 'wspd'
# v.attrs["units"] = "m/s"
# v.attrs["desc"] = "area-weighted mean south of -50 (index 37) from calculateUKESMmeanForcing.py"
# v.to_netcdf(f'{tdir}wspd_{sc}_overwatermean-50N.nc')

# sc = '2A'
# td = xr.open_mfdataset(make_yearlist(yrst, yren, '2H', '2FA', dtype = 'wspd'))
# v = td.wspd.sel(y=slice(0,37)).weighted(tmesh['csize'].sel(y=slice(0,37))).mean(dim = ['x','y'])
# v.name = 'wspd'
# v.attrs["units"] = "m/s"
# v.attrs["desc"] = "area-weighted mean south of -50 (index 37) from calculateUKESMmeanForcing.py"
# v.to_netcdf(f'{tdir}wspd_{sc}_overwatermean-50N.nc')

# sc = '3A'
# td = xr.open_mfdataset(make_yearlist(yrst, yren, '3H', '3FA', dtype = 'wspd'))
# v = td.wspd.sel(y=slice(0,37)).weighted(tmesh['csize'].sel(y=slice(0,37))).mean(dim = ['x','y'])
# v.name = 'wspd'
# v.attrs["units"] = "m/s"
# v.attrs["desc"] = "area-weighted mean south of -50 (index 37) from calculateUKESMmeanForcing.py"
# v.to_netcdf(f'{tdir}wspd_{sc}_overwatermean-50N.nc')

# sc = '1B'
# td = xr.open_mfdataset(make_yearlist(yrst, yren, '1H', '1FB', dtype = 'wspd'))
# v = td.wspd.sel(y=slice(0,37)).weighted(tmesh['csize'].sel(y=slice(0,37))).mean(dim = ['x','y'])
# v.name = 'wspd'
# v.attrs["units"] = "m/s"
# v.attrs["desc"] = "area-weighted mean south of -50 (index 37) from calculateUKESMmeanForcing.py"
# v.to_netcdf(f'{tdir}wspd_{sc}_overwatermean-50N.nc')

# sc = '2B'
# td = xr.open_mfdataset(make_yearlist(yrst, yren, '2H', '2FB', dtype = 'wspd'))
# v = td.wspd.sel(y=slice(0,37)).weighted(tmesh['csize'].sel(y=slice(0,37))).mean(dim = ['x','y'])
# v.name = 'wspd'
# v.attrs["units"] = "m/s"
# v.attrs["desc"] = "area-weighted mean south of -50 (index 37) from calculateUKESMmeanForcing.py"
# v.to_netcdf(f'{tdir}wspd_{sc}_overwatermean-50N.nc')

# sc = '3B'
# td = xr.open_mfdataset(make_yearlist(yrst, yren, '3H', '3FB', dtype = 'wspd'))
# v = td.wspd.sel(y=slice(0,37)).weighted(tmesh['csize'].sel(y=slice(0,37))).mean(dim = ['x','y'])
# v.name = 'wspd'
# v.attrs["units"] = "m/s"
# v.attrs["desc"] = "area-weighted mean south of -50 (index 37) from calculateUKESMmeanForcing.py"
# v.to_netcdf(f'{tdir}wspd_{sc}_overwatermean-50N.nc')

sc = '3B'
td = xr.open_mfdataset(make_yearlist_era(1940, 2022,  dtype = 'wspd'))
v = td.wspd.sel(y=slice(0,37)).weighted(tmesh['csize'].sel(y=slice(0,37))).mean(dim = ['x','y'])
v.name = 'wspd'
v.attrs["units"] = "m/s"
v.attrs["desc"] = "area-weighted mean south of -50 (index 37) from calculateUKESMmeanForcing.py"
v.to_netcdf(f'{tdir}wspd_ERA5_v2023_overwatermean-50N.nc')