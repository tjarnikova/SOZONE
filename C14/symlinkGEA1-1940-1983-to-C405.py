import os
import sys


for yr in range(1940,1983):
    
    bdir = '/gpfs/data/greenocean/software/runs/'
    srcrun = 'TOM12_TJ_GEC1'
    dstrun = 'TOM12_TJ_C4C5'
    
    tfil = f'ORCA2_1m_{yr}0101_{yr}1231_ptrc_T.nc'
    src = f'{bdir}/{srcrun}/{tfil}'
    dst = f'{bdir}/{dstrun}/{tfil}'
    os.symlink(src, dst)
    
    tfil = f'ORCA2_1m_{yr}0101_{yr}1231_grid_T.nc'
    src = f'{bdir}/{srcrun}/{tfil}'
    dst = f'{bdir}/{dstrun}/{tfil}'
    os.symlink(src, dst)
    
    tfil = f'ORCA2_1m_{yr}0101_{yr}1231_diad_T.nc'
    src = f'{bdir}/{srcrun}/{tfil}'
    dst = f'{bdir}/{dstrun}/{tfil}'
    os.symlink(src, dst)