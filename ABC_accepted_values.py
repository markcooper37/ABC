import ABC_investigation
import RMS_error
import numpy as np
import matplotlib.pyplot as plt

def accepted_values(N, delta):
    C_0 = 1
    t_size = np.linspace(0, 4, 100)
    Results = ABC_investigation.C_function(150, 3, 2, C_0, t_size)
    k_estimate = []
    r_estimate = []
    sigma_estimate = []
    for i in range(N):
        random = [np.random.uniform(100, 200), np.random.uniform(0, 10), np.random.uniform(0, 5)]
        function_guess = ABC_investigation.C_function(random[0], random[1], random[2], C_0, t_size)
        error = RMS_error.RMS_deviation(function_guess, Results)
        if error < delta:
            k_estimate.append(random[0])
            r_estimate.append(random[1])
            sigma_estimate.append(random[2])
    print(len(k_estimate) / N)
    return [k_estimate, r_estimate, sigma_estimate]

value_guesses = accepted_values(100000, 5)

print(value_guesses)

for i in range(3):
    plt.subplot(3, 1, i + 1)
    plt.hist(value_guesses[i])

plt.show()