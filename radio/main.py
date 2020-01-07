#!/usr/bin/env python
'''The main Program runs the Data and Plot objects to read and plot the data
from the radiosonde'''

from data import *
from plot import Plot


def main():
    '''The main Program runs the Data and Plot objects to read and plot the
    data from the radiosonde.'''

    dat = Data('dats')
    pl = Plot(dat)

    pl.plot()


if __name__ == '__main__':
    main()
    
