from __future__ import (absolute_import, division, print_function)

# example showing how to use streamlines to visualize a vector
# flow field (from Hurricane Earl).  
# Requires matplotlib 1.1.1 or newer.
from netCDF4 import Dataset as NetCDFFile
from mpl_toolkits.basemap import Basemap, interp
import numpy as np
import matplotlib.pyplot as plt

if not hasattr(plt, 'streamplot'):
    raise ValueError('need newer version of matplotlib to run this example')

# H*wind data from http://www.aoml.noaa.gov/hrd/data_sub/wind.html
ncfile = NetCDFFile('/Volumes/JPNOBRE/dados/Teste_03/MERRA2_BK/3DVar/teste_gfs.nc')
udat = ncfile.variables['ua'][0,0,:,:]
vdat = ncfile.variables['va'][0,0,:,:]
tdat = ncfile.variables['ta'][0,0,:,:]
lons1 = ncfile.variables['longitude'][:]
lats1 = ncfile.variables['latitude'][:]
lat0 = lats1[len(lats1)//2]; lon0 = lons1[len(lons1)//2]
lons, lats = np.meshgrid(lons1,lats1)
ncfile.close()

# downsample to finer grid for nicer looking plot.
nlats = 2*udat.shape[0]; nlons = 2*udat.shape[1]
lons = np.linspace(lons1[0],lons1[-1],nlons)
lats = np.linspace(lats1[0],lats1[-1],nlats)
lons, lats = np.meshgrid(lons, lats)
udat = interp(udat,lons1,lats1,lons,lats)
vdat = interp(vdat,lons1,lats1,lons,lats)
tdat = interp(tdat,lons1,lats1,lons,lats)
speed = np.sqrt(udat**2+vdat**2)


fig = plt.figure(figsize=(8,8))
m = Basemap(projection='cyl',llcrnrlat=-20,llcrnrlon=-50,urcrnrlat=0,urcrnrlon=-30,resolution='i')
x, y = m(lons,lats)
m.drawmapboundary(fill_color='w')
m.drawcoastlines(linewidth=1)
m.drawcountries(linewidth=1)
m.drawstates(linewidth=1)
m.drawmeridians(np.arange(-50,-30,5),labels=[0,0,0,1])
m.drawparallels(np.arange(-20,0,5),labels=[1,0,0,0])

m.streamplot(x,y,udat,vdat,linewidth=2,density=2,color='black')
m.contourf(x,y,tdat,11,cmap=plt.cm.seismic)
m.colorbar()

plt.title('SCM 14/01/2017',\
        fontsize=13)
plt.show()
