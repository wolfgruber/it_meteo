'''The file classes.py containes the two classes Data and Plot, which work
together to load, analyse and plot the meteorological data from the file
filename.grib.'''

import numpy as np
import matplotlib.pyplot as plt
import eccodes as ecc
import cartopy as ctp


class Data:
    '''The class Data loads data from the *.grib file and performs the desired 
    manipulations on it. An Data object is the used to initialize a Plot
    object.'''
    
    def __init__(self, filename):
        '''grb = ecc.GribFile(filename)
        msg = ecc.GribMessage(grb)
        self.name = msg.get('name')
        self.lat = msg.get('distinctLatitudes')
        self.lon = msg.get('distinctLongitudes')
        #self.lat = msg.get('latitudes')
        #self.lon = msg.get('longitudes')
        self.values = np.reshape(msg.get('values'), (len(self.lat), len(self.lon)))
        return'''
        with ecc.GribFile(filename) as grib:
            for i in range(len(grib)):
                msg = ecc.GribMessage(grib)
                print(msg.get('name'))
        
    def get_values(self):
        return self.values
    
    def get_coord(self):
        return (self.lat, self.lon)
        
        
        
class Plot:
    '''The class Plot takes a Data object and plots the data with cartopy.'''
    
    
    def __init__(self, dataobject, name):
        self.name = name
        self.title = dataobject.name
        self.values = dataobject.get_values()
        self.lat, self.lon = dataobject.get_coord()
        #print('len(lat)', len(self.lat))
        #print('len(lon)', len(self.lon))
        return
    
    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1, projection=ctp.crs.Mollweide())
        
        ax.contourf(self.lon, self.lat, self.values, transform=ctp.crs.PlateCarree(),
                    cmap='nipy_spectral')
        
        ax.coastlines()
        ax.set_global()
        plt.show()
        return
    
if __name__ == '__main__':
    da = Data('data/data.grib')
    #pl = Plot(da, 'first plot')
    #pl.plot()