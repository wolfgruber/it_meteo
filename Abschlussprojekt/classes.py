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


    def get_name(self):
        return self.name

    
def plot_mean_global(data1, data2):
    lat1, lon1 = data1.get_coord()
    values1 = data1.get_time_mean()
    name1 = data1.get_name()
    
    values2 = data2.get_time_mean()
    name2 = data2.get_name()
    if values1.shape == values2.shape:
        lat2 = lat1
        lon2 = lon1
    else:
        lat2, lon2 = data2.get_coord()
    
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1, projection=ctp.crs.Mollweide())
        
    m1 = ax1.contourf(lon1, lat1, values1, 15, transform=ctp.crs.PlateCarree(),
                cmap='nipy_spectral')
    
    m2 = ax1.contourf(lon2, lat2, values2, colors='none',
                 hatches=['/', 'x','//', 'xx', '///', 'xxx', '////', 'xxxx'],
                 transform=ctp.crs.PlateCarree())
        
    fig.colorbar(m1, orientation='horizontal')
    fig.colorbar(m2, orientation='horizontal')
    ax1.coastlines()
    ax1.set_global()
    plt.savefig('fig/mean_global.png')
    plt.show()
    return

def plot_time_series(dataobject1, dataobject2):
    values1, std1 = dataobject1.get_space_mean()
    name1 = dataobject1.get_name()
    values2, std2 = dataobject2.get_space_mean()
    name2 = dataobject2.get_name()
    time1 = range(len(values1))
    time2 = range(len(values2))
    
    fig, ax1 = plt.subplots()
    
    color = 'tab:blue'
    ax1.errorbar(time1, values1, yerr=std1, color=color)
    ax1.set_ylabel(name1, color=color)
    ax1.set_xlabel('months since Jan 1979')
    ax1.tick_params(axis='y', labelcolor=color)
    
    color = 'tab:orange'
    ax2 = ax1.twinx()
    ax2.errorbar(time2, values2, yerr=std2, color=color, alpha=0.8)
    ax2.set_ylabel(name2, color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    
    plt.show()
    return
    
if __name__ == '__main__':
    perc = Data('data/data.grib', 'tp')
    temp = Data('data/data.grib', '2t')
    plot_mean_global(perc, temp)
    #plot_time_series(perc, temp)