'''This module contains functions to plot the data loaded and analysed with
the Data class.'''


import matplotlib.pyplot as plt
import cartopy as ctp
import seaborn as srs

from data_class import Data


def plot_mean_global(data1, data2):
    '''
    Creates a plot with thwe mean with respect to time of two datasets. The
    plot is saved in "fig/mean_lobal.png".

    Parameters
    ----------
    data1 : Data object
        data for the colorplot
    data2 : Data object
        data for the hatched plot

    Returns
    -------
    None.

    '''
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

    fig = plt.figure(dpi=250)
    ax1 = fig.add_subplot(1, 1, 1, projection=ctp.crs.Mollweide())

    m1 = ax1.contourf(lon1, lat1, values1, 15,
                      transform=ctp.crs.PlateCarree(), cmap='nipy_spectral')

    m2 = ax1.contourf(lon2, lat2, values2, colors='none',
                      hatches=['/', 'x', '//', 'xx', '///',
                               'xxx', '////', 'xxxx'],
                      transform=ctp.crs.PlateCarree())

    cbar1 = fig.colorbar(m1, orientation='horizontal', shrink=0.7)
    cbar1.ax.set_xlabel(name1)
    cbar2 = fig.colorbar(m2, orientation='horizontal', shrink=0.7)
    cbar2.ax.set_xlabel(name2)
    ax1.coastlines()
    ax1.set_global()
    plt.savefig('fig/mean_global.png')
    plt.show()
    #return


def plot_time_series(data1, data2):
    '''
    Creates a plot with the spatial means of two datasets. The plot is saved
    in "fig/time_series.png"

    Parameters
    ----------
    data1 : Data object
        data for the first plot (blue)
    data2 : Data object
        data for the second plot (orange)

    Returns
    -------
    None.

    '''
    values1, std1 = data1.get_space_mean()
    name1 = data1.get_name()
    values2, std2 = data2.get_space_mean()
    name2 = data2.get_name()
    time1 = range(len(values1))
    time2 = range(len(values2))

    fig, ax1 = plt.subplots(dpi=250)

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

    plt.savefig('fig/time_series.png')
    plt.show()
    #return


def plot_austria(data1, data2, anno):
    '''
    Creates a plot with the temporally averaged datasetd for a given year of
    two Data objects in Europe within the boundaries of map_border. The plot
    is saved at "fig/austria_[year].png"

    Parameters
    ----------
    data1 : Data object
        data for the colored plot
    data2 : Data object
        data for the hatched plot
    anno : int
        year of interest

    Returns
    -------
    None.

    '''
    map_border = [9, 17.5, 46, 49.5]
    values1, lat1, lon1 = data1.reduce_grid(data1.ann_mean(anno), *map_border)
    name1 = data1.get_name()
    values2, lat2, lon2 = data2.reduce_grid(data2.ann_mean(anno), *map_border)
    name2 = data2.get_name()

    fig = plt.figure(dpi=250)
    ax1 = fig.add_subplot(1, 1, 1, projection=ctp.crs.EuroPP())
    ax1.set_extent(map_border, crs=ctp.crs.PlateCarree())

    map1 = ax1.contourf(lon1, lat1, values1, 10,
                        transform=ctp.crs.PlateCarree(), cmap='nipy_spectral')

    map2 = ax1.contourf(lon2, lat2, values2, colors='none',
                        hatches=['/', 'x', '//', 'xx', '///',
                                 'xxx', '////', 'xxxx'],
                        transform=ctp.crs.PlateCarree())

    ax1.add_feature(ctp.feature.BORDERS.with_scale('10m'))
    cbar1 = fig.colorbar(map1, orientation='vertical', pad=0.1, shrink=0.7)
    cbar1.ax.set_ylabel(name1)
    cbar2 = fig.colorbar(map2, orientation='vertical', shrink=0.7)
    cbar2.ax.set_ylabel(name2)
    ax1.coastlines()
    plt.title('Annual mean in the year '+str(anno)+' over Austria')
    plt.savefig('fig/austria_'+str(anno)+'.png')
    plt.show()
    #return


def plot_anomaly(data1, data2, anno):
    '''
    Creates a plot with the deviation of the data from a given year from the
    temporal mean. The plot is saved at "fig/anomaly_[year].plt".

    Parameters
    ----------
    data1 : Data object
        data for the colored plot
    data2 : Data object
        data for the hatched plot
    anno : int
        year of interest

    Returns
    -------
    None.

    '''
    lat1, lon1 = data1.get_coord()
    mean1 = data1.get_time_mean()
    name1 = data1.get_name()

    mean2 = data2.get_time_mean()
    name2 = data2.get_name()
    if mean1.shape == mean2.shape:
        lat2 = lat1
        lon2 = lon1
    else:
        lat2, lon2 = data2.get_coord()

    values1 = data1.ann_mean(anno)
    values2 = data2.ann_mean(anno)
    values1 = mean1 - values1
    values2 = mean2 - values2

    fig = plt.figure(dpi=250)
    ax1 = fig.add_subplot(1, 1, 1, projection=ctp.crs.Mollweide())

    ma1 = ax1.contourf(lon1, lat1, values1, 17,
                       transform=ctp.crs.PlateCarree(), cmap='nipy_spectral')

    ma2 = ax1.contourf(lon2, lat2, values2, colors='none',
                       hatches=['/', 'x', '//', 'xx', '///',
                                'xxx', '////', 'xxxx'],
                       transform=ctp.crs.PlateCarree())

    cbar1 = fig.colorbar(ma1, orientation='horizontal', shrink=0.7)
    cbar1.ax.set_xlabel(name1, size=10)
    cbar1.ax.tick_params(labelsize=7.5)
    cbar2 = fig.colorbar(ma2, orientation='horizontal', shrink=0.7)
    cbar2.ax.set_xlabel(name2)
    ax1.coastlines()
    ax1.set_global()
    plt.savefig('fig/anomaly_'+str(anno)+'.png')
    plt.show()
    #return


def plot_season_mean(data1, data2):
    season_key = ['winter', 'spring', 'summer', 'autumn']
    for i in range(4):
        lat1, lon1 = data1.get_coord()
        mean1 = data1.get_season_mean(i)
        name1 = data1.get_name()

        mean2 = data2.get_season_mean(i)
        name2 = data2.get_name()
        if mean1.shape == mean2.shape:
            lat2 = lat1
            lon2 = lon1
        else:
            lat2, lon2 = data2.get_coord()

        fig = plt.figure(dpi=250)
        ax1 = fig.add_subplot(1, 1, 1, projection=ctp.crs.Mollweide())

        ma1 = ax1.contourf(lon1, lat1, mean1, 17,
                           transform=ctp.crs.PlateCarree(), cmap='nipy_spectral')

        ma2 = ax1.contourf(lon2, lat2, mean2, colors='none',
                           hatches=['/', 'x', '//', 'xx', '///',
                                    'xxx', '////', 'xxxx'],
                           transform=ctp.crs.PlateCarree())

        cbar1 = fig.colorbar(ma1, orientation='horizontal', shrink=0.7)
        cbar1.ax.set_xlabel(name1, size=10)
        cbar1.ax.tick_params(labelsize=7.5)
        cbar2 = fig.colorbar(ma2, orientation='horizontal', shrink=0.7)
        cbar2.ax.set_xlabel(name2)
        ax1.coastlines()
        ax1.set_global()
        plt.savefig('fig/season_'+season_key[i]+'.png')
        plt.show()
    

def plot_season_violin(data):
    season_key = ['winter', 'spring', 'summer', 'autumn']
    name = data.get_name()
    mean = data.get_mean_per_season()
    
    plt.figure(dpi=250)
    ax = srs.violinplot(data=mean)
    ax.set(xticklabels=season_key, ylabel=name)
    plt.savefig('fig/violin_'+str(data.sname)+'.png')
    plt.show()


if __name__ == '__main__':
    perc = Data('data/data.grib', 'tp')
    temp = Data('data/data.grib', '2t')
    #plot_mean_global(perc, temp)
    #plot_time_series(perc, temp)
    #plot_austria(perc, temp, 2019)
    #plot_anomaly(perc, temp, 2019)
    #plot_season_mean(perc, temp)
    plot_season_violin(temp)
    