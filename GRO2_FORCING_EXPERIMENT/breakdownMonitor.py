#simple model monitor based on the breakdowns that are created at the end of the model running process. 
#creates a csv summary in pandas and saves it under /gpfs/home/mep22dku/scratch/ModelRuns/modelBreakdownSummaries/{tmod}_breakdown.csv
#creates a picture and saves it under /gpfs/data/greenocean/software/runs/modelMonitor/plots/{tmod}_summary.jpg'


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tmodels = ['TOM12_TJ_GPB0', 'TOM12_TJ_GNB0', 'TOM12_TJ_GPA1']

def makeSummaryFromBreakdowns(tmod, modBaseDir = '/gpfs/home/mep22dku/scratch/ModelRuns/'):
    
    figDir = '/gpfs/data/greenocean/software/runs/modelMonitor/plots/'
    csvDir = '/gpfs/home/mep22dku/scratch/ModelRuns/modelBreakdownSummaries/'
    
    try:
        w = pd.read_csv(f'/{modBaseDir}/{tmod}/breakdown.sur.annual.dat', sep='\t')
        print('read1')
        year = w.year[2:-1].to_numpy().astype(float)
        Cflx_total = w.Cflx[2:-1].to_numpy().astype(float)
        Cflx_Arctic = w['Cflx.1'][2:-1].to_numpy().astype(float)
        Cflx_N_Atl = w['Cflx.2'][2:-1].to_numpy().astype(float)
        Cflx_N_Pac = w['Cflx.3'][2:-1].to_numpy().astype(float)
        Cflx_Equ_N = w['Cflx.4'][2:-1].to_numpy().astype(float)
        Cflx_Equ = w['Cflx.5'][2:-1].to_numpy().astype(float)
        Cflx_Equ_S = w['Cflx.6'][2:-1].to_numpy().astype(float)
        Cflx_SO_Atl = w['Cflx.7'][2:-1].to_numpy().astype(float)
        Cflx_SO_Pac = w['Cflx.8'][2:-1].to_numpy().astype(float)
        Cflx_SO_Ind = w['Cflx.9'][2:-1].to_numpy().astype(float)

        Cflx_SO = Cflx_SO_Atl + Cflx_SO_Pac + Cflx_SO_Ind
        Cflx_Equ_tot = Cflx_Equ_N + Cflx_Equ_S + Cflx_Equ
        Cflx_NANP = Cflx_N_Atl + Cflx_N_Pac

        w = pd.read_csv(f'/{modBaseDir}/{tmod}/breakdown.vol.annual.dat', sep='\t')
        print('read2')
        year = w.year[2:-1].to_numpy().astype(float)
        PPT_total = w.PPT[2:-1].to_numpy().astype(float)
        PPT_Arctic = w['PPT.1'][2:-1].to_numpy().astype(float)
        PPT_N_Atl = w['PPT.2'][2:-1].to_numpy().astype(float)
        PPT_N_Pac = w['PPT.3'][2:-1].to_numpy().astype(float)
        PPT_Equ_N = w['PPT.4'][2:-1].to_numpy().astype(float)
        PPT_Equ = w['PPT.5'][2:-1].to_numpy().astype(float)
        PPT_Equ_S = w['PPT.6'][2:-1].to_numpy().astype(float)
        PPT_SO_Atl = w['PPT.7'][2:-1].to_numpy().astype(float)
        PPT_SO_Pac = w['PPT.8'][2:-1].to_numpy().astype(float)
        PPT_SO_Ind = w['PPT.9'][2:-1].to_numpy().astype(float)

        PPT_SO = PPT_SO_Atl + PPT_SO_Pac + PPT_SO_Ind
        PPT_Equ_tot = PPT_Equ_N + PPT_Equ_S + PPT_Equ
        PPT_NANP = PPT_N_Atl + PPT_N_Pac


        ###
        w = pd.read_csv(f'/{modBaseDir}/{tmod}/breakdown.lev.annual.dat', sep='\t')

        year = w.year[2:-1].to_numpy().astype(float)
        EXP_total = w.EXP[2:-1].to_numpy().astype(float)
        EXP_Arctic = w['EXP.1'][2:-1].to_numpy().astype(float)
        EXP_N_Atl = w['EXP.2'][2:-1].to_numpy().astype(float)
        EXP_N_Pac = w['EXP.3'][2:-1].to_numpy().astype(float)
        EXP_Equ_N = w['EXP.4'][2:-1].to_numpy().astype(float)
        EXP_Equ = w['EXP.5'][2:-1].to_numpy().astype(float)
        EXP_Equ_S = w['EXP.6'][2:-1].to_numpy().astype(float)
        EXP_SO_Atl = w['EXP.7'][2:-1].to_numpy().astype(float)
        EXP_SO_Pac = w['EXP.8'][2:-1].to_numpy().astype(float)
        EXP_SO_Ind = w['EXP.9'][2:-1].to_numpy().astype(float)

        EXP_SO = EXP_SO_Atl + EXP_SO_Pac + EXP_SO_Ind
        EXP_Equ_tot = EXP_Equ_N + EXP_Equ_S + EXP_Equ
        EXP_NANP = EXP_N_Atl + EXP_N_Pac
        ####
        w = pd.read_csv(f'//{modBaseDir}/{tmod}/breakdown.ave.annual.dat', sep='\t')

        year = w.year[2:-1].to_numpy().astype(float)
        TChl_total = w.TChl[2:-1].to_numpy().astype(float)
        TChl_Arctic = w['TChl.1'][2:-1].to_numpy().astype(float)
        TChl_N_Atl = w['TChl.2'][2:-1].to_numpy().astype(float)
        TChl_N_Pac = w['TChl.3'][2:-1].to_numpy().astype(float)
        TChl_Equ_N = w['TChl.4'][2:-1].to_numpy().astype(float)
        TChl_Equ = w['TChl.5'][2:-1].to_numpy().astype(float)
        TChl_Equ_S = w['TChl.6'][2:-1].to_numpy().astype(float)
        TChl_SO_Atl = w['TChl.7'][2:-1].to_numpy().astype(float)
        TChl_SO_Pac = w['TChl.8'][2:-1].to_numpy().astype(float)
        TChl_SO_Ind = w['TChl.9'][2:-1].to_numpy().astype(float)

        TChl_SO = TChl_SO_Atl + TChl_SO_Pac + TChl_SO_Ind
        TChl_Equ_tot = TChl_Equ_N + TChl_Equ_S + TChl_Equ
        TChl_NANP = TChl_N_Atl + TChl_N_Pac
        print('read3')
        df = pd.DataFrame([year,TChl_total,TChl_Arctic,TChl_NANP,TChl_Equ_tot,TChl_SO,
                          PPT_total,PPT_Arctic,PPT_NANP,PPT_Equ_tot,PPT_SO,
                          EXP_total,EXP_Arctic,EXP_NANP,EXP_Equ_tot,EXP_SO,
                          Cflx_total,Cflx_Arctic,Cflx_NANP,Cflx_Equ_tot,Cflx_SO,
                          ]).T
        df.columns = ['year', 'TChl_total','TChl_Arctic','TChl_NANP','TChl_Equ_tot','TChl_SO',
                     'PPT_total','PPT_Arctic','PPT_NANP','PPT_Equ_tot','PPT_SO',
                     'EXP_total','EXP_Arctic','EXP_NANP','EXP_Equ_tot','EXP_SO',
                     'Cflx_total','Cflx_Arctic','Cflx_NANP','Cflx_Equ_tot','Cflx_SO',
                     ]
        df.wheremade = 'GRO2_FORCING_EXPERIMENT/breakdownSummary.ipynb'
        df.notes = 'everything is in PgC/yr except TChl, which is in 1/giga whatever that is'
        df.to_csv(f'{csvDir}{tmod}_breakdown.csv')
        print(f'made breakdown file {csvDir}{tmod}_breakdown.csv')
        
        ##figure 
        fact = 1.1
        fig, axs = plt.subplots(4,5, figsize=(12*fact, 8*fact), facecolor='w', edgecolor='k')
        axs = axs.ravel()

        ind = 0
        axs[0+ind].plot(year, Cflx_total); axs[0].set_title('Cflx PgCarbonPerYr \n full domain')
        axs[1+ind].plot(year, Cflx_Arctic); axs[1].set_title('Arctic')
        axs[2+ind].plot(year, Cflx_NANP); axs[2].set_title('N Atl + N Pac')
        axs[3+ind].plot(year, Cflx_Equ_tot); axs[3].set_title('Equ + Equ_N \n + Equ_S')
        axs[4+ind].plot(year, Cflx_SO); axs[4].set_title('S. Ocean \n (Atl+Pac+Ind)')

        ind = 5
        axs[0+ind].plot(year, PPT_total); axs[0+ind].set_title('PPT PgCarbonPerYr \n full domain')
        axs[1+ind].plot(year, PPT_Arctic); axs[1+ind].set_title('Arctic')
        axs[2+ind].plot(year, PPT_NANP); axs[2+ind].set_title('N Atl + N Pac')
        axs[3+ind].plot(year, PPT_Equ_tot); axs[3+ind].set_title('Equ + Equ_N \n + Equ_S')
        axs[4+ind].plot(year, PPT_SO); axs[4+ind].set_title('S. Ocean \n (Atl+Pac+Ind)')
        ind = 10
        axs[0+ind].plot(year, EXP_total); axs[0+ind].set_title('EXP PgCarbonPerYr \n full domain')
        axs[1+ind].plot(year, EXP_Arctic); axs[1+ind].set_title('Arctic')
        axs[2+ind].plot(year, EXP_NANP); axs[2+ind].set_title('N Atl + N Pac')
        axs[3+ind].plot(year, EXP_Equ_tot); axs[3+ind].set_title('Equ + Equ_N \n + Equ_S')
        axs[4+ind].plot(year, EXP_SO); axs[4+ind].set_title('S. Ocean \n (Atl+Pac+Ind)')
        ind = 15
        axs[0+ind].plot(year, TChl_total); axs[0+ind].set_title('TChl 1/giga \n full domain')
        axs[1+ind].plot(year, TChl_Arctic); axs[1+ind].set_title('Arctic')
        axs[2+ind].plot(year, TChl_NANP); axs[2+ind].set_title('N Atl + N Pac')
        axs[3+ind].plot(year, TChl_Equ_tot); axs[3+ind].set_title('Equ + Equ_N \n + Equ_S')
        axs[4+ind].plot(year, TChl_SO); axs[4+ind].set_title('S. Ocean \n (Atl+Pac+Ind)')

        plt.suptitle(tmod, fontsize = 15)
        plt.tight_layout()
        fig.savefig(f'{figDir}/{tmod}_summary.jpg')
        print(f'made summary figure {tmod}')
        
        
    except:
        print('something awry')
    
    
for model in tmodels:
    makeSummaryFromBreakdowns(model)