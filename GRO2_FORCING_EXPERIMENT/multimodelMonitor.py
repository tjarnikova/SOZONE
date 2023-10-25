tmodels = ['TOM12_TJ_GPB0', 'TOM12_TJ_GNB0', 'TOM12_TJ_GPA1']
fignam = 'monitor_GPA1_GPB0_GNB0.jpg'
#comparing multiple model breakdowns made by /gpfs/data/greenocean/software/runs/modelMonitor/breakdownMonitor.py
#for models in tmodels, attempts to find the breakdowns in /gpfs/data/greenocean/software/runs/modelMonitor/summarycsv
# and saves figure showing progress of all models under //gpfs/data/greenocean/software/runs/modelMonitor/plots/{fignam}

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mods_to_plot = ['TOM12_TJ_GPB0', 'TOM12_TJ_GPA1', 'TOM12_TJ_GNB0']

def plot_sum(df, fig, axs, tcol = 'red', tlab = 'G101 (orig ERA)'):
    ind = 0
    axs[0+ind].plot(df.year, df.Cflx_total, color = tcol, label = tlab); 
    axs[1+ind].plot(df.year, df.Cflx_Arctic, color = tcol); 
    axs[2+ind].plot(df.year, df.Cflx_NANP, color = tcol); 
    axs[3+ind].plot(df.year, df.Cflx_Equ_tot, color = tcol); 
    axs[4+ind].plot(df.year, df.Cflx_SO, color = tcol); 
    ind = 5
    axs[0+ind].plot(df.year, df.PPT_total, color = tcol);
    axs[1+ind].plot(df.year, df.PPT_Arctic, color = tcol); 
    axs[2+ind].plot(df.year, df.PPT_NANP, color = tcol); 
    axs[3+ind].plot(df.year, df.PPT_Equ_tot, color = tcol); 
    axs[4+ind].plot(df.year, df.PPT_SO, color = tcol); 
    ind = 10
    axs[0+ind].plot(df.year, df.EXP_total, color = tcol); 
    axs[1+ind].plot(df.year, df.EXP_Arctic, color = tcol); 
    axs[2+ind].plot(df.year, df.EXP_NANP, color = tcol); 
    axs[3+ind].plot(df.year, df.EXP_Equ_tot, color = tcol); 
    axs[4+ind].plot(df.year, df.EXP_SO, color = tcol); 
    ind = 15
    axs[0+ind].plot(df.year, df.TChl_total, color = tcol); 
    axs[1+ind].plot(df.year, df.TChl_Arctic, color = tcol); 
    axs[2+ind].plot(df.year, df.TChl_NANP, color = tcol); 
    axs[3+ind].plot(df.year, df.TChl_Equ_tot, color = tcol); 
    axs[4+ind].plot(df.year, df.TChl_SO, color = tcol); 
    axs[0].legend()

def plot_summary(mods_to_plot, fignam = 'multimodel_monitor.jpg'):
    cols = ['r','b','g','y','k','c']
    fact = 1.6
    fig, axs = plt.subplots(4,5, figsize=(12*fact, 10*fact), facecolor='w', edgecolor='k')
    axs = axs.ravel()

    axs[0].set_title('Cflx PgCarbonPerYr \n full domain'); axs[1].set_title('Arctic'); axs[2].set_title('N Atl + N Pac')
    axs[3].set_title('Equ + Equ_N \n + Equ_S'); axs[4].set_title('S. Ocean \n (Atl+Pac+Ind)')
    ind = 5
    axs[0+ind].set_title('PPT PgCarbonPerYr \n full domain'); axs[1+ind].set_title('Arctic')
    axs[2+ind].set_title('N Atl + N Pac'); axs[3+ind].set_title('Equ + Equ_N \n + Equ_S'); axs[4+ind].set_title('S. Ocean \n (Atl+Pac+Ind)')
    ind = 10
    axs[0+ind].set_title('EXP PgCarbonPerYr \n full domain'); axs[1+ind].set_title('Arctic')
    axs[2+ind].set_title('N Atl + N Pac'); axs[3+ind].set_title('Equ + Equ_N \n + Equ_S'); axs[4+ind].set_title('S. Ocean \n (Atl+Pac+Ind)')
    ind = 15
    axs[0+ind].set_title('TChl 1/giga \n full domain'); axs[1+ind].set_title('Arctic')
    axs[2+ind].set_title('N Atl + N Pac'); axs[3+ind].set_title('Equ + Equ_N \n + Equ_S'); axs[4+ind].set_title('S. Ocean \n (Atl+Pac+Ind)')

    for q in range(0,len(mods_to_plot)):
        tmod = mods_to_plot[q]
        sumdir = '/gpfs/data/greenocean/software/runs/modelMonitor/summarycsv/'
        try: 
            modsum = pd.read_csv(f'{sumdir}{tmod}_breakdown.csv')
            plot_sum(modsum, fig, axs, tcol = cols[q], tlab = tmod)
            print('plotted')
        except:
            print(f'didnt find {tmod} in model summaries')


    axs[0].legend(loc = 'best')


    plt.tight_layout()
    fig.savefig(f'/gpfs/data/greenocean/software/runs/modelMonitor/plots/{fignam}')
    print('made multimodel figure')

    
plot_summary(mods_to_plot, fignam)