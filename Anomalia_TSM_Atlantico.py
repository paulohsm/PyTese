__author__ = 'santiago'

import netCDF4
#import pydap
#import urllib
import pylab
import matplotlib
import numpy as np
from opendap import opendap

url_grid = r'http://opendap.deltares.nl/thredds/dodsC/opendap/rijkswaterstaat/vaklodingen/vaklodingenKB116_4544.nc'
url_time = r'http://opendap.deltares.nl/thredds/dodsC/opendap/rijkswaterstaat/waterbase/concentration_of_suspended_matter_in_water/id410-DELFZBTHVN.nc'

# Get grid data
grid = opendap(url_grid)
G_x = grid.variables['x']
G_y = grid.variables['y']
G_z = grid.variables['z']

G = {}
G['x'] = G_x[:].squeeze()
G['y'] = G_y[:].squeeze()
G['z'] = G_z[1,:,:].squeeze()

# represent fillValue from data as Masked Array
# the next release of netcdf4 will return a masked array by default, handling NaNs
# correctly too (http://code.google.com/p/netcdf4-python/issues/detail?id=168)
G['z'] = np.ma.masked_invalid(G['z'])

# Get time series data
time = opendap(url_time)
T_t = time.variables['time']
T_z = time.variables['concentration_of_suspended_matter_in_water']

T = {}
T['t'] = netCDF4.num2date(T_t[:], units=T_t.units)
T['z'] = T_z[:].squeeze()

# plot grid data
matplotlib.pyplot.pcolormesh(G['x'], G['y'], G['z'])
pylab.xlabel('x [m]')
pylab.ylabel('y [m]')
matplotlib.pyplot.colorbar()
matplotlib.pyplot.axis('tight')
matplotlib.pyplot.axis('equal')
matplotlib.pyplot.title(url_grid)
pylab.savefig('vaklodingenKB116_4544')

# plot time series data
pylab.clf()
matplotlib.pyplot.plot_date(T['t'], T['z'], fmt='b-', xdate=True, ydate=False)
pylab.ylabel('SPM [kg/m3]')
matplotlib.pyplot.title(url_time)
pylab.savefig('DELFZBTHVN')