#-----IMPORTS
import matplotlib.pyplot as plt
import glob
import xarray as xr
import sys
sys.path.append('/gpfs/home/mep22dku/scratch/SOZONE/MODPROC_ROBOT/MultiModelMonitor/WORK_SCRIPTS')
sys.path.append('/gpfs/home/mep22dku/scratch/SOZONE/MO_pipeline/')
import scendict as sc
import breakdown as bp
import plotr as pr
 
#------CHANGE THIS TO WHAT YOU WANT TO EXTRACT
extract = False #extracting?
graph = True #plotting?
sdir = '/gpfs/home/mep22dku/scratch/SOZONE/MODPROC_ROBOT/MultiModelMonitor/OUTPUT/' #results directory
fnam = 'Cflx_comparison.png' ## filename for resulting plot
tms = ['TOM12_TJ_1AS6','TOM12_TJ_1BS2', 'TOM12_TJ_3AS1','TOM12_DW_WE43', 'TOM12_DW_GA01'] ##models to plot
tms_te = [] ##models to extract
descs = ['1AS6: TJ(MET), Hist. ozone, \n SSP 1-2.6, restart@ WE43(1948)',\
         '1BS2: TJ(MET), Hist. ozone, \n SSP 3-7.0, restart@ WE43(1948)',\
         '3AS1: TJ(MET), Ozone-1990, \n SSP 1-2.6, restart@ WE43(1948)',\
         'WE43: DW(ERA5)',
         'GA01: DW(NCEP), GCB run'] #descriptions of models in tm
cols = [sc.scen['1A']['color'],sc.scen['1B']['color'],sc.scen['3A']['color'], 'grey', 'b'] #colours for models in tm

if extract: 
    for tm in tms_te:
        bp.breakdown_maker(tr, fmi = 1948, bdflag = 'cflx', resDir = sdir)

### open the datasets
if graph:
    dsets = []

    for tm in tms:
        w = glob.glob(f'{sdir}*{tm}*')
        ds = xr.open_dataset(w[0])
        dsets.append(ds)
    pr.plot_carbon(dsets, cols, descs, sdir, fnam, tend = 2100, tendatm = 450)