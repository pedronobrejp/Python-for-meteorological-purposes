#!/usr/bin/env python

"""
  Function to plot data on map.
  The user provides:
     - the data
     - lat/lon information
     - the figure name
     - the title of the plot
"""

#-------------
# Load modules
#-------------
from netCDF4 import Dataset
import matplotlib.pyplot as plt            # pyplot module import
import numpy as np                         # Numpy import
import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap   # basemap import
import scipy.io as spio
import scipy.linalg as linalg
import scipy.fftpack as fft
import scipy.stats as stats
import sys

#----------------------
# Function for plotting
#----------------------
def bmContourPlot(var, lats, lons, figName, figTitle):
    plt.figure( )
    latLow  = lats[0]
    latHigh = lats[-1]
    lonLow  = lons[0]
    lonHigh = lons[-1]
#-----------------------
# plt.figure is optional
#-----------------------
    plt.figure(figsize=(8,8))
      
    m = Basemap(projection='mill',
                llcrnrlat=latLow,
                urcrnrlat=latHigh,
                llcrnrlon=lonLow,
                urcrnrlon=lonHigh,
                resolution='c')
    m.drawcoastlines(linewidth=2)
    m.drawcountries(linewidth=2)
    m.drawparallels(np.arange(latLow,latHigh+1,20.), 
                    labels=[True,False,False,False])
    m.drawmeridians(np.arange(lonLow,lonHigh+1,30.),
                    labels=[False,False,False,True])

    longrid,latgrid = np.meshgrid(lons,lats)

    # compute native map projection coordinates of lat/lon grid.
    x, y = m(longrid,latgrid)
    # contour data over the map.
    #m.contour(x,y,var,11,cmap=plt.cm.RdBu)
    m.contourf(x,y,var,11,cmap=plt.cm.RdBu)
    plt.title(figTitle)
    plt.colorbar(shrink=.7)
    plt.savefig(figName + '.png')
    plt.show()

