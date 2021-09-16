#!/usr/bin/env python

"""gfs_rainprecipitation_1.py: Plota arquivos do GFS pelo NOMADS."""

__author__      = "João Nobre"
__copyright__   = "Copyright 2009, Regional Modelling System Project"
__email__       = "joao.nobre@inpe.br"

# Pacotes para extrair dados via NOMADS OpenDAP
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import netCDF4

# Configura a figura
plt.figure()

# Local do GFS
mydate='20210916'
url='http://nomads.ncep.noaa.gov:80/dods/gfs_0p25/gfs'+mydate+'/gfs_0p25_00z'

# Extraindo os dados
file = netCDF4.Dataset(url)
lat  = file.variables['lat'][:]
lon  = file.variables['lon'][:]
data = file.variables['apcpsfc'][4:10,:,:]
file.close()

data = np.sum(data,0)

# Definindo tamanho da figura e o mapa 
fig = plt.figure(figsize=(10,10))

m=Basemap(projection='cyl',lat_ts=10,llcrnrlon=275, \
  urcrnrlon=330,llcrnrlat=-40,urcrnrlat=15, \
  resolution='i')

# Covertendo lat/lon para x/y
x, y = m(*np.meshgrid(lon,lat))

# Definindo as cores do campo
clevs = [0, 1, 2.5, 5, 7.5, 10, 15, 20, 30, 40,
         50, 70, 100, 150, 200, 250, 300, 400, 500, 600, 750]

cmap_data = [(1.0, 1.0, 1.0),
             (0.3137255012989044, 0.8156862854957581, 0.8156862854957581),
             (0.0, 1.0, 1.0),
             (0.0, 0.8784313797950745, 0.501960813999176),
             (0.0, 0.7529411911964417, 0.0),
             (0.501960813999176, 0.8784313797950745, 0.0),
             (1.0, 1.0, 0.0),
             (1.0, 0.6274510025978088, 0.0),
             (1.0, 0.0, 0.0),
             (1.0, 0.125490203499794, 0.501960813999176),
             (0.9411764740943909, 0.250980406999588, 1.0),
             (0.501960813999176, 0.125490203499794, 1.0),
             (0.250980406999588, 0.250980406999588, 1.0),
             (0.125490203499794, 0.125490203499794, 0.501960813999176),
             (0.125490203499794, 0.125490203499794, 0.125490203499794),
             (0.501960813999176, 0.501960813999176, 0.501960813999176),
             (0.8784313797950745, 0.8784313797950745, 0.8784313797950745),
             (0.9333333373069763, 0.8313725590705872, 0.7372549176216125),
             (0.8549019694328308, 0.6509804129600525, 0.47058823704719543),
             (0.6274510025978088, 0.42352941632270813, 0.23529411852359772),
             (0.4000000059604645, 0.20000000298023224, 0.0)]
cmap = mcolors.ListedColormap(cmap_data, 'precipitation')
norm = mcolors.BoundaryNorm(clevs, cmap.N)

m.contourf(x,y,data,clevs,cmap=cmap,norm=norm)
m.colorbar(location='bottom', pad=0.4)

# Definindo contorno do mapa

m.drawmapboundary(fill_color='w')
m.drawcoastlines(linewidth=1)
m.drawcountries(linewidth=1)
m.drawstates(linewidth=1)
m.drawparallels(np.arange(-40.,15.,15.),labels=[1,0,0,0])
m.drawmeridians(np.arange(-85,-30.,15.),labels=[0,0,0,1])

# Definindo nome, cor e plotando o mapa

title = f"GFS {mydate} Chuva Acumulada em 24 horas"
figure = f"/Users/joaonobre/Desktop/GFS_{mydate}_rain.png"
txt = "GitHub: https://github.com/pedronobrejp"
plt.title(title)
fig.text(.05,.05,txt)
fig1 = plt.gcf()
plt.draw()
fig1.savefig(figure, dpi=100)