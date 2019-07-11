import ABC_investigation
import numpy as np

def test_logistic():
    print("Hi")

def test_t_zero():
    assert ABC_investigation.C_function(20, 5, 0, 5, np.array([0])) == np.array([5.0])

def test_r_zero():
    assert ABC_investigation.C_function(20, 0, 0, 5, np.array([5])) == np.array([5.0])

def test_k_zero():
    assert ABC_investigation.C_function(0, 5, 0, 7, np.array([12])) == np.array([0.0])

def test_large_t():
    assert np.abs(ABC_investigation.C_function(20, 5, 0, 5, np.array([100])) - np.array([20.0])) < 1e-6