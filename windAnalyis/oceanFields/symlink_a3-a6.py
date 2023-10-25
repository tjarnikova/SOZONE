import os
import sys

def do_symlinks(bdir,srcrun,dstrun,yr):

    try:
        tfil = f'ORCA2_1m_{yr}0101_{yr}1231_ptrc_T.nc'
        src = f'{bdir}/{srcrun}/{tfil}'
        dst = f'{bdir}/{dstrun}/{tfil}'
        os.symlink(src, dst)
    except:
        print(f'failed {dst}')

    try:
        tfil = f'ORCA2_1m_{yr}0101_{yr}1231_grid_T.nc'
        src = f'{bdir}/{srcrun}/{tfil}'
        dst = f'{bdir}/{dstrun}/{tfil}'
        os.symlink(src, dst)
    except:
        print(f'failed {dst}')

    try:
        tfil = f'ORCA2_1m_{yr}0101_{yr}1231_diad_T.nc'
        src = f'{bdir}/{srcrun}/{tfil}'
        dst = f'{bdir}/{dstrun}/{tfil}'
        os.symlink(src, dst)
    except:
        print(f'failed {dst}')

    try:
        tfil = f'ORCA2_1m_{yr}0101_{yr}1231_grid_V.nc'
        src = f'{bdir}/{srcrun}/{tfil}'
        dst = f'{bdir}/{dstrun}/{tfil}'
        os.symlink(src, dst)
    except:
        print(f'failed {dst}')

    try:
        tfil = f'ORCA2_1m_{yr}0101_{yr}1231_icemod.nc'
        src = f'{bdir}/{srcrun}/{tfil}'
        dst = f'{bdir}/{dstrun}/{tfil}'
        os.symlink(src, dst)
    except:
        print(f'failed {dst}')

###
dstrun = 'TOM12_TJ_1AA6'
srcrun = 'TOM12_TJ_1AA3'
for yr in range(1950,2073):
    bdir = '/gpfs/data/greenocean/software/runs/'
    do_symlinks(bdir,srcrun,dstrun,yr)

###
dstrun = 'TOM12_TJ_1BA6'
srcrun = 'TOM12_TJ_1BA3'
for yr in range(1950,2073):
    bdir = '/gpfs/data/greenocean/software/runs/'
    do_symlinks(bdir,srcrun,dstrun,yr)
    
    
###
dstrun = 'TOM12_TJ_2AA6'
srcrun = 'TOM12_TJ_2AA3'
for yr in range(1950,2073):
    bdir = '/gpfs/data/greenocean/software/runs/'
    do_symlinks(bdir,srcrun,dstrun,yr)
    
###
dstrun = 'TOM12_TJ_2BA6'
srcrun = 'TOM12_TJ_2BA3'
for yr in range(1950,2073):
    bdir = '/gpfs/data/greenocean/software/runs/'
    do_symlinks(bdir,srcrun,dstrun,yr)
    
###
dstrun = 'TOM12_TJ_3AA6'
srcrun = 'TOM12_TJ_3AA3'
for yr in range(1950,2073):
    bdir = '/gpfs/data/greenocean/software/runs/'
    do_symlinks(bdir,srcrun,dstrun,yr)
    
###
dstrun = 'TOM12_TJ_3BA6'
srcrun = 'TOM12_TJ_3BA3'
for yr in range(1950,2073):
    bdir = '/gpfs/data/greenocean/software/runs/'
    do_symlinks(bdir,srcrun,dstrun,yr)
