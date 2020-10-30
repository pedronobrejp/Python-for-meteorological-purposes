#!/usr/bin/env python

"""
  Function for extracting a subset of
  Lat/Lon indices.
  Given lat and lon arrays latitudes and longitudes, 
  we want to determine the arrays inxdex_lat and
  index_lon of indices where the latitudes and longitudes
  fall in provided ranges ([minLat,maxLat] and [minLon,maxLon])

        lat[:]>=minLat and lat[:]<=maxLat
        lon[:]>=minLon and lon[:]<=maxLon
"""

#-------------
# Load modules
#-------------
import numpy as np                         # Numpy import

def sliceLatLon(lats, lons, minLat,maxLat,minLon,maxLon):
    indexLat = np.nonzero((lats[:]>=minLat) & (lats[:]<=maxLat))[0]
    indexLon = np.nonzero((lons[:]>=minLon) & (lons[:]<=maxLon))[0]
    return indexLat, indexLon

