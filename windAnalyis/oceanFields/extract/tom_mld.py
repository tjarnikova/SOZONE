## test
import numpy as np
import xarray as xr
import pandas as pd
import glob
import gsw


def make_yearlist(yrst, yrend, baseDir):
    yrs = np.arange(yrst,yrend+1,1)
    ylist = []
    for i in range(0,len(yrs)):
        ty = f'{baseDir}/nemo_scen_1A_1m_{yrs[i]}_fy_grid-T.nc'
        ty = f'{baseDir}/ORCA2_1m_{yrs[i]}0101_{yrs[i]}1231_grid_T.nc'
        t2 = glob.glob(ty)
        #print(t2)
        ylist.append(t2[0])
    return ylist

def get_mld(sa,ct,deptht):

    st = gsw.sigma0(sa,ct)
    dens_10m = np.interp(10, deptht[0:2], st[0:2]) #get density at 10m
    dens01 = dens_10m+0.01 #get criterions
    dens03 = dens_10m+0.03

    depth_dens01 = -9999 #default values
    depth_dens03 = -9999
    

    try:

        fb_01 = [np.where(st >= dens01)][0][0]
        fb_01 = fb_01[0]
        depth_dens01 = np.interp(dens01,st[fb_01-1:fb_01+1], deptht[fb_01-1:fb_01+1])
        #
        fb_03 = [np.where(st >= dens03)][0][0]
        fb_03 = fb_03[0]
        depth_dens03 = np.interp(dens03,st[fb_03-1:fb_03+1], deptht[fb_03-1:fb_03+1])
        
        #if it's finding 
        q = (np.where(ct == 0)) ##run out of ocean values
        first0 = (q[0][0])
    
        if fb_01 >= first0:
            depth_dens01 = deptht[first0-1]
        if fb_03 >= first0:
            depth_dens03 = deptht[first0-1]    
    
    except:
        
        pass

    return depth_dens01, depth_dens03


def make_mld_nc(year):
    
    baseDir = '/gpfs/data/greenocean/software/runs/TOM12_TJ_1AA6/'
    w = xr.open_dataset(make_yearlist(year,year,baseDir)[0])
    
    savenam = f'{baseDir}nemo_scen_1A_1m_{year}_calcMLD.nc'
    print(savenam)
    
    times = pd.date_range(f"{year}/01/01",f"{year+1}/01/01",freq='MS',closed='left')

#     mm_med = xr.open_dataset('/gpfs/data/greenocean/software/resources/MEDUSA/mesh_mask_eORCA1_wrk.nc')
#     mm_med['area'] = mm_med.tmask[0,:,:] * mm_med.e1t[:,:] * mm_med.e2t[:,:]

    mm_tom = xr.open_dataset('/gpfs/data/greenocean/software/resources/regrid/mesh_mask3_6.nc')

    MLD_01 = np.zeros([12,149,182])
    MLD_03 = np.zeros([12,149,182])

    deptht = w.deptht.values

    for m in range(0,12):
        print(m)
        for j in range(0,149):
            if j%10 == 0:
                print(j)
            for i in range(0,182):
                
                mask = mm_tom.tmaskutil[0,j,i].values
                if mask == 0:
                    MLD_01[m,j,i] = -9999 
                    MLD_03[m,j,i] = -9999  
                    print(f'land ho! j{j} i{i}')
                else:
                    ct = w.votemper[m,:,j,i].values
                    sa = w.vosaline[m,:,j,i].values
                    depth_dens01, depth_dens03 = get_mld(sa,ct,deptht)
                    MLD_01[m,j,i] = depth_dens01 
                    MLD_03[m,j,i] = depth_dens03 
                    if depth_dens01 == -9999:
                        print(f'not land, but still cant find mld, m{m} j{j} i{i}')   

    data_vars = {'MLD_01':(['time_counter', 'y', 'x'], MLD_01,
    {'units': 'm',
    'long_name':'mld 0.01 sigcrit'}),
                 'MLD_03':(['time_counter', 'y', 'x'], MLD_03,
    {'units': 'm',
    'long_name':'mld 0.03 sigcrit'}),
    }
    # define coordinates
    coords = {'time_counter': (['time_counter'], times),
    'nav_lat': (['y','x'], w.nav_lat),
    'nav_lon': (['y','x'], w.nav_lon),
    }
    # define global attributes
    attrs = {'made in':'/SOZONE/windAnalyis/oceanFields/observational_MLD.ipynb',
    'desc': 'backcalculate okesm mld'
    }
    ds = xr.Dataset(data_vars=data_vars,
    coords=coords,
    attrs=attrs)
    ds.to_netcdf(savenam)
    
for y in range(2001,2007):
    make_mld_nc(y)
