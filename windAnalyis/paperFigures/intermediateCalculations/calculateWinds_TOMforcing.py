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
             ty = f'/gpfs/data/greenocean/software/resources/winds_gooddates/UKESM_scen_{hist_scen}_{dtype}_{y}_daily.nc'
        if y >= 2015:
             ty = f'/gpfs/data/greenocean/software/resources/winds_gooddates/UKESM_scen_{fut_scen}_{dtype}_{y}_daily.nc'
        t2 = glob.glob(ty)
        #print(t2)
        ylist.append(t2[0])
    return ylist

tdir = '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/paperFigures/intermediateCalculations/'

# tauy_1A = xr.open_mfdataset(make_yearlist(1940, 2100, '1H', '1FA', dtype = 'tauy'))
yrst = 1940; yren = 2100

sc = '1A'
td = xr.open_mfdataset(make_yearlist(yrst, yren, '1H', '1FA', dtype = 'wspd'))
v = td.wspd.sel(y=slice(0,50)).weighted(tmesh['csize'].sel(y=slice(0,50))).mean(dim = ['x','y'])
v.name = 'wspd'
v.attrs["units"] = "m/s"
v.attrs["desc"] = "area-weighted mean south of -30 (index 50) from tom forcing"
v.to_netcdf(f'{tdir}wspd_{sc}.nc')

sc = '2A'
td = xr.open_mfdataset(make_yearlist(yrst, yren, '2H', '2FA', dtype = 'wspd'))
v = td.wspd.sel(y=slice(0,50)).weighted(tmesh['csize'].sel(y=slice(0,50))).mean(dim = ['x','y'])
v.name = 'wspd'
v.attrs["units"] = "m/s"
v.attrs["desc"] = "area-weighted mean south of -30 (index 50) from tom forcing"
v.to_netcdf(f'{tdir}wspd_{sc}.nc')

sc = '3A'
td = xr.open_mfdataset(make_yearlist(yrst, yren, '3H', '3FA', dtype = 'wspd'))
v = td.wspd.sel(y=slice(0,50)).weighted(tmesh['csize'].sel(y=slice(0,50))).mean(dim = ['x','y'])
v.name = 'wspd'
v.attrs["units"] = "m/s"
v.attrs["desc"] = "area-weighted mean south of -30 (index 50) from tom forcing"
v.to_netcdf(f'{tdir}wspd_{sc}.nc')

sc = '1B'
td = xr.open_mfdataset(make_yearlist(yrst, yren, '1H', '1FB', dtype = 'wspd'))
v = td.wspd.sel(y=slice(0,50)).weighted(tmesh['csize'].sel(y=slice(0,50))).mean(dim = ['x','y'])
v.name = 'wspd'
v.attrs["units"] = "m/s"
v.attrs["desc"] = "area-weighted mean south of -30 (index 50) from tom forcing"
v.to_netcdf(f'{tdir}wspd_{sc}.nc')

sc = '2B'
td = xr.open_mfdataset(make_yearlist(yrst, yren, '2H', '2FB', dtype = 'wspd'))
v = td.wspd.sel(y=slice(0,50)).weighted(tmesh['csize'].sel(y=slice(0,50))).mean(dim = ['x','y'])
v.name = 'wspd'
v.attrs["units"] = "m/s"
v.attrs["desc"] = "area-weighted mean south of -30 (index 50) from tom forcing"
v.to_netcdf(f'{tdir}wspd_{sc}.nc')

sc = '3B'
td = xr.open_mfdataset(make_yearlist(yrst, yren, '3H', '3FB', dtype = 'wspd'))
v = td.wspd.sel(y=slice(0,50)).weighted(tmesh['csize'].sel(y=slice(0,50))).mean(dim = ['x','y'])
v.name = 'wspd'
v.attrs["units"] = "m/s"
v.attrs["desc"] = "area-weighted mean south of -30 (index 50) from tom forcing"
v.to_netcdf(f'{tdir}wspd_{sc}.nc')