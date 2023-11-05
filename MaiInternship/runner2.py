#put python script here
import seawater
import numpy as np
import gsw
import pandas as pd
import netCDF4 as nc

def haversine(lon1, lat1, lon2, lat2):
    """Calculate the great-circle distance in kilometers between two points
    on a sphere from their longitudes and latitudes.
    Reference: http://www.movable-type.co.uk/scripts/latlong.html
    :arg lon1: Longitude of point 1.
    :type lon1: float or :py:class:`numpy.ndarray`
    :arg lat1: Latitude of point 1.
    :type lat1: float or :py:class:`numpy.ndarray`
    :arg lon2: Longitude of point 2.
    :type lon2: float or :py:class:`numpy.ndarray`
    :arg lat2: Latitude of point 2.
    :type lat2: float or :py:class:`numpy.ndarray`
    :returns: Great-circle distance between two points in km
    :rtype: float or :py:class:`numpy.ndarray`
    """
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km

def find_closest(lon1, lat1):
    w = nc.Dataset('/gpfs/data/greenocean/software/runs/TOM12_TJ_1ASA/ORCA2_1m_20500101_20501231_ptrc_T.nc')
    lats = (w['nav_lat'][:])
    lons = w['nav_lon'][:]
    km = haversine(lon1, lat1, lons, lats)
    q = (np.where(km == np.min(km)))
    tY = q[0][0]
    tX = q[1][0]

    return tY, tX

glodap = pd.read_csv('/gpfs/home/mep22dku/scratch/SOZONE/MaiInternship/GLODAPv2.2022_GLOBE_valid_DICTA_umolL.csv')

lat = np.array(glodap.LAT)
lon = np.array(glodap.LON)
tY = np.zeros_like(lat)
tX = np.zeros_like(lat)

for i in range(0,len(lat)):
    if i%1000 == 0:
        print(i)
    tY[i], tX[i] = find_closest(lon[i], lat[i])

glodap['tY'] = tY
glodap['tX'] = tX

glodap.to_csv('./GLODAPv2.2022_GLOBE_valid_DICTA_umolL_XY.csv')