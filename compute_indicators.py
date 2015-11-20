import numpy as np
import datetime
import talib
from talib.abstract import *

def get_indicators():
    gbpusd = np.loadtxt('DATA/filled_in_trades.csv',delimiter=",",skiprows=1,usecols=(2,3,4,5,6))
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
    return indicatorArray


def get_trades():
    #load trade decisions
    trade_decisions = np.loadtxt('DATA/filled_in_trades.csv',delimiter=",",skiprows=1,usecols=(7,))

    #create "trades"  matrix to encode trade decisions as one_hot vectors
    sells_ = [0]*len(trade_decisions)
    no_trades = [0]*len(trade_decisions)
    buys_ = [0]*len(trade_decisions)
    trades = np.vstack((sells_,no_trades,buys_))

    #encode decisions in "trades" matrix
    for entry in range(len(trade_decisions)):
        row = trade_decisions[entry]+1
        column = entry
        trades[row,column] = 1
        
    #encoding: buy=row2, none=row1, sell=row0
    #return encoded trades matrix
    return trades

