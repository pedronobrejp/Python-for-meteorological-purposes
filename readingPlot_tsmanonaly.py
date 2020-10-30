#!/usr/bin/env python

#-------------
# Load modules
#-------------
from netCDF4 import Dataset
import numpy as np                         # Numpy import
import scipy.io as spio
import scipy.linalg as linalg
import scipy.fftpack as fft
import scipy.stats as stats
import sys
import salem

from bmContourModtsm import *



#----------------------
# Provide the file name
#----------------------
dirName  = '/Users/joaonobre/Downloads/'
fileName = dirName+'CFSv2.SST.20201030.202011.nc'

#------------------
# Opening the file
#------------------
ncFid = Dataset(fileName, mode='r')

#----------------------
# Extracting dimensions
#----------------------
lat  = ncFid.variables['LAT'][:]
lon  = ncFid.variables['LON'][:]

#------------------------------------
# Extracting the temperature variable
#------------------------------------
temp = ncFid.variables['anom'][:]

#-------------
# Closing file
#-------------
ncFid.close()

#--------------------------
# Set the level of interest
#--------------------------
level500 = 1

T = temp[0,0,0,:,:]  # time, lat, lon

#------------------------------
# Compute the mean and variance
#------------------------------

#T500mean = np.mean(T500,0)
#T500var  = np.var(T500,0)

#---------------------------
# Plot the mean and variance
#---------------------------

bmContourPlot(T, lat, lon, 'fig_TempMean', 'Anomalia de TSM')
#bmContourPlot(T,  lat, lon, 'fig_TempVariance', 'Variância da precipitação')

