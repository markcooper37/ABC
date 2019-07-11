import numpy as np

def C_function(k, r, sigma, C_0, t):

    exponent = np.exp(-r * t)

    noise = np.random.normal(scale=sigma, size=len(t))

    return k / (1 + (-1 + (k / C_0))*exponent) + noise


if __name__ == "__main__":
    t_size = np.linspace(0, 4, 100)

    Results = C_function(150, 3, 2, 1, t_size)

    print(Results)

    import matplotlib.pyplot as plt
    plt.plot(t_size, Results)
    plt.show()