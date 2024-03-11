import pandas as pd
import numpy as np

import scipy.stats as stats
from pylab import *

import datetime as dt
from datetime import timedelta

# Create time

def set_time(inicio, fin, c_rate):
    
    """Defines time series to plot against data. The arguments "inicio" and "fin" muste be given  
    in datetime format, for example: inicio = dt.datetime(2017, 9, 3, 0, 0, 0) and 
    fin = dt.datetime(2017, 9, 14, 0, 0, 0). The c_rate allows to change the time series resolution."""
    
    seconds = (fin - inicio).total_seconds()
    delta = timedelta(minutes = c_rate)

    tiempo = []
    for i in range(0, int(seconds), int(delta.total_seconds())):
        tiempo.append(inicio + timedelta(seconds=i)) 
    print(f'Time starts on {inicio} and ends on {fin}')
    
    return tiempo
    


# Modify data resolution 

def counting_rate_modifier(x, c_rate, tiempo):
    
    """Modify resolution data resolution in x by specifying the desired counting rate (c_rate).
    Typically c_rate = 5 min or 10 min is prefered. It is assumed that data in x is already preprocessed"""
    
    if dtype(x) != float:
        x = x.astype(float)

    result = [sum(x[i : i + c_rate]) for i in range(0, len(x), c_rate)]
    result = pd.Series(result, index = tiempo)
    
    return result


# Normalize data

def counting_normalizer(x):
    
    """ Normalize counting rate percentage to 1 """
    
    normalized_x = 100*(x - x.mean())/x.mean()
    
    return normalized_x
