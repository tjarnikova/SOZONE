import glob
import numpy as np
import xarray as xr

def check_filetype_present(yr,runname,rtype):

    savenam = f'/gpfs/data/greenocean/software/resources/MEDUSA/PROC2/*_{runname}*1y_{yr}*{rtype}*nc'

    tw = glob.glob(savenam)
    #print(tw)
    ### need 12 monthly files
    if len(tw) != 1:
        print(f'{yr}, {runname} {rtype} missing')
    else:
        pass
    
def check_full_scenario(rtype):

    #1h
    runname = 'bc370'
    print(f'checking {runname}')
    yrs = np.arange(1950,2015,1)
    for y in yrs:
        check_filetype_present(y,runname,rtype)    
    #1a
    runname = 'be682'
    print(f'checking {runname}')
    yrs = np.arange(2015,2100,1)
    for y in yrs:
        check_filetype_present(y,runname,rtype)
    print()
    #1b
    runname= 'ce417'
    print(f'checking {runname}')
    yrs = np.arange(2015,2100,1)
    for y in yrs:
        check_filetype_present(y,runname,rtype)
    print()
    # #2h
    runname = 'cj198'
    print(f'checking {runname}')
    yrs = np.arange(1950,2015,1)
    for y in yrs:
        check_filetype_present(y,runname,rtype)    
    print()
    # #2a
    runname = 'cj880'
    print(f'checking {runname}')
    yrs = np.arange(2015,2100,1)
    for y in yrs:
        check_filetype_present(y,runname,rtype)
    print()    
    # #2b
    runname= 'cj881'
    print(f'checking {runname}')
    yrs = np.arange(2015,2100,1)
    for y in yrs:
        check_filetype_present(y,runname,rtype)

    print()    
    # #3h
    runname = 'cj200'
    print(f'checking {runname}')
    yrs = np.arange(1990,2015,1)
    for y in yrs:
        check_filetype_present(y,runname,rtype)    
    print()
    # #3a
    runname = 'cj484'
    print(f'checking {runname}')
    yrs = np.arange(2015,2100,1)
    for y in yrs:
        check_filetype_present(y,runname,rtype)    
    print()    
    # #3a
    runname = 'cj504'
    print(f'checking {runname}')
    yrs = np.arange(2015,2100,1)
    for y in yrs:
        check_filetype_present(y,runname,rtype)  


typ = 'grid-T-TS'
print(typ)
check_full_scenario(typ) 
