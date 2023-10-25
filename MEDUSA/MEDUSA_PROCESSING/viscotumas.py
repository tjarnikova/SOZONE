import glob
import numpy as np
import xarray as xr

def check_filetype_present(tdir, yr,runname,rtype):

    savenam = f'/gpfs/data/greenocean/software/resources/MEDUSA/{tdir}/*_{runname}*1m_{yr}*{rtype}*nc'

    tw = glob.glob(savenam)
    #print(tw)
    ### need 12 monthly files
    if len(tw) != 12:
        print(f'{yr}, {runname} {rtype} missing')
    else:
        pass
    
def check_full_scenario(tdir, rtype):
    print(tdir)
    #1h
    runname = 'bc370'
    print(f'checking {runname}')
    yrs = np.arange(1950,2015,1)
    for y in yrs:
        check_filetype_present(tdir, y,runname,rtype)    
    #1a
    runname = 'be682'
    print(f'checking {runname}')
    yrs = np.arange(2015,2100,1)
    for y in yrs:
        check_filetype_present(tdir, y,runname,rtype)
    print()
    #1b
    runname= 'ce417'
    print(f'checking {runname}')
    yrs = np.arange(2015,2100,1)
    for y in yrs:
        check_filetype_present(tdir, y,runname,rtype)
    print()
    # #2h
    runname = 'cj198'
    print(f'checking {runname}')
    yrs = np.arange(1950,2015,1)
    for y in yrs:
        check_filetype_present(tdir, y,runname,rtype)    
    print()
    # #2a
    runname = 'cj880'
    print(f'checking {runname}')
    yrs = np.arange(2015,2100,1)
    for y in yrs:
        check_filetype_present(tdir, y,runname,rtype)
    print()    
    # #2b
    runname= 'cj881'
    print(f'checking {runname}')
    yrs = np.arange(2015,2100,1)
    for y in yrs:
        check_filetype_present(tdir, y,runname,rtype)

    print()    
    # #3h
    runname = 'cj200'
    print(f'checking {runname}')
    yrs = np.arange(1990,2015,1)
    for y in yrs:
        check_filetype_present(tdir, y,runname,rtype)    
    print()
    # #3a
    runname = 'cj484'
    print(f'checking {runname}')
    yrs = np.arange(2015,2100,1)
    for y in yrs:
        check_filetype_present(tdir, y,runname,rtype)    
    print()    
    # #3a
    runname = 'cj504'
    print(f'checking {runname}')
    yrs = np.arange(2015,2100,1)
    for y in yrs:
        check_filetype_present(tdir, y,runname,rtype)  

print('je to k posrani')
check_full_scenario('ukesm_allscen_gridT_TS','grid-T') 
print('hlavne se neposrat')