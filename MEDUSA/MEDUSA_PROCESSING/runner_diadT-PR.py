
import numpy as np
import xarray as xr
import glob
import pandas as pd

def make_yearly_subset(yr,runname, dtype = 'diad-T', tdir = 'ukesm_allscen_diadT_PR_strag'):

    #what is new file going to be called:
    savenam = f'/gpfs/data/greenocean/software/resources/MEDUSA/PROC2/medusa_{runname}_1y_{yr}_diad-T-PR.nc'
    print(savenam)
    
    #get by-month dimension for this year:
    times = pd.date_range(f"{yr}/01/01",f"{yr+1}/01/01",freq='M',closed='left')
    #get the spatial dimensions from a variable


    #get the files we are converting
    td = f'/gpfs/data/greenocean/software/resources/MEDUSA/{tdir}/*_{runname}*_1m_{yr}*01-*{dtype}.nc'
    fils = glob.glob(td)
    fils.sort()
    
    if len(fils) != 12:
        print(f'missing files for year {yr} in {runname}: we have {len(fils)}')
        return

    else:
        ## define variables that we are saving
        
        q = xr.open_dataset(fils[0])
        nav_lat = q['nav_lat'].values
        nav_lon = q['nav_lon'].values

        
        PRD = np.zeros([12,332,362])
        PRN = np.zeros([12,332,362])

        
        for i in range(0,12):
            tfil = xr.open_dataset(fils[i])
            PRD[i,:,:] = tfil['PRD'][:,:].values
            PRN[i,:,:] = tfil['PRN'][:,:].values


        # define data with variable attributes
        data_vars = {'PRD':(['time_counter','y', 'x'], PRD,
                                 {'units': '',
                                  'long_name':' '}),
                    'PRN':(['time_counter','y', 'x'], PRN,
                                 {'units': ' ',
                                  'long_name':' '}),
       
                    }

        # define coordinates
        coords = {'time_counter': (['time_counter'], times),
            'nav_lat': (['y','x'], nav_lat),
            'nav_lon': (['y','x'], nav_lon),
            }

        # define global attributes
        attrs = {'made in':'SOZONE/MEDUSA/MEDUSA_PROCESSING/runner_diadT-PR.py',
                'desc': 'yearly medusa files, saving only variables of interest'
                }

        ds = xr.Dataset(data_vars=data_vars,
                        coords=coords,
                        attrs=attrs)

        try:
            ## lol compression that we found off the internet? maybe?
            # https://stackoverflow.com/questions/40766037/specify-encoding-compression-for-many-variables-in-xarray-dataset-when-write-to
            comp = dict(zlib=True, complevel=5)
            encoding = {var: comp for var in ds.data_vars}
            ds.to_netcdf(savenam, encoding=encoding)

        except:
            print(f'seems like {savenam} exists already')
    
#make_yearly_subset_nc(1954,'cj198')

#make_yearly_subset_nc(1954,'cj198')
#1h
# runname = 'bc370'
# yrs = np.arange(1950,2015,1)
# for y in yrs:
#     make_yearly_subset(y,runname)    

#1a
runname = 'be682'
yrs = np.arange(2053,2054,1)
for y in yrs:
    make_yearly_subset(y,runname)

# #1b
# runname = 'ce417'
# yrs = np.arange(2015,2100,1)
# for y in yrs:
#     make_yearly_subset(y,runname)

# #2h
# runname = 'cj198'
# yrs = np.arange(1950,2015,1)
# for y in yrs:
#     make_yearly_subset(y,runname)    

# #2a
# runname = 'cj880'
# yrs = np.arange(2015,2100,1)
# for y in yrs:
#     make_yearly_subset(y,runname)
    
# #2b
# runname = 'cj881'
# yrs = np.arange(2015,2100,1)
# for y in yrs:
#     make_yearly_subset(y,runname)
    
    
# #3h
# runname = 'cj200'
# yrs = np.arange(1990,2015,1)
# for y in yrs:
#     make_yearly_subset(y,runname)    
    
# #3a
# runname = 'cj484'
# yrs = np.arange(2015,2100,1)
# for y in yrs:
#     make_yearly_subset(y,runname)    
    
# #3a
# runname = 'cj504'
# yrs = np.arange(2015,2100,1)
# for y in yrs:
#     make_yearly_subset(y,runname)   