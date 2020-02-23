'''The module main runs the functions from the module plot to create the data
plots.'''

from plot import *


if __name__ == '__main__':
    perc = Data('data/data.grib', 'tp')
    temp = Data('data/data.grib', '2t')
    #plot_mean_global(perc, temp)
    plot_time_series(perc, temp)
    #plot_austria(perc, temp, 2019)
    #plot_anomaly(perc, temp, 2019)
    #plot_season_mean(perc, temp)
    #plot_season_violin(perc)
    #plot_season_violin(temp)