import numpy as np
import netCDF4 as nc

# monthly wind forcing for the southern ocean
#open a landmask file and get a 365 day tmask

mask = nc.Dataset('../../UTILS/simple_landmask.nc')
tmask = mask['mask'][:]
tmask_broad = np.zeros([365, 149, 182])
for i in range(0,365):
    tmask_broad[i,:,:] = tmask
#cut it down to SO size
tmask_broad_SO = tmask_broad[:,0:37,:]

#years for which to do this averaging process
dr = np.arange(1950,2021,1)
sz = len(dr)

#starts and ends of months
mo_st = np.array([1,32,60,91,121,152,182,213,244,274,305,335])
mo_st = mo_st - 1
mo_en = np.array([31,59,90,120,151,181,212,243,273,304,334,365])

for y in range(0,sz):
    
    tyear = dr[y]
    print(tyear)
    tdir = '/gpfs/data/greenocean/software/products/ERA5Forcing/daily/'

    tfil = f'tauy_1d_{tyear}_daily.nc'
    MO = nc.Dataset(f'{tdir}{tfil}')
    vwind10m = MO['vflx'][0:365,0:37,:]
    
    tfil = f'taux_1d_{tyear}_daily.nc'
    MO = nc.Dataset(f'{tdir}{tfil}')
    uwind10m = MO['uflx'][0:365,0:37,:]
    
    wspd10m = np.sqrt(uwind10m**2+vwind10m**2) 
    
    #nans over land
    uwind10m[tmask_broad_SO == 1] = np.nan
    vwind10m[tmask_broad_SO == 1] = np.nan
    wspd10m[tmask_broad_SO == 1] = np.nan
    
    #arrays for monthly vars
    uwind10m_MON = np.zeros([12,37,182])
    vwind10m_MON = np.zeros([12,37,182])
    wspd10m_MON = np.zeros([12,37,182])
    
    for m in range(0,12):
        uwind10m_MON[m,:,:] = np.nanmean(uwind10m[mo_st[m]:mo_en[m],:,:],axis = 0)
        vwind10m_MON[m,:,:] = np.nanmean(vwind10m[mo_st[m]:mo_en[m],:,:],axis = 0)
        wspd10m_MON[m,:,:] = np.nanmean(wspd10m[mo_st[m]:mo_en[m],:,:],axis = 0)
        
    outdir = '../averaged_forcing/ERA5/'
    outfil = f'{outdir}ERA5_MONTHLY_SO_wind{tyear}.nc'
    
    ds = nc.Dataset(outfil, 'w', format='NETCDF4')
    ds.description = 'monthly averaged uwind,vwind,windspeed,south of 50deg. daily wspd is calculated from daily averages of velocities, and monthly wspd avgd. from daily '
    day = ds.createDimension('month',12)
    x = ds.createDimension('x',182)
    y = ds.createDimension('y',37)
    uw = ds.createVariable('uwind10m', 'f4', ('month','y','x'))
    uw[:] = uwind10m_MON
    vw = ds.createVariable('vwind10m', 'f4', ('month','y','x'))
    vw[:] = vwind10m_MON
    uw = ds.createVariable('wspd10m', 'f4', ('month','y','x'))
    uw[:] = wspd10m_MON    
    ds.close()
    
