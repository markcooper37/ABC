import numpy

def C_function(k, r, sigma, C_0, t):

    e = numpy.exp(-r * t)

    noise = numpy.random.normal(scale=sigma, size=len(t))

    return k / (1 + (-1 + k / C_0))*e + noise

print(C_function(5, 3, 1, 7, numpy.linspace(0, 1, 10)))
