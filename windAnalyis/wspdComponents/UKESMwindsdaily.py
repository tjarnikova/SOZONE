import xarray as xr 
import numpy as np
import glob

tdir = '/gpfs/data/greenocean/software/resources/MetOffice/fixed_ozone/'
dir_1H = 'hist/u-bc370_hist/'
dir_2H = 'hist/u-cj198_hist_1950start1950ozone/'
dir_3H = 'hist/u-cj200_hist_1990start1990ozone/'

dir_1FA = 'ssp126/u-be682_ssp126/'
dir_1FB = 'ssp370/u-ce417_ssp370/'

dir_2FA = 'ssp126/u-cj880_ssp126_1950start1950ozone/'
dir_2FB = 'ssp370/u-cj881_ssp370_1950start1950ozone/'

dir_3FA = 'ssp126/u-cj484_ssp126_1990start1990ozone/'
dir_3FB = 'ssp370/u-cj504_ssp370_1990start1990ozone/'

fact = 1.1
fig, axs = plt.subplots(2,5, figsize=(12*fact, 8*fact), facecolor='w', edgecolor='k')
axs = axs.ravel()
cdom

##1A

scen = '1A'
# for y in range(1940,2101):
#     if y < 2015:
#         dir2 = dir_1H
#     if y >= 2015:
#         dir2 = dir_1FA
#     fdir = f'{tdir}{dir2}'
#     print(y)
#     wx = glob.glob(f'{fdir}/*wind*y{y}*')
#     wx2 = np.sort(wx)#wx.sort()
#     mons = ['01','02','03','04','05','06','07','08','09','10','11','12']
#     for i in range(0,12):
#         if f'm{mons[i]}' not in wx2[i]:
#             print(f'problem in {fdir}, {mons[i]}')
#         else:
#             pass
#         w = xr.open_dataset(wx2[i])
#         savedir = '/gpfs/data/greenocean/software/products/windsFromComponents/UKESM_monthly_atdayres/'
#         savestr = f'UKESM_{scen}_y{y}m{mons[i]}'
#         print(savestr)
#         w2 = w.uwind10m.groupby('time_counter.day').mean()
#         w3 = w2.to_dataset()
#         w3['day'] = np.arange(i*30+1,(i+1)*30+1,1)
#         w3.attrs = {'made in': '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/UKESMwindsdaily.py'}
#         w3.to_netcdf(f'{savedir}{savestr}_uwind10m_daily.nc')

#         w4 = w.vwind10m.groupby('time_counter.day').mean()
#         w5 = w4.to_dataset()
#         w5['day'] = np.arange(i*30+1,(i+1)*30+1,1)
#         w5.attrs = {'made in': '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/UKESMwindsdaily.py'}
#         w5.to_netcdf(f'{savedir}{savestr}_vwind10m_daily.nc')

# ##1A

# scen = '1B'
# print()
# print(scen)
# for y in range(1940,2101):
#     if y < 2015:
#         dir2 = dir_1H
#     if y >= 2015:
#         dir2 = dir_1FB
#     fdir = f'{tdir}{dir2}'
#     print(y)
#     wx = glob.glob(f'{fdir}/*wind*y{y}*')
#     wx2 = np.sort(wx)#wx.sort()
#     mons = ['01','02','03','04','05','06','07','08','09','10','11','12']
#     for i in range(0,12):
#         if f'm{mons[i]}' not in wx2[i]:
#             print(f'problem in {fdir}, {mons[i]}')
#         else:
#             pass
#         w = xr.open_dataset(wx2[i])
#         savedir = '/gpfs/data/greenocean/software/products/windsFromComponents/UKESM_monthly_atdayres/'
#         savestr = f'UKESM_{scen}_y{y}m{mons[i]}'
#         print(savestr)
#         w2 = w.uwind10m.groupby('time_counter.day').mean()
#         w3 = w2.to_dataset()
#         w3['day'] = np.arange(i*30+1,(i+1)*30+1,1)
#         w3.attrs = {'made in': '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/UKESMwindsdaily.py'}
#         w3.to_netcdf(f'{savedir}{savestr}_uwind10m_daily.nc')

#         w4 = w.vwind10m.groupby('time_counter.day').mean()
#         w5 = w4.to_dataset()
#         w5['day'] = np.arange(i*30+1,(i+1)*30+1,1)
#         w5.attrs = {'made in': '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/UKESMwindsdaily.py'}
#         w5.to_netcdf(f'{savedir}{savestr}_vwind10m_daily.nc')

# ####
# ##1A

# scen = '2A'
# for y in range(1940,2101):
#     if y < 1950:
#         dir2 = dir_1H
#         print(dir2)
#     if (y < 2015) & (y>=1950):
#         dir2 = dir_2H
#     if y >= 2015:
#         dir2 = dir_2FA
#     fdir = f'{tdir}{dir2}'
#     print(y)
#     wx = glob.glob(f'{fdir}/*wind*y{y}*')
#     wx2 = np.sort(wx)#wx.sort()
#     mons = ['01','02','03','04','05','06','07','08','09','10','11','12']
#     for i in range(0,12):
#         if f'm{mons[i]}' not in wx2[i]:
#             print(f'problem in {fdir}, {mons[i]}')
#         else:
#             pass
#         w = xr.open_dataset(wx2[i])
#         savedir = '/gpfs/data/greenocean/software/products/windsFromComponents/UKESM_monthly_atdayres/'
#         savestr = f'UKESM_{scen}_y{y}m{mons[i]}'
#         print(savestr)
#         w2 = w.uwind10m.groupby('time_counter.day').mean()
#         w3 = w2.to_dataset()
#         w3['day'] = np.arange(i*30+1,(i+1)*30+1,1)
#         w3.attrs = {'made in': '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/UKESMwindsdaily.py'}
#         w3.to_netcdf(f'{savedir}{savestr}_uwind10m_daily.nc')

#         w4 = w.vwind10m.groupby('time_counter.day').mean()
#         w5 = w4.to_dataset()
#         w5['day'] = np.arange(i*30+1,(i+1)*30+1,1)
#         w5.attrs = {'made in': '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/UKESMwindsdaily.py'}
#         w5.to_netcdf(f'{savedir}{savestr}_vwind10m_daily.nc')

# ##1A

# scen = '2B'
# print()
# print(scen)
# for y in range(1940,2101):
#     if y < 1950:
#         dir2 = dir_1H
#         print(dir2)
#     if (y < 2015) & (y>=1950):
#         dir2 = dir_2H
#     if y >= 2015:
#         dir2 = dir_2FA
#     fdir = f'{tdir}{dir2}'
#     print(y)
#     wx = glob.glob(f'{fdir}/*wind*y{y}*')
#     wx2 = np.sort(wx)#wx.sort()
#     mons = ['01','02','03','04','05','06','07','08','09','10','11','12']
#     for i in range(0,12):
#         if f'm{mons[i]}' not in wx2[i]:
#             print(f'problem in {fdir}, {mons[i]}')
#         else:
#             pass
#         w = xr.open_dataset(wx2[i])
#         savedir = '/gpfs/data/greenocean/software/products/windsFromComponents/UKESM_monthly_atdayres/'
#         savestr = f'UKESM_{scen}_y{y}m{mons[i]}'
#         print(savestr)
#         w2 = w.uwind10m.groupby('time_counter.day').mean()
#         w3 = w2.to_dataset()
#         w3['day'] = np.arange(i*30+1,(i+1)*30+1,1)
#         w3.attrs = {'made in': '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/UKESMwindsdaily.py'}
#         w3.to_netcdf(f'{savedir}{savestr}_uwind10m_daily.nc')

#         w4 = w.vwind10m.groupby('time_counter.day').mean()
#         w5 = w4.to_dataset()
#         w5['day'] = np.arange(i*30+1,(i+1)*30+1,1)
#         w5.attrs = {'made in': '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/UKESMwindsdaily.py'}
#         w5.to_netcdf(f'{savedir}{savestr}_vwind10m_daily.nc')

######### love is dumb

scen = '3A'
for y in range(1940,2101):
    if y < 1990:
        dir2 = dir_1H
    if (y>=1990) & (y < 2015):
        dir2 = dir_3H
    if y >= 2015:
        dir2 = dir_3FA
    fdir = f'{tdir}{dir2}'
    print(y)
    wx = glob.glob(f'{fdir}/*wind*y{y}*')
    wx2 = np.sort(wx)#wx.sort()
    mons = ['01','02','03','04','05','06','07','08','09','10','11','12']
    for i in range(0,12):
        if f'm{mons[i]}' not in wx2[i]:
            print(f'problem in {fdir}, {mons[i]}')
        else:
            pass
        w = xr.open_dataset(wx2[i])
        savedir = '/gpfs/data/greenocean/software/products/windsFromComponents/UKESM_monthly_atdayres/'
        savestr = f'UKESM_{scen}_y{y}m{mons[i]}'
        print(savestr)
        w2 = w.uwind10m.groupby('time_counter.day').mean()
        w3 = w2.to_dataset()
        w3['day'] = np.arange(i*30+1,(i+1)*30+1,1)
        w3.attrs = {'made in': '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/UKESMwindsdaily.py'}
        w3.to_netcdf(f'{savedir}{savestr}_uwind10m_daily.nc')

        w4 = w.vwind10m.groupby('time_counter.day').mean()
        w5 = w4.to_dataset()
        w5['day'] = np.arange(i*30+1,(i+1)*30+1,1)
        w5.attrs = {'made in': '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/UKESMwindsdaily.py'}
        w5.to_netcdf(f'{savedir}{savestr}_vwind10m_daily.nc')

##1A

scen = '3B'
for y in range(1940,2101):
    if y < 1990:
        dir2 = dir_1H
    if (y>=1990) & (y < 2015):
        dir2 = dir_3H
    if y >= 2015:
        dir2 = dir_3FB
    fdir = f'{tdir}{dir2}'
    print(y)
    wx = glob.glob(f'{fdir}/*wind*y{y}*')
    wx2 = np.sort(wx)#wx.sort()
    mons = ['01','02','03','04','05','06','07','08','09','10','11','12']
    for i in range(0,12):
        if f'm{mons[i]}' not in wx2[i]:
            print(f'problem in {fdir}, {mons[i]}')
        else:
            pass
        w = xr.open_dataset(wx2[i])
        savedir = '/gpfs/data/greenocean/software/products/windsFromComponents/UKESM_monthly_atdayres/'
        savestr = f'UKESM_{scen}_y{y}m{mons[i]}'
        print(savestr)
        w2 = w.uwind10m.groupby('time_counter.day').mean()
        w3 = w2.to_dataset()
        w3['day'] = np.arange(i*30+1,(i+1)*30+1,1)
        w3.attrs = {'made in': '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/UKESMwindsdaily.py'}
        w3.to_netcdf(f'{savedir}{savestr}_uwind10m_daily.nc')

        w4 = w.vwind10m.groupby('time_counter.day').mean()
        w5 = w4.to_dataset()
        w5['day'] = np.arange(i*30+1,(i+1)*30+1,1)
        w5.attrs = {'made in': '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/UKESMwindsdaily.py'}
        w5.to_netcdf(f'{savedir}{savestr}_vwind10m_daily.nc')
