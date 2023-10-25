import xarray as xr
import glob

scendict = {
    '1A': {
        'hist_str': 'bc370',
        'fut_str': 'be682',
        'name': 'HIST.OZONE \n LOW TEMP.',
        'name2':'1A: NatlOzone-SSP126',
        'color':'#E8D215',
        'color2':'orange'},
    '1B': {
        'hist_str': 'bc370',
        'fut_str': 'ce417',
        'name': 'HIST. OZONE \n HIGH TEMP.',
        'name2':'1B: NatlOzone-SSP370',
        'color':'#87800A',
        'color2':'orangered'},
    '2A': {
        'hist_str': 'cj198',
        'fut_str': 'cj880',
        'name': 'FIXED OZONE \n LOW TEMP.',
        'name2':'2A: Ozone1950-SSP126',
        'color':'#2DC18E',
        'color2':'mediumseagreen'},
    '2B': {
        'hist_str': 'cj198',
        'fut_str': 'cj881',
        'name': 'FIXED OZONE \n HIGH TEMP.',
        'name2':'2B: Ozone1950-SSP370',
        'color':'#18765C',
        'color2':'green'},
    '3A': {
        'hist_str': 'cj200',
        'fut_str': 'cj484',
        'name': '1990 OZONE \n LOW TEMP.',
        'name2':'3A: Ozone1990-SSP126',
        'color':'#FF462B',
        'color2':'dodgerblue'},
    '3B': {
        'hist_str': 'cj200',
        'fut_str': 'cj504',
        'name': '1990 OZONE \n HIGH TEMP.',
        'name2':'3B: Ozone1990-SSP370',
        'color':'#822722',
        'color2':'mediumblue'}
}


ukmesh = xr.open_dataset('/gpfs/data/greenocean/software/resources/MEDUSA/mesh_mask_eORCA1_wrk.nc')
ukmesh['area'] = ukmesh.tmask[0,:,:] * ukmesh.e1t[:,:] * ukmesh.e2t[:,:]


def make_yearlist_ukesm(yrst, yren, tscen, dtype = 'grid-T'):
    print(f'SCENARIO {tscen}')
    dslist = []

    for y in range(yrst,yren):
        if ((y<1990) & ((tscen == '3A') | (tscen == '3B'))):
            tstr = scendict['1A']['hist_str']
        elif y<2015:
            tstr = scendict[tscen]['hist_str']

        else:
            tstr = scendict[tscen]['fut_str']

        try:
            td = glob.glob(f'/gpfs/data/greenocean/software/resources/MEDUSA/PROC2/*{tstr}*{y}*{dtype}*')
            dslist.append(td[0])
        except:
            pass
            #print(f'FAIL {tscen},{tstr}, {y}')
    return dslist

tdir = '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/paperFigures/intermediateCalculations/'

yst = 1950; yen = 2100

mld_1A = xr.open_mfdataset(make_yearlist_ukesm(yst,yen,'1A', dtype = 'TS'))
v  = mld_1A.votemper.isel(deptht=0).sel(y=slice(0,114)).weighted(ukmesh['area'].sel(y=slice(0,114))).mean(dim = ['x','y'])
v.name = "votemper"
v.attrs["units"] = "m"
v.attrs["desc"] = "area-weighted mean south of -50 from ukesm"
v.to_netcdf(f'{tdir}_-50_SST_1A.nc')

mld_1B = xr.open_mfdataset(make_yearlist_ukesm(yst,yen,'1B', dtype = 'TS'))
v  = mld_1B.votemper.isel(deptht=0).sel(y=slice(0,114)).weighted(ukmesh['area'].sel(y=slice(0,114))).mean(dim = ['x','y'])
v.name = "votemper"
v.attrs["units"] = "m"
v.attrs["desc"] = "area-weighted mean south of -50 from ukesm"
v.to_netcdf(f'{tdir}_-50_SST_1B.nc')

mld_2A = xr.open_mfdataset(make_yearlist_ukesm(yst,yen,'2A', dtype = 'TS'))
v  = mld_2A.votemper.isel(deptht=0).sel(y=slice(0,114)).weighted(ukmesh['area'].sel(y=slice(0,114))).mean(dim = ['x','y'])
v.name = "votemper"
v.attrs["units"] = "m"
v.attrs["desc"] = "area-weighted mean south of -50 from ukesm"
v.to_netcdf(f'{tdir}_-50_SST_2A.nc')

mld_2B = xr.open_mfdataset(make_yearlist_ukesm(yst,yen,'2B', dtype = 'TS'))
v  = mld_2B.votemper.isel(deptht=0).sel(y=slice(0,114)).weighted(ukmesh['area'].sel(y=slice(0,114))).mean(dim = ['x','y'])
v.name = "votemper"
v.attrs["units"] = "m"
v.attrs["desc"] = "area-weighted mean south of -50 from ukesm"
v.to_netcdf(f'{tdir}_-50_SST_2B.nc')

mld_3A = xr.open_mfdataset(make_yearlist_ukesm(yst,yen,'3A', dtype = 'TS'))
v  = mld_3A.votemper.isel(deptht=0).sel(y=slice(0,114)).weighted(ukmesh['area'].sel(y=slice(0,114))).mean(dim = ['x','y'])
v.name = "votemper"
v.attrs["units"] = "m"
v.attrs["desc"] = "area-weighted mean south of -50 from ukesm"
v.to_netcdf(f'{tdir}_-50_SST_3A.nc')

mld_3B = xr.open_mfdataset(make_yearlist_ukesm(yst,yen,'3B', dtype = 'TS'))
v  = mld_3B.votemper.isel(deptht=0).sel(y=slice(0,114)).weighted(ukmesh['area'].sel(y=slice(0,114))).mean(dim = ['x','y'])
v.name = "votemper"
v.attrs["units"] = "m"
v.attrs["desc"] = "area-weighted mean south of -50 from ukesm"
v.to_netcdf(f'{tdir}_-50_SST_3B.nc')
