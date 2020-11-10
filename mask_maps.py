import xarray as xr 
import numpy as np
import regionmask
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings(action='ignore')

PATH_TO_SHAPEFILE = '/Users/joaonobre/Downloads/Brazilian_States_Shape/BRA_adm1.shp'
estados = gpd.read_file(PATH_TO_SHAPEFILE)
estados.head()

my_list = list(estados['ADM1'])
my_list_unique = set(list(estados['ADM1']))
indexes = [my_list.index(x) for x in my_list_unique]
      
data = '/Users/joaonobre/Downloads/datafiles/teste_wrf.nc'
ds = xr.open_mfdataset(data, chunks = {'time': 10})
ds

ds = ds.assign_coords(longitude=(((ds.longitude + 180) % 360) - 180)).sortby('longitude')
ds

a = range(0,estados.shape[0])
np.shape(a)

estados_mask_poly = regionmask.Regions_cls(name = 'ADM1', numbers = indexes, names = estados.ADM1[indexes], abbrevs = estados.ADM1[indexes], outlines = list(estados.geometry.values[i] for i in range(0,estados.shape[0])))
estados_mask_poly

mask = estados_mask_poly.mask(ds.isel(time = 0), lat_name='latitude', lon_name='longitude')
mask

plt.figure(figsize=(16,8))
ax = plt.axes()
mask.plot(ax = ax)
estados.plot(ax = ax, alpha = 0.8, facecolor = 'none', lw = 1)

mask_alagoas = mask.where(mask == 1)

plt.figure(figsize=(16,8))
ax = plt.axes()
mask_alagoas.plot(ax = ax)
estados.plot(ax = ax, alpha = 0.8, facecolor = 'none', lw = 1)
plt.show()

ID_COUNTRY = 1
print(estados.ADM1[ID_COUNTRY])
lat = mask.latitude.values
lon = mask.longitude.values

sel_mask = mask.where(mask == ID_COUNTRY).values
sel_mask

id_lon = lon[np.where(~np.all(np.isnan(sel_mask), axis=0))]
id_lat = lat[np.where(~np.all(np.isnan(sel_mask), axis=1))]
id_lat

out_sel1 = ds.sel(latitude = slice(id_lat[0], id_lat[-1]), longitude = slice(id_lon[0], id_lon[-1])).compute().where(mask == ID_COUNTRY)

out_sel2 = ds.where(mask == 1)
out_sel2

plt.figure(figsize=(12,8))
ax = plt.axes()
data = out_sel2.ta.isel(time = 0).plot(ax = ax, cmap="seismic", add_colorbar=False, vmax=2, vmin=10)
plt.colorbar(data, label="Temperatura [K]")
estados.plot(ax = ax, alpha = 0.8, facecolor = 'none')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()


plt.figure(figsize=(12,8))
ax = plt.axes()
data = out_sel1.ta.isel(time = 0).plot(ax = ax, cmap="seismic", add_colorbar=False)
plt.colorbar(data, label="Temperatura [K]")
estados.plot(ax = ax, alpha = 0.8, facecolor = 'none')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()