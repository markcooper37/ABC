import RMS_error
import ABC_investigation
import numpy as np

def test_equal():
    t_size = np.linspace(0, 4, 100)
    Results = ABC_investigation.C_function(150, 3, 2, 1, t_size)
    assert RMS_error.RMS_deviation(Results, Results) == 0.0

def test_diff():
    array_1 = np.array([1, 2, 3, 4, 5])
    array_2 = np.array([2, 1, 2, 5, 4])
    array_3 = np.array([3, 4, 1, 6, 7])
    assert RMS_error.RMS_deviation(array_1, array_2) == 1.0
    assert RMS_error.RMS_deviation(array_1, array_3) == 2.0