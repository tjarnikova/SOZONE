import numpy as np
import netCDF4 as nc

# monthly wind forcing for the southern ocean
#open a landmask file and get a 365 day tmask

mask = nc.Dataset('simple_landmask.nc')
tmask = mask['mask'][:]
tmask_broad = np.zeros([365, 149, 182])
for i in range(0,365):
    tmask_broad[i,:,:] = tmask
#cut it down to SO size
tmask_broad_SO = tmask_broad[:,0:37,:]

#years for which to do this averaging process
dr = np.arange(1948,2021,1)
sz = len(dr)

#starts and ends of months
mo_st = np.array([1,32,60,91,121,152,182,213,244,274,305,335])
mo_st = mo_st - 1
mo_en = np.array([31,59,90,120,151,181,212,243,273,304,334,365])

for y in range(0,sz):
    
    tyear = dr[y]
    print(tyear)
    tdir = '/gpfs/data/greenocean/software/products/NCEPForcingData/'
    tfil = f'ncep_bulk_{tyear}.nc'
    MO = nc.Dataset(f'{tdir}{tfil}')
 
    wspd10m = MO['wspd'][0:365,0:37,:]
    
    wspd10m[tmask_broad_SO == 1] = np.nan
    
    wspd10m_MON = np.zeros([12,37,182])
    
    for m in range(0,12):
        # uwind10m_MON[m,:,:] = np.nanmean(uwind10m[mo_st[m]:mo_en[m],:,:],axis = 0)
        # vwind10m_MON[m,:,:] = np.nanmean(vwind10m[mo_st[m]:mo_en[m],:,:],axis = 0)
        wspd10m_MON[m,:,:] = np.nanmean(wspd10m[mo_st[m]:mo_en[m],:,:],axis = 0)
        
    outdir = '../averaged_forcing/NCEP/'
    outfil = f'{outdir}NCEP_MONTHLY_SO_wind{tyear}.nc'
    
    ds = nc.Dataset(outfil, 'w', format='NETCDF4')
    ds.description = 'monthly averaged windspeed,south of 50deg. monthly wspd avgd. from daily. days 0-365 of each yr, no leap year treatment'
    day = ds.createDimension('month',12)
    x = ds.createDimension('x',182)
    y = ds.createDimension('y',37)
    # uw = ds.createVariable('uwind10m', 'f4', ('month','y','x'))
    # uw[:] = uwind10m_MON
    # vw = ds.createVariable('vwind10m', 'f4', ('month','y','x'))
    # vw[:] = vwind10m_MON
    uw = ds.createVariable('wspd10m', 'f4', ('month','y','x'))
    uw[:] = wspd10m_MON    
    ds.close()
    
