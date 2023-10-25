import os

# lrwxrwxrwx 1 avd22gnu greenocean 25 Oct 20 07:52 era5_bulk_8_y2000.nc -> bulk_2000_8_era5_daily.nc
# lrwxrwxrwx 1 avd22gnu greenocean 25 Oct 20 07:52 era5_bulk_9_y2000.nc -> bulk_2000_9_era5_daily.nc
# lrwxrwxrwx 1 avd22gnu greenocean 26 Oct 20 07:52 era5_bulk_15_y2000.nc -> bulk_2000_15_era5_daily.nc
# lrwxrwxrwx 1 avd22gnu greenocean 26 Oct 20 07:52 era5_bulk_14_y2000.nc -> bulk_2000_14_era5_daily.nc
# lrwxrwxrwx 1 avd22gnu greenocean 26 Oct 20 07:52 era5_bulk_11_y2000.nc -> bulk_2000_11_era5_daily.nc
# lrwxrwxrwx 1 avd22gnu greenocean 21 Oct 20 07:52 tauy_1d_y2000.nc -> tauy_1d_2000_daily.nc
# lrwxrwxrwx 1 avd22gnu greenocean 26 Oct 20 07:53 era5_bulk_13_y2000.nc -> bulk_2000_13_era5_daily.nc
# lrwxrwxrwx 1 avd22gnu greenocean 21 Oct 20 07:53 taux_1d_y2000.nc -> taux_1d_2000_daily.nc
# lrwxrwxrwx 1 avd22gnu greenocean 26 Oct 20 07:53 era5_bulk_12_y2000.nc -> bulk_2000_12_era5_daily.nc


# src = '/gpfs/home/mep22dku/scratch/MET_soft/hist/u-bc370_hist//bulk_1981_16_met_daily.nc'
# dst = '/gpfs/home/mep22dku/scratch/MET_forcing/scen_1A/MetOffice_tair10m1981.nc'

# os.symlink(src,dst)

tdir = '/gpfs/data/greenocean/software/products/ERA5_v202303_TJ/'

print('testing tym socialne divergentni')


for y in range(1940,2020):
    print(y)
    for b in range(8,16):
        try:
            src = f'{tdir}bulk_{y}_{b}_era5_daily.nc'
            dst = f'{tdir}era5_bulk_{b}_y{y}.nc'
            os.symlink(src,dst)
            print(f'year {y} bulk variable {b} GO!')
        except:
            print(f'didnt work for year {y} bulk variable {b}')
        try: 
            src = f'{tdir}taux_1d_{y}_daily.nc'
            dst = f'{tdir}taux_1d_y{y}.nc'
            os.symlink(src,dst)
        except:
            print('year {y} taux is off')
        try:
            src = f'{tdir}tauy_1d_{y}_daily.nc'
            dst = f'{tdir}tauy_1d_y{y}.nc'
            os.symlink(src,dst)
        except:
            print('year {y} tauy is off')

# #symlink the old era for variable 9, because it hates us
# tdir2 = '/gpfs/data/greenocean/software/products/ERA5Forcing/daily/1990spinup/'

# for y in range(1940,2020):
#     print(y)
#     for b in range(9,10):
#         try:
#             src = f'{tdir2}era5_bulk_{b}_y{y}.nc'
#             dst = f'{tdir}era5_bulk_{b}_y{y}.nc'
#             os.symlink(src,dst)
#             print(f'quick fix year {y} bulk variable {b} GO!')
#         except:
#             print(f'didnt work for year {y} bulk variable {b}')
#     try:
#         src = f'{tdir}taux_1d_{y}_daily.nc'
#         dst = f'{tdir}taux_1d_y{y}.nc'
#         os.symlink(src,dst)
#     except:
#         print('year {y} taux is off')
#     try:
#         src = f'{tdir}tauy_1d_{y}_daily.nc'
#         dst = f'{tdir}tauy_1d_y{y}.nc'
#         os.symlink(src,dst)
#     except:
#         print('year {y} tauy is off')



print('we have shutdown')
