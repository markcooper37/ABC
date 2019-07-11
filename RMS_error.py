import ABC_investigation
import numpy as np
import math

def RMS_deviation(array_1, array_2):
    if array_1.size == array_2.size:
        square_difference = np.square(array_1 - array_2)
        sum_square = np.sum(square_difference)
        error = math.sqrt(sum_square / array_1.size)
        return error

if __name__ == "__main__":
    t_size = np.linspace(0, 4, 100)
    Results = ABC_investigation.C_function(150, 3, 2, 1, t_size)
    Results_2 = ABC_investigation.C_function(145, 3, 2, 1, t_size)
    print(RMS_deviation(Results, Results_2))