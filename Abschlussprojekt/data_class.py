'''The file classes.py containes the class Data, which loads and analyses
the meteorological data from the file filename.grib.'''

import numpy as np
import eccodes as ecc


class Data:
    '''The class Data loads data from the *.grib file and performs the desired 
    manipulations on it. A Data object is the used by the functions from the
    plot module to produce plots'''


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
                        self.name = msg.get('name')+' / '+msg.get('units')
                        self.sname = msg.get('shortName')
                        self.values = np.empty(
                                (n, len(self.lat), len(self.lon)))
                        
                    self.values[i,:,:] = np.reshape(msg.get('values'),
                               (len(self.lat), len(self.lon)))
                    i = i + 1

        return


    def comp_mean_space(self):
        '''
        Computes the mean with respect to space of the values of the Data
        object.

        Returns
        -------
        mean : np.array(dtype=float)
            time series with the spatial means for each month
        std : np.array(dtype=float)
            time series with the spatial standard deviations for each month

        '''
        mean = np.mean(self.values, axis=(1,2))
        std = np.std(self.values, axis=(1,2))
        return (mean, std)


    def comp_mean_time(self):
        '''
        Computes the mean with respect to space of the values of the Data
        object.

        Returns
        -------
        np.array(dtype=float)
            2x2 array containing the temporal means for each grid point

        '''
        return np.mean(self.values, axis=0)


    def ann_mean(self, anno):
        '''
        Computes the mean with respect to space of the values of the Data
        object for the given year.

        Parameters
        ----------
        anno : int
            year of interest

        Returns
        -------
        data : np.array(dtype=float)
            2x2 array containing the temporal means over the given year for
            each grid point

        '''
        time_idx = (anno - 1979) * 12 - 1
        data = np.mean(self.values[time_idx:time_idx+12,:,:], axis=0)
        
        return data


    def get_time_mean(self):
        '''
        Returnes the mean with respect to space of the values of the Data
        object. If the mean does not exist yet, it gets computed
        with comp_mean_time().

        Returns
        -------
        np.array(dtype=float)
            2x2 array containing the temporal means for each grid point

        '''
        if type(self.mean_time) == int:
            self.mean_time = self.comp_mean_time()

        return self.mean_time


    def get_space_mean(self):
        '''
        Returnes the mean with respect to space of the values of the Data
        object. If the mean does not exist yet, it gets computed
        with comp_mean_space().

        Returns
        -------
        mean : np.array(dtype=float)
            time series with the spatial means for each month
        std : np.array(dtype=float)
            time series with the spatial standard deviations for each month

        '''
        if self.mean_space == 0:
            self.mean_space = self.comp_mean_space()

        return self.mean_space


    def get_coord(self):
        '''
        Returns the coordinate grid to which the values of the Data object
        refer.

        Returns
        -------
        np.array(dtype=float)
            array of latitudes
        np.array(dtype=float)
            array of longitudes

        '''
        return (self.lat, self.lon)


    def get_name(self):
        '''
        Returns the name of the data with its unit.

        Returns
        -------
        str
            name of variable / unit

        '''
        return self.name


    def reduce_grid(self, inpt, lon_min, lon_max, lat_min, lat_max):
        '''
        Returns the data of inpt reduced to a grid with the borders lon_min,
        lon_max, lat_min, lat_max.

        Parameters
        ----------
        inpt : np.array(dtype=float)
            2x2 array on which the grid reduction is performed
        lon_min : float
            lower longitude boundary
        lon_max : float
            upper longitude boundary
        lat_min : float
            lower latitude boundary
        lat_max : float
            upper latitude boundary

        Returns
        -------
        data : np.array(dtype=float)
            values with reduced grid
        lat : np.array(dtype=float)
            array of latitudes for reduced grid
        lon : np.array(dtype=float)
            array of longitudes for reduced grid

        '''

        idx_lon_min = np.argmin(np.abs(self.lon - lon_min))
        idx_lon_max = np.argmin(np.abs(self.lon - lon_max))
        idx_lat_min = np.argmin(np.abs(self.lat - lat_min))
        idx_lat_max = np.argmin(np.abs(self.lat - lat_max))

        data = inpt[idx_lat_max:idx_lat_min,idx_lon_min:idx_lon_max]
        lat = self.lat[idx_lat_max:idx_lat_min]
        lon = self.lon[idx_lon_min:idx_lon_max]
        
        return (data, lat, lon)


    def get_season_mean(self, season):
        len_dta = self.values.shape
        j = 0
        data = np.zeros((len_dta[0]//4, len_dta[1], len_dta[2]))
        season_key = [[0, 1, 11], [2, 3, 4], [5, 6, 7], [8, 9, 10]]
        for i in range(len_dta[0]):
            key = i % 12 == season_key[season][0]
            key = key or i % 12 == season_key[season][1]
            key = key or i % 12 == season_key[season][2]
                
            if key:
                data[j,:,:] = self.values[i,:,:]
                j = j + 1
                
        data = np.mean(data, axis = 0)
        return data
    

    def get_mean_per_season(self):
        len_dta = self.values.shape
        data = []
        season_data = np.zeros((len_dta[0]//4, len_dta[1], len_dta[2]))
        for season in range(4):
            j = 0
            
            season_key = [[0, 1, 11], [2, 3, 4], [5, 6, 7], [8, 9, 10]]
            for i in range(len_dta[0]):
                key = i % 12 == season_key[season][0]
                key = key or i % 12 == season_key[season][1]
                key = key or i % 12 == season_key[season][2]
                
                if key:
                    season_data[j,:,:] = self.values[i,:,:]
                    j = j + 1
                
            data.append(np.mean(season_data, axis=(1,2)))
        return data
