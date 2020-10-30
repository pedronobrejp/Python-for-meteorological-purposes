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
fileName = dirName+'CFSv2.Prec.20201030.202011.nc'

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
# Extracting the rain variable
#------------------------------------
p = ncFid.variables['anom'][:]

#-------------
# Closing file
#-------------
ncFid.close()

#--------------------------
# Set the level of interest
# optional
#--------------------------
level = 0

#---------------
# Slice the data
#---------------
indexLat, indexLon = sliceLatLon(lat, lon, -40.0, 15.0, 275, 330)

nLat = lat[indexLat[0]:indexLat[-1]+1]
nLon = lon[indexLon[0]:indexLon[-1]+1]

precip = p[0,0,0,indexLat[0]:indexLat[-1]+1,indexLon[0]:indexLon[-1]+1]

#---------------------------
# Plot the mean and variance
#---------------------------

bmContourPlot(precip, nLat, nLon, 'fig_TempMeanSlice', 'Anomalia de Precipitação')

