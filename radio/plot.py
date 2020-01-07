'''The module plot contains the class Plot'''

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np


def plotmap(loc, name):
    '''Plot the location and the name of the weatherstation that launches
    the radiosonde. Gets called in the main program and appears in the
    documentation.'''

    fig = plt.figure(figsize=(12,8))

    m = Basemap(projection='cyl',
                llcrnrlon = loc[0]-12, llcrnrlat = loc[1]-12 % 90,
                urcrnrlon = loc[0]+12, urcrnrlat = loc[1]+12 % 90,
                resolution='l', area_thresh=10.)

    #set properites...
    parallels = np.arange(-90.,90.,10.0)
    m.drawparallels(parallels,labels=[True,False,False,True],fontsize=10)

    # draw meridians
    meridians = np.arange(-180.0,180.0,10.0)
    m.drawmeridians(meridians,labels=[True,False,False,True],fontsize=12)   

    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()

    m.etopo()

    loc = m(loc[0], loc[1])

    m.plot(loc[0], loc[1], 'bs', markersize=10)

    plt.text(loc[0]+0.25, loc[1]+0.25, name,size=10)

    plt.savefig('docs/build/html/loc.jpg')
    plt.close()
    
    return


class Plot:
    '''Class `Plot` plots the data from the radiosonde which gets passed py a
     `Data` object. The plot can be customized and be finally displayd with
     `Plot.plot()`'''
    
    # setting default height and width
    h = 4.8
    l = 6.4
    
    def __init__(self, data):
        '''Initializes the `Plot` object with data from the passed `Data` object.'''
        self.pres = data.get_pressure()
        self.temp = data.get_temp()
        self.dwpt = data.get_dwpt()
        self.loc = data.get_dest()
        
    def set_size(self, height, length):
        '''Sets height and width of the plot.'''
        self.h = height
        self.l = length
        
    def plot(self):
        '''Plots the plot.'''
        
        fig = plt.figure(figsize=(self.l, self.h))
        plt.plot(self.temp, self.pres, label='Temperature')
        plt.plot(self.dwpt, self.pres, label='Temperature of Dew Point')
        plt.ylim(max(self.pres), min(self.pres))
        plt.grid(True)
        plt.ylabel('Pressure/hPa')
        plt.xlabel('T/°C')
        plt.legend()
        plt.savefig('docs/build/html/plt.jpg')
        plt.show()

        plotmap(self.loc[0:2], self.loc[2])
        
        return

