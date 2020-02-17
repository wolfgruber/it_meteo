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
    
    def __init__(self, filename, code):
        i = 0
        self.mean_time = 0
        self.mean_space = 0
        self.lat = []
        self.lon = []
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
            n = len(grib)//2
            for j in range(len(grib)):
                msg = ecc.GribMessage(grib)
                if msg.get('shortName') == code:
                    if i == 0:
                        self.lat = msg.get('distinctLatitudes')
                        self.lon = msg.get('distinctLongitudes')
                        self.name = msg.get('name')
                        self.values = np.empty(
                                (n, len(self.lat), len(self.lon)))
                        
                    self.values[i,:,:] = np.reshape(msg.get('values'),
                               (len(self.lat), len(self.lon)))
                    i = i + 1
                    
        return
    

    def comp_mean_space(self):
        mean = np.mean(self.values, axis=(1,2))
        std = np.std(self.values, axis=(1,2))
        return (mean, std)


    def comp_mean_time(self):
        return np.mean(self.values, axis=0)


    def get_time_mean(self):
        if self.mean_time == 0:
            self.mean_time = self.comp_mean_time()

        return self.mean_time


    def get_space_mean(self):
        if self.mean_space == 0:
            self.mean_space = self.comp_mean_space()

        return self.mean_space


    def get_coord(self):
        return (self.lat, self.lon)


    def get_date(self, idx):
        return self.values[idx,:,:]

    
def plot_global(dataobject):
    lat, lon = dataobject.get_coord()
    values = dataobject.get_time_mean()
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1, projection=ctp.crs.Mollweide())
        
    ax.contourf(lon, lat, values, transform=ctp.crs.PlateCarree(),
                cmap='nipy_spectral')
        
    ax.coastlines()
    ax.set_global()
    plt.show()
    return
    
if __name__ == '__main__':
    #da = Data('data/data.grib', 'tp')
    da = Data('data/data.grib', '2t')
    plot_global(da)