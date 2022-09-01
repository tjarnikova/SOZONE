import glob
import pickle
import netCDF4 as nc
import numpy as np
 
runhorse = True
rdir = '/gpfs/home/mep22dku/scratch/MET_soft/'
dir_1H = 'hist/u-bc370_hist/'
dir_2H = 'hist/u-cj198_hist_1950start1950ozone/'
dir_3H = 'hist/u-cj200_hist_1990start1990ozone/'

dir_1FA = 'ssp126/u-be682_ssp126/'
dir_1FB = 'ssp370/u-ce417_ssp370/'

dir_2FA = 'ssp126/u-cj880_ssp126_1950start1950ozone/'
dir_2FB = 'ssp370/u-cj881_ssp370_1950start1950ozone/'

dir_3FA = 'ssp126/u-cj484_ssp126_1990start1990ozone/'
dir_3FB = 'ssp370/u-cj504_ssp370_1990start1990ozone/'

def return_mean_SO_wspd(tdir,yr):
    
    days_in_month = np.array([31,28,31,30,31,30,31,31,30,31,30,31])
    starts = np.zeros_like(days_in_month)
    ends = np.zeros_like(starts)

    monthly_sts = np.zeros([12,3])
    monthly_sts[:] = np.nan
    
    for i in range(0,12):
        starts[i] = np.sum(days_in_month[0:i])
        ends[i] = np.sum(days_in_month[0:i+1])
    
    
    rdir = f'/gpfs/home/mep22dku/scratch/MET_soft/{tdir}'
    uf_f = glob.glob(f'{rdir}/taux_1d_{yr}_daily.nc')
    vf_f = glob.glob(f'{rdir}/tauy_1d_{yr}_daily.nc')

    try:
        uf = nc.Dataset(uf_f[0])
        uf_nc = (uf['uflx'])
        vf = nc.Dataset(vf_f[0])
        vf_nc = (vf['vflx'])
        
        #south of 50
        for i in range(0,12):
            uf_t_mon = uf_nc[starts[i]:ends[i],0:37,:]
            vf_t_mon = uf_nc[starts[i]:ends[i],0:37,:]
            t_mon = np.sqrt(uf_t_mon**2 + vf_t_mon**2)
            monthly_sts[i,0] = np.nanmean(t_mon)
            monthly_sts[i,1] = np.nanmax(t_mon)
            monthly_sts[i,2] = np.nanmin(t_mon)

    except:
        print('cannot find')
        print(f'{tdir} {yr}')
        x = 'we'
                    
    return monthly_sts
    
def calc_stats_wspd(tdir, yrstart, yrend):
    yrs = np.arange(yrstart,yrend,1)
    stor = np.zeros([len(yrs),12,3])
    for i in range(0,len(yrs)):
        yr = yrs[i]
        if yr%50 == 0: print(yr)
        monthly_sts = return_mean_SO_wspd(tdir,yr)
        stor[i,:,:] = monthly_sts
    
    return stor


if runhorse:
    tnam = 'scen_1H'; tdir = dir_1H; yrstart = 1940; yrend = 2015
    stor = calc_stats_wspd(tdir,yrstart,yrend)
    pickle.dump(stor, open(f"./pkls/{tnam}_wspd_{yrstart}_{yrend}.pkl", 'wb'))

    tnam = 'scen_2H'; tdir = dir_2H; yrstart = 1950; yrend = 2015
    stor = calc_stats_wspd(tdir,yrstart,yrend)
    pickle.dump(stor, open(f"./pkls/{tnam}_wspd_{yrstart}_{yrend}.pkl", 'wb'))

    tnam = 'scen_3H'; tdir = dir_3H; yrstart = 1990; yrend = 2015
    stor = calc_stats_wspd(tdir,yrstart,yrend)
    pickle.dump(stor, open(f"./pkls/{tnam}_wspd_{yrstart}_{yrend}.pkl", 'wb'))

    tnam = 'scen_1FA'; tdir = dir_1FA; yrstart = 2015; yrend = 2101
    stor = calc_stats_wspd(tdir,yrstart,yrend)
    pickle.dump(stor, open(f"./pkls/{tnam}_wspd_{yrstart}_{yrend}.pkl", 'wb'))

    tnam = 'scen_2FA'; tdir = dir_2FA; yrstart = 2015; yrend = 2101
    stor = calc_stats_wspd(tdir,yrstart,yrend)
    pickle.dump(stor, open(f"./pkls/{tnam}_wspd_{yrstart}_{yrend}.pkl", 'wb'))

    tnam = 'scen_3FA'; tdir = dir_3FA; yrstart = 2015; yrend = 2101
    stor = calc_stats_wspd(tdir,yrstart,yrend)
    pickle.dump(stor, open(f"./pkls/{tnam}_wspd_{yrstart}_{yrend}.pkl", 'wb'))

    tnam = 'scen_1FB'; tdir = dir_1FB; yrstart = 2015; yrend = 2101
    stor = calc_stats_wspd(tdir,yrstart,yrend)
    pickle.dump(stor, open(f"./pkls/{tnam}_wspd_{yrstart}_{yrend}.pkl", 'wb'))

    tnam = 'scen_2FB'; tdir = dir_2FB; yrstart = 2015; yrend = 2101
    stor = calc_stats_wspd(tdir,yrstart,yrend)
    pickle.dump(stor, open(f"./pkls/{tnam}_wspd_{yrstart}_{yrend}.pkl", 'wb'))

    tnam = 'scen_3FB'; tdir = dir_3FB; yrstart = 2015; yrend = 2101
    stor = calc_stats_wspd(tdir,yrstart,yrend)
    pickle.dump(stor, open(f"./pkls/{tnam}_wspd_{yrstart}_{yrend}.pkl", 'wb'))
