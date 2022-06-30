import numpy as np
import glob
import netCDF4 as nc

def make_yearlist(yrst, yrend, dtype, modnam):
    '''
    open many files together as the same dataset
    ylist = make_yearlist(2001,2011,'diad_T','TOM12_TJ_1AS1')
    ds = xr.open_mfdataset(ylist)
    
    '''
    bD = f'/gpfs/afm/greenocean/software/runs/{modnam}/'
    yrs = np.arange(yrst,yrend+1,1)
    ylist = []
    for i in range(0,len(yrs)):
        ty = f'{bD}/ORCA2_1m_{yrs[i]}0101_{yrs[i]}1231_{dtype}.nc'
        ylist.append(ty)
    return ylist

def make_yearlist_data(yrst, yrend, dtype, modnam):
    '''
    open many files together as the same dataset
    ylist = make_yearlist(2001,2011,'diad_T','TOM12_TJ_1AS1')
    ds = xr.open_mfdataset(ylist)
    
    '''
    bD = f'/gpfs/data/greenocean/software/runs/{modnam}/'
    yrs = np.arange(yrst,yrend+1,1)
    ylist = []
    for i in range(0,len(yrs)):
        ty = f'{bD}/ORCA2_1m_{yrs[i]}0101_{yrs[i]}1231_{dtype}.nc'
        ylist.append(ty)
    return ylist

def extract_model_from_daily_2D(yrstart,yrend,path_to_files,ftype,var):
    '''
    path_to_files = '/gpfs/afm/greenocean/software/runs/TOM12_TJ_1AS1/'
    ftype = 'diad_T'; var = 'Cflx'    
    st = extract_model_from_daily_2D(1950,1951,path_to_files,ftype,var)
    '''
    yrs = np.arange(yrstart,yrend+1,1)
    storar = np.zeros([len(yrs),12,149,182])
    
    tnc = nc.Dataset('/gpfs/data/greenocean/software/resources/regrid/mesh_mask3_6.nc')
    tmask = (tnc['tmask'][:,0,:,:])
    tmask_12m = np.zeros([12,149,182])
    
    for i in range(0,12):
        tmask_12m[i,:,:] = tmask
   
    for i in range(0,len(yrs)):
        yr = yrs[i]
        fnam = f'/ORCA*{yr}0101*{ftype}*.nc'
        w = glob.glob(f'{path_to_files}{fnam}')

        try:
            w2 = nc.Dataset(w[0])
            tvar = w2[var][:]

            tvar[tmask_12m ==0] = np.nan
            storar[i,:,:,:] = tvar
        except:
            storar[i,:,:,:] = np.nan
            
    return storar

def extract_model_from_daily_3D(yrstart,yrend,path_to_files,ftype,var):
    '''
    path_to_files = '/gpfs/afm/greenocean/software/runs/TOM12_TJ_1AS1/'
    ftype = 'diad_T'; var = 'Cflx'    
    st = extract_model_from_daily_3D(1950,1951,path_to_files,ftype,var)
    '''
    tnc = nc.Dataset('/gpfs/data/greenocean/software/resources/regrid/mesh_mask3_6.nc')
    tmask = (tnc['tmask'][:])
    tmask_12m = np.zeros([12,31,149,182])
    for i in range(0,12):
        tmask_12m[i,:,:,:] = tmask
    
    yrs = np.arange(yrstart,yrend+1,1)
    storar = np.zeros([len(yrs),12,31,149,182])
    for i in range(0,len(yrs)):
        yr = yrs[i]
        fnam = f'/ORCA*{yr}0101*{ftype}*.nc'
        w = glob.glob(f'{path_to_files}{fnam}')
        try:
            w2 = nc.Dataset(w[0])
            tvar = w2[var][:]
            tvar[tmask_12m ==0] = np.nan
            storar[i,:,:,:,:] = tvar
        except:
            storar[i,:,:,:,:] = np.nan
            
    return storar

def check_for_nans(yrstart,yrend,path_to_files,ftype,var):
    '''
    path_to_files = '/gpfs/afm/greenocean/software/runs/TOM12_TJ_1AS1/'
    ftype = 'diad_T'; var = 'Cflx'    
    st = extract_model_from_daily_3D(1950,1951,path_to_files,ftype,var)
    indarray = 0 means everything is fine, 1 means there's nans, 2 means doesn't exist
    '''

    yrs = np.arange(yrstart,yrend+1,1)
    indarray = np.zeros(len(yrs))
    list_of_nanyears = []
    for i in range(0,len(yrs)):
        yr = yrs[i]
        fnam = f'/ORCA*{yr}0101*{ftype}*.nc'
        w = glob.glob(f'{path_to_files}{fnam}')
        try:
            w2 = nc.Dataset(w[0])
            s = w2[var][:]
            q = (np.where(np.isnan(s)))
            if (np.size(q) == 0):
                indarray[i] = 0
            else:
                indarray[i] = 1
                list_of_nanyears.append(yr)
        except:
            indarray[i] = 2
            
    return indarray, list_of_nanyears