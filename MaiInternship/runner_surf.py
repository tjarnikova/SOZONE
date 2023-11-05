#put python script here
import seawater
import numpy as np
import gsw
import pandas as pd

runhorse = True
if runhorse:

    tdir = '/gpfs/data/greenocean/observations/'
    glodap = pd.read_csv(f'{tdir}GLODAPv2.2022_Merged_Master_File.csv')
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    print('walrus!')
    print(glodap.head())

    tDIC = np.array(glodap['G2tco2'][:])
    tco2f = np.array(glodap['G2tco2f'][:])
    tco2qc = np.array(glodap['G2tco2qc'][:])

    tALK = np.array(glodap['G2talk'][:])
    talkf = np.array(glodap['G2talkf'][:])
    tco2f = np.array(glodap['G2tco2f'][:])

    print(np.unique(talkf))
    print(np.unique(tco2f))

    tSAL = np.array(glodap['G2salinity'][:])
    tTEMP = np.array(glodap['G2temperature'][:])
    tPRES = np.array(glodap['G2pressure'][:])
    tLAT = np.array(glodap['G2latitude'][:])
    tLON = np.array(glodap['G2longitude'][:])
    tYEAR = np.array(glodap['G2year'])
    tMONTH = np.array(glodap['G2month'])
    tBOTdepth = np.array(glodap['G2bottomdepth'][:])
    #tAOU = np.array(glodap['aou'][:])

    tSAL_SA = tSAL * (35.16504/35.000)
    dens = gsw.rho_t_exact(tSAL_SA,tTEMP,tPRES)

    
    print('density')
    print(np.nanmin(dens))
    print(np.nanmax(dens))
    tDIC=tDIC*dens/1000
    tALK=tALK*dens/1000


    tfilt = (tco2f < 9) & (talkf <9) & ~np.isnan(tDIC) & ~np.isnan(tALK) & (dens > 900) & (tPRES < 15) & (tYEAR > 1990) & (tBOTdepth > 1000) #surface observations
    print('new filter!')
    tDIC_SO = tDIC[tfilt]

    print(np.nanmin(tDIC_SO))
    tco2f_SO =  tco2f[tfilt]
    tco2qc_SO = tco2qc[tfilt]
    tALK_SO = tALK[tfilt]
    talkf_SO = talkf[tfilt]
    tco2f_SO = tco2f[tfilt]

    tSAL_SO = tSAL[tfilt]
    tTEMP_SO = tTEMP[tfilt]
    tPRES_SO = tPRES[tfilt]
    tLAT_SO = tLAT[tfilt]
    tLON_SO = tLON[tfilt]
    tYEAR_SO = tYEAR[tfilt]
    tMONTH_SO = tMONTH[tfilt]
    tBOTdepth_SO = tBOTdepth[tfilt]

    print(np.shape(tYEAR_SO))
    df = pd.DataFrame([tYEAR_SO,tMONTH_SO,tDIC_SO,tALK_SO,tSAL_SO,tTEMP_SO,tPRES_SO,tLAT_SO,tLON_SO, tBOTdepth_SO]).T
    # df = df.sort_values(by = tYEAR_SO)
    df.columns = ['YR', 'MONTH', 'DIC', 'ALK', 'SAL', 'TEMP', 'PRES', 'LAT', 'LON','BOTTOMdepth']
    df.to_csv('./GLODAPv2.2022_GLOBE_valid_DICTA_umolL_surface.csv')