import numpy as np
import datetime
import talib
from talib.abstract import *

gbpusd = np.loadtxt('GBPUSD5.csv',delimiter=",",skiprows=1,usecols=(2,3,4,5,6))
#print gbpusd[:,0]

inputs = {
    'open'  : gbpusd[:,0],
    'high'  : gbpusd[:,1],
    'low'   : gbpusd[:,2],
    'close' : gbpusd[:,3],
    'volume': gbpusd[:,4]
}

moving_average_50  = EMA(inputs, timeperiod=50, price='close')
moving_average_200 = EMA(inputs, timeperiod=200,price='close')
stoch_oscillator = 


print moving_average_50[48:54]
print moving_average_200[198:204]





