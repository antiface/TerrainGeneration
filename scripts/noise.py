import math
import numpy
import matplotlib
import pylab

def noise(seed):
    # returns floating point numbers between -1.0 and 1.0
    x = (seed << 13) ** seed
    return 1.0 - ((x * (x*x*15731 + 789221) + 1376312589) & 0x7fffffff) / 1073741824.0

def linear_interpolate(a, b, x):
    return a * (1 - x) + b*x

def cosine_interpolate(a, b, x):
    f = (1 - cos(math.pi*x)) / 2
    return a * (1 - f) + b*f

if __name__ == '__main__':
    seed = 0
    x = range(10)
    y = [noise(n) for n in x]
    print y
    matplotlib.pyplot.show()
    print matplotlib.pyplot.plot(y)