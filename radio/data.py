'''Module data contains the class Data and some functions to read and prepare
data from the radiosonde.'''

import numpy as np
import pandas as pd


def read_tab(filename):
    '''Read the information from the *filename* file and returns it in a way
    the Data class can handle it.'''
    n = ['PRES', 'HGHT', 'TEMP', 'DWPT', 'RELH', 'MIXR', 'DRCT', 'SKNT',
         'THTA', 'THTE', 'THTV']

    data = pd.read_csv(filename, sep=' ', names = n,  skipfooter=27,
                       skiprows=10, skipinitialspace=True, engine='python')
    
    file = open(filename)
    lines=file.readlines()
    st_lon = lines[-20]
    st_lat = lines[-21]
    st_name = lines[1]
    file.close()
    
    dest = [st_lon, st_lat, st_name]
    
    return data, dest

class Data:
    '''Class Data reads and prepares the radiosonde data and returns it to
    class Plot for plotting'''
    
    def __init__(self, filename):
        self.raw, self.dest = read_tab(filename)
        self.dest[0] = float((self.dest[0][45:])[:-2])
        self.dest[1] = float((self.dest[1][45:])[:-2])
        self.dest[2] = self.dest[2][:-19]
        
    def get_pressure(self):
        '''Return the pressure as a numpy file. Function gets called by the
        initialisation of a Plot object.'''
        return self.raw['PRES'].to_numpy()
    
    def get_temp(self):
        '''Return the temperature as a numpy file. Function gets called by the
        initialisation of a Plot object.'''
        return self.raw['TEMP'].to_numpy()
    
    def get_dwpt(self):
        '''Return the dewpoint as a numpy file. Function gets called by the
        initialisation of a Plot object.'''
        return self.raw['DWPT'].to_numpy()
        
    def get_dest(self):
        '''Return destination and name of the weater atation that launched
        the radiosonde.'''
        return self.dest
        
    
