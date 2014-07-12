__author__ = 'santiago'

# para ler netcdf
# http://snowball.millersville.edu/~adecaria/ESCI386P/esci386-lesson14-Reading-NetCDF-files.pdf

# todos os comandos do matplotlib
# http://matplotlib.org/api/pyplot_summary.html

# trabalhando eixo do tempo
# http://schubert.atmos.colostate.edu/~cslocum/netcdf_example.html

# Matplotlib tutorial
# http://www.loria.fr/~rougier/teaching/matplotlib/

# Matplotlib In-depth
# http://www.astro.washington.edu/users/vanderplas/Astr599/notebooks/12_AdvancedMatplotlib

# formatando graficos
# http://www.astro.washington.edu/users/vanderplas/Astr599/notebooks/12_AdvancedMatplotlib

# How to name the ticks in a python matplotlib boxplot
# http://stats.stackexchange.com/questions/3476/how-to-name-the-ticks-in-a-python-matplotlib-boxplot

# para centralizar os rotulos dos meses entre os tics
# http://matplotlib.org/examples/pylab_examples/centered_ticklabels.html

from netCDF4 import Dataset
from numpy import *
#from matplotlib.pyplot import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pylab
from matplotlib.dates import date2num
from datetime import datetime, timedelta

# Loading data
act_sst_file = "OISST_AtlanticColdTongue.nc"
act_sst_data = Dataset(act_sst_file, 'r')
#for var in act_sst_data.variables:
#    print var

# Variables
sst = act_sst_data.variables['SST_ACT'][1:385]
tax = act_sst_data.variables['TIME'][1:385]

# Time axis
#starttime=act_sst_data.variables['TIME'].time_origin



#sstm = empty([32, 12], dtype='float')

#sstm = sst.reshape([32, 12])
sstm = reshape(sst, (32,12))
#for idx in range(12):
#    print sstm[1,idx] - sst[idx+12]
sstt = transpose(sstm)
msst = mean(sstt, 1)
#rsst = transpose(vstack((sstm, sstm)))

#sst2 = [msst msst]

#for yr in range(32):
#    for mon in range(12):
#        tt = mon * yr
#        sstm[yr,mon] = sst[tt]

#print sst[:]
#print tax

# The Plot

#plot(sst[1:384], linewidth=2.0)
fig, ax = plt.subplots()
fig = plt.plot(msst[:], color='red', linestyle='-', linewidth=2.0)
fig = plt.plot(sstt[:,:], 'x', color='black')
fig = plt.ylabel('Temperatura mensal media (deg C)')
fig = plt.xlabel('Mes')
fig = ax.xaxis.grid(True, which='major')

fig = plt.axes()
fig = plt.autoscale(enable=True, axis='x', tight=None)

month_labels = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']
fig = pylab.xticks(range(12), month_labels)
#ax.xaxis.set_major_formatter(plt.FixedFormatter(month_labels))
ax.xaxis.set_minor_formatter(plt.FixedFormatter(month_labels))
fig = plt.tick_params(axis='x', which='minor', bottom='off', top='off', labelbottom='off')
#fig = plt.set_xticks
fig = plt.xlim(-1.0,12.0)
#label = plt.axes.yaxis.get_major_ticks()[2].label
#print label

#ax.xaxis.set_major_locator(dates.MonthLocator())
#ax.xaxis.set_major_formatter(ticker.NullFormatter())

fig = ticker.AutoLocator()

for tick in ax.xaxis.get_minor_ticks():
    tick.tick1line.set_markersize(0)
    tick.tick2line.set_markersize(0)
    tick.label1.set_horizontalalignment('center')

plt.savefig('OISST_AtlanticColdTongue.png')
plt.show()

#  Make another plot, simpler, cleaner, repeating the annual cycle
rsst = vstack((sstt, sstt)) # [r]epeated [sst]
two_years = hstack((month_labels, month_labels))

fig2, ax2 = plt.subplots()
fig2 = plt.plot(rsst[:,:], 'x', color='black')
fig2 = plt.ylabel('Temperatura mensal media (deg C)')
fig2 = plt.xlabel('Mes')
fig2 = ax.xaxis.grid(True, which='major')
fig2 = pylab.xticks(range(24), two_years)
fig2 = plt.autoscale(enable=True, axis='x', tight=None)
fig2 = plt.xlim(-1.0,24.0)
fig2 = plt.savefig('OISST_AtlanticColdTongue.png')
fig2 = plt.show()

#plt.axis(tax[:])