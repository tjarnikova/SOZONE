import numpy as np
import xarray as xr
import glob

scen = 'PI'
dir2 = '/gpfs/data/greenocean/software/products/MetOffice/u-aw310_pictrl/'
for y in range(1950,2101):
    print(y)
    yPI = y + 270
    print(yPI)
    wx = glob.glob(f'{dir2}/*wind*y{yPI}*')
    wx2 = np.sort(wx)#wx.sort()
    print(wx2)
    print()
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
