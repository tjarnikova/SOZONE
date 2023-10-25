import xarray as xr
import numpy as np

def weighted_quantile(values, quantiles, sample_weight=None, 
                      values_sorted=False, old_style=False):
    """ Very close to numpy.percentile, but supports weights.
    NOTE: quantiles should be in [0, 1]!
    :param values: numpy.array with data
    :param quantiles: array-like with many quantiles needed
    :param sample_weight: array-like of the same length as `array`
    :param values_sorted: bool, if True, then will avoid sorting of
        initial array
    :param old_style: if True, will correct output to be consistent
        with numpy.percentile.
    :return: numpy.array with computed quantiles.
    """
    values = np.array(values)
    quantiles = np.array(quantiles)
    if sample_weight is None:
        sample_weight = np.ones(len(values))
    sample_weight = np.array(sample_weight)
    assert np.all(quantiles >= 0) and np.all(quantiles <= 1), \
        'quantiles should be in [0, 1]'

    if not values_sorted:
        sorter = np.argsort(values)
        values = values[sorter]
        sample_weight = sample_weight[sorter]

    weighted_quantiles = np.cumsum(sample_weight) - 0.5 * sample_weight
    if old_style:
        # To be convenient with numpy.percentile
        weighted_quantiles -= weighted_quantiles[0]
        weighted_quantiles /= weighted_quantiles[-1]
    else:
        weighted_quantiles /= np.sum(sample_weight)
    return np.interp(quantiles, weighted_quantiles, values)



tdir = '/gpfs/data/greenocean/software/products/windsFromComponents/ERA5_v202303_rawdat/daily/'


for y in range(1940,2023):
    w = xr.open_dataset(f'{tdir}/10m_windspeed_ERA5_{y}-daily-rg.nc')
    savenam = f'{tdir}/10m_windspeed_ERA5_{y}_extremes.nc'
    tlen = (len(w.time))
    mask = xr.open_dataset('/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/PlankTOMmask_krg.nc')
    maskval = mask.aream2[10,:,:].values
    tmask = mask.aream2[10,0:40,:].values
    
    at95 = np.zeros([tlen])
    above95 = np.zeros([tlen])
    above95wt = np.zeros([tlen])

    for i in range(0,len(w.time)):
        twspd = w.windspeed[i,0:40,:]

        where0 = np.where(tmask == 0)
        twspd2 = np.copy(twspd)
        twspd2[np.where(tmask == 0)] = np.nan
        perc95 = weighted_quantile(np.ravel(twspd), 0.95, \
                                   sample_weight=np.ravel(tmask))
        at95[i] = perc95
        tmask2 = np.copy(tmask)
        s = twspd2[twspd2>perc95]
        q = np.where(twspd2 < perc95)
        tmask2[q] = 0
        above95wt[i] = np.average(np.ravel(twspd), weights = np.ravel(tmask2))
        above95[i] = np.nanmean(twspd2[twspd2>perc95])


    data_vars = {'at95':(['time'], at95,
    {'long_name':'weighted 95th percentile of winds'}),
                 'above95':(['time'], above95,
    {'long_name':'unweighted mean of all winds above 95th percentile'}),
                 'above95wt':(['time'], above95wt,
    {'long_name':'weighted mean of all winds above 95th percentile'}),

                }
    # define coordinates
    coords = {'time': (['time'], w.time),
            }
    # define global attributes
    attrs = {'made in':'SOZONE/MEDUSA/makeYearlyMEDUSAsubsetfiles.ipynb',
    'desc': 'yearly medusa files, saving only variables of interest'
    }
    ds = xr.Dataset(data_vars=data_vars,
    coords=coords,
    attrs=attrs)
    ds.to_netcdf(savenam)
