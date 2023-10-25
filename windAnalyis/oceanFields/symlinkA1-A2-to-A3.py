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

# ###
# dstrun = 'TOM12_TJ_1AA3'
# srcrun = 'TOM12_TJ_1AA1'
# for yr in range(1950,2014):
#     bdir = '/gpfs/data/greenocean/software/runs/'
#     do_symlinks(bdir,srcrun,dstrun,yr)
# srcrun = 'TOM12_TJ_1AA2'
# for yr in range(2014,2053):
#     bdir = '/gpfs/data/greenocean/software/runs/'
#     do_symlinks(bdir,srcrun,dstrun,yr)
# ###
# dstrun = 'TOM12_TJ_1BA3'
# srcrun = 'TOM12_TJ_1BA1'
# for yr in range(1950,2013):
#     bdir = '/gpfs/data/greenocean/software/runs/'
#     do_symlinks(bdir,srcrun,dstrun,yr)
# srcrun = 'TOM12_TJ_1BA2'
# for yr in range(2013,2053):
#     bdir = '/gpfs/data/greenocean/software/runs/'
#     do_symlinks(bdir,srcrun,dstrun,yr)
# ###
# ###
# dstrun = 'TOM12_TJ_2AA3'
# srcrun = 'TOM12_TJ_2AA1'
# for yr in range(1950,2013):
#     bdir = '/gpfs/data/greenocean/software/runs/'
#     do_symlinks(bdir,srcrun,dstrun,yr)
# srcrun = 'TOM12_TJ_2AA2'
# for yr in range(2013,2053):
#     bdir = '/gpfs/data/greenocean/software/runs/'
#     do_symlinks(bdir,srcrun,dstrun,yr)
# ###
# dstrun = 'TOM12_TJ_2BA3'
# srcrun = 'TOM12_TJ_2BA1'
# for yr in range(1950,2013):
#     bdir = '/gpfs/data/greenocean/software/runs/'
#     do_symlinks(bdir,srcrun,dstrun,yr)
# srcrun = 'TOM12_TJ_2BA2'
# for yr in range(2013,2053):
#     bdir = '/gpfs/data/greenocean/software/runs/'
#     do_symlinks(bdir,srcrun,dstrun,yr)
# ###
# ###
# dstrun = 'TOM12_TJ_3AA3'
# srcrun = 'TOM12_TJ_3AA1'
# for yr in range(1950,2013):
#     bdir = '/gpfs/data/greenocean/software/runs/'
#     do_symlinks(bdir,srcrun,dstrun,yr)
# srcrun = 'TOM12_TJ_3AA2'
# for yr in range(2013,2053):
#     bdir = '/gpfs/data/greenocean/software/runs/'
#     do_symlinks(bdir,srcrun,dstrun,yr)
# ###
# dstrun = 'TOM12_TJ_3BA3'
# srcrun = 'TOM12_TJ_3BA1'
# for yr in range(1950,2008):
#     bdir = '/gpfs/data/greenocean/software/runs/'
#     do_symlinks(bdir,srcrun,dstrun,yr)
# srcrun = 'TOM12_TJ_3BA2'
# for yr in range(2008,2017):
#     bdir = '/gpfs/data/greenocean/software/runs/'
#     do_symlinks(bdir,srcrun,dstrun,yr)
###

# dstrun = 'TOM12_TJ_2BA6'
# srcrun = 'TOM12_TJ_2BA3'
# for yr in range(1999,2001):
#     bdir = '/gpfs/data/greenocean/software/runs/'
#     do_symlinks(bdir,srcrun,dstrun,yr)
# print('again')
# print('done!')