__author__ = 'santiago'

# para ler netcdf
# http://snowball.millersville.edu/~adecaria/ESCI386P/esci386-lesson14-Reading-NetCDF-files.pdf

# todos os comandos do matplotlib
# http://matplotlib.org/api/pyplot_summary.html

# trabalhando eixo do tempo
# http://schubert.atmos.colostate.edu/~cslocum/netcdf_example.html

# para centralizar os rotulos dos meses entre os tics
# http://matplotlib.org/examples/pylab_examples/centered_ticklabels.html

from netCDF4 import Dataset
from numpy import *
from matplotlib.pyplot import *
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
starttime=act_sst_data.variables['TIME'].time_origin
print starttime
#X = [date2num(datetime())]

#sstm = empty([32, 12], dtype='float')

#sstm = sst.reshape([32, 12])
sstm = reshape(sst, (32,12))
#for idx in range(12):
#    print sstm[1,idx] - sst[idx+12]
sstt = transpose(sstm)

#for yr in range(32):
#    for mon in range(12):
#        tt = mon * yr
#        sstm[yr,mon] = sst[tt]

#print sst[:]
#print tax

#plot(sst[1:384], linewidth=2.0)
plot(sstt[:,:], '.')
ylabel('Temperatura mensal media (deg C)')
xlabel('Mes')
grid(True)

axes()
autoscale(enable=True, axis='x', tight=None)

savefig('OISST_AtlanticColdTongue.png')
show()

#plt.axis(tax[:])