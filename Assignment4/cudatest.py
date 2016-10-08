from numpy import *
from numba import cuda
import time
from PIL import Image

@cuda.jit
def bar(x,y):
    c = complex(x,y)
    print(x)

starttime = time.time()

presicion = 0.01
x = arange(-2,2, step=presicion)
y = arange(-2,2, step=presicion)


def thefractal(x,y):
    for i in range(x.size):
        print(i)
        for j in range(y.size):
            bar(x[i], y[j])


thefractal(x,y)

endtime= time.time()

print(endtime-starttime)


