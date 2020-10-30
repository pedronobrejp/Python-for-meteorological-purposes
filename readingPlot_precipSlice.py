#!/usr/bin/env python

########################## Correção de bug ##########################
# Este arquivo foi modificado pois havia erros de sintaxe,
# para correção o script subLatLonMod.py foi corrigido pa- 
# ra as seguintes linhas de comando 
# def sliceLatLon(lats, lons, minLat,maxLat,minLon,maxLon):
#    indexLat = np.nonzero((lats[:]>=minLat) & (lats[:]<=maxLat))[0]
#    indexLon = np.nonzero((lons[:]>=minLon) & (lons[:]<=maxLon))[0].
# Enquanto que para o presente script foi adaptado para as
# seguintes linhas
# indexLat, indexLon = sliceLatLon(lat, lon, -40.0, 15.0, 275, 330)
#
# nLat = lat[indexLat[0]:indexLat[-1]+1]
# nLon = lon[indexLon[0]:indexLon[-1]+1]
#
# Adaptado por: João Pedro Nobre
# Instituição: CPTEC/INPE
#####################################################################

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

from bmContourMod import *
from subLatLonMod import *


#----------------------
# Provide the file name
#----------------------
dirName  = '/Users/joaonobre/Downloads/'
fileName = dirName+'teste.nc'

#------------------
# Opening the file
#------------------
ncFid = Dataset(fileName, mode='r')

#----------------------
# Extracting dimensions
#----------------------
time = ncFid.variables['time'][:]
lev  = ncFid.variables['z'][:]
lat  = ncFid.variables['latitude'][:]
lon  = ncFid.variables['longitude'][:]

#------------------------------------
# Extracting the rain variable
#------------------------------------
p = ncFid.variables['precip'][:]

#-------------
# Closing file
#-------------
ncFid.close()

#--------------------------
# Set the level of interest
#--------------------------
level500 = 0

#---------------
# Slice the data
#---------------
indexLat, indexLon = sliceLatLon(lat, lon, -40.0, 15.0, 275, 330)

nLat = lat[indexLat[0]:indexLat[-1]+1]
nLon = lon[indexLon[0]:indexLon[-1]+1]

precip = p[:,level500,indexLat[0]:indexLat[-1]+1,indexLon[0]:indexLon[-1]+1]
#T500 = temp[:,level500,:,:]  # time, lat, lon

#------------------------------
# Compute the mean and variance
#------------------------------

precipmean = np.mean(precip,0)
precipvar  = np.var (precip,0)


#nT500mean = T500mean[indexLat[0]:indexLat[-1]+1, indexLon[0]:indexLon[-1]+1]
#nT500var  =  T500var[indexLat[0]:indexLat[-1]+1, indexLon[0]:indexLon[-1]+1]

#---------------------------
# Plot the mean and variance
#---------------------------

bmContourPlot(precipmean, nLat, nLon, 'fig_TempMeanSlice', 'Média do Campo')
bmContourPlot(precipvar,  nLat, nLon, 'fig_TempVarianceSlice', 'Variância do Campo')
