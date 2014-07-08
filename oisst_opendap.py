__author__ = 'santiago'
# PSD/ERSL/NOAA OPeNDAP server
# http://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/

import netCDF4
#import pydap
#import urllib
import pylab
import matplotlib
import numpy as np
from opendap import opendap

oisst_url = r'http://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/noaa.oisst.v2/sst.mnmean.nc'

data = opendap(oisst_url)
gx = data.variables['lon'][:]
gy = data.variables['lat'][:]
gt = data.variables['time'][:]

raw_sst = data.variables['sst']

G = {}
G['x'] = gx[:].squeeze()
G['y'] = gy[:].squeeze()
G['t'] = gt[:].squeeze()

sst = raw_sst * raw_sst.scale_factor + raw_sst.add_offset

print raw_sst