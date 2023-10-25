import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 12})
font = {'family' : 'monospace',
'weight' : 'normal',
'size'   : 12}

plt.rc('font', **font)

mod = {
    '1A': {
        'hist_str': 'bc370',
        'fut_str': 'be682',
        'name': 'HIST.OZONE \n LOW TEMP.',
        'name2':'1A: NatlOzone-SSP126',
        'color':'#E8D215',
        'runid':'TOM12_TJ_1AA3'},
    '1B': {
        'hist_str': 'bc370',
        'fut_str': 'ce417',
        'name': 'HIST. OZONE \n HIGH TEMP.',
        'name2':'1B: NatlOzone-SSP370',
        'color':'#87800A',
        'runid':'TOM12_TJ_1BA3'},
    '2A': {
        'hist_str': 'cj198',
        'fut_str': 'cj880',
        'name': 'FIXED OZONE \n LOW TEMP.',
        'name2':'2A: Ozone1950-SSP126',
        'color':'#2DC18E',
        'runid':'TOM12_TJ_2AA3'},
    '2B': {
        'hist_str': 'cj198',
        'fut_str': 'cj881',
        'name': 'FIXED OZONE \n HIGH TEMP.',
        'name2':'2B: Ozone1950-SSP370',
        'color':'#18765C',
        'runid':'TOM12_TJ_2BA3'},
    '3A': {
        'hist_str': 'cj200',
        'fut_str': 'cj484',
        'name': '1990 OZONE \n LOW TEMP.',
        'name2':'3A: Ozone1990-SSP126',
        'color':'#FF462B',
        'runid':'TOM12_TJ_3AA3'},
    '3B': {
        'hist_str': 'cj200',
        'fut_str': 'cj504',
        'name': '1990 OZONE \n HIGH TEMP.',
        'name2':'3B: Ozone1990-SSP370',
        'color':'#822722',
        'runid':'TOM12_TJ_3BA3'},
    'PI': {
        'hist_str': '',
        'fut_str': '',
        'name': 'PI OZONE \n PI TEMP.',
        'name2':'PI: OzonePI-PI',
        'color':'silver',
        'runid':'TOM12_TJ_PIA3'}
}

models = ['1A','1B','2A','2B','3A','3B' ]
#'3B','PI'
tvar = 'Cflx_total'
ttit = 'Cflx, pgC_yr'

plt.figure()

fact = 1.1
fig, axs = plt.subplots(1,1, figsize=(12*fact, 6*fact), facecolor='w', edgecolor='k')
# axs = axs.ravel()

ind = 0
for i in range(0,len(models)):
    tmod = models[i]
    print(tmod)
    trunid = mod[tmod]['runid']
    
    tdat = pd.read_csv(f'/gpfs/home/mep22dku/scratch/ModelRuns//{trunid}/breakdown.sur.annual.dat', sep='\t')
    tcol = mod[tmod]['color']
    tlin = '-'#mod[tmod]['linestyle']
    tdesc = mod[tmod]['runid']

    tdat = pd.read_csv(f'/gpfs/home/mep22dku/scratch/ModelRuns//{trunid}/breakdown.sur.annual.dat', sep='\t')
    year = tdat.year[2:].to_numpy().astype(float)
    Cflx_total = tdat.Cflx[2:].to_numpy().astype(float)
    filt = (year>1700)
    axs.plot(year[filt],Cflx_total[filt], linestyle = tlin, color = tcol, label = f'{tmod} \n {tdesc}')

    axs.legend(ncol = 4, loc = 'best', fontsize = 12)
    axs.set_ylabel('global cflx Pg/y')
    axs.grid(linestyle = ':')

fig.savefig('./figs/Cflx_monitor.jpg')
