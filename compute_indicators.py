import numpy as np
import datetime
import talib
from talib.abstract import *

def get_indicators():
    gbpusd = np.loadtxt('GBPUSD5.csv',delimiter=",",skiprows=1,usecols=(2,3,4,5,6))
    inputs = {
        'open'  : gbpusd[:,0],
        'high'  : gbpusd[:,1],
        'low'   : gbpusd[:,2],
        'close' : gbpusd[:,3],
        'volume': gbpusd[:,4]
    }
    moving_average_50  = np.array(EMA(inputs, timeperiod=50, price='close'))
    moving_average_200 = np.array(EMA(inputs, timeperiod=200,price='close'))
    slowk, slowd = np.array(STOCH(inputs, 5,3,0,3,0)) 
    bal_of_power = np.array(BOP(inputs))
    accum_dist = np.array(AD(inputs))
    indicatorArray = np.vstack((moving_average_50, moving_average_200, slowk, slowd, bal_of_power, accum_dist))
    print indicatorArray[:,60]
    return indicatorArray


'''    
print moving_average_50[60]
print moving_average_200[60]
print slowk[60]
print slowd[60]
print bal_of_power[60]
print accum_dist[60]

'''



