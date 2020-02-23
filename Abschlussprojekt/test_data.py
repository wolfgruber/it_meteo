'''Test module for the Data class. Can be executed with pytest.'''

from data_class import Data
import numpy as np


def test_data():
    obj = Data('data/data.grib', '2t')
    obj.values = np.arange(100*24)
    obj.values = np.reshape(obj.values, (24, 10,10))
    obj.lat = np.arange(9, -1, -1)
    obj.lon = np.arange(10)
    obj.name = 'test'
    
    assert np.mean(obj.ann_mean(1979)) == 599.5
    
    assert np.mean(obj.get_time_mean()) == 1199.5
    
    assert np.mean(obj.get_space_mean()) == 614.1830350238611
    
    lat, lon = obj.get_coord()
    assert np.array_equal(lat, np.arange(9, -1, -1))
    assert np.array_equal(lon, np.arange(10))
    
    assert obj.get_name() == 'test'
    
    data, lat, lon = obj.reduce_grid(obj.values, 4, 6, 4, 6)
    assert np.mean(data) == 399.5
    
    assert np.mean(obj.get_mean_per_season()) == 1199.5

