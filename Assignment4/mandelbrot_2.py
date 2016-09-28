from numpy import *
from PIL import Image
from progressbar import *

def mandelbrotchecker(x, y):
    c = complex(x, y)
    z = complex(0, 0)
    for x in arange(1001):
        sum = z * z + c
        if (abs(z) >= 2):
            return x * 10 % 255
        elif (x == 1000):
            return 255
        z = sum
x = arange(-2,2, step=.01)
y = arange(-2,2, step=.01)

im = Image.new("RGB", (x.size,y.size))

#for i in range(x.size):
#    for j in range(y.size):
#        color_value = (mandelbrotchecker(x[i], y[j]))
#        im.putpixel((i, j), (color_value, color_value, color_value))

counterx = 0
countery = 0

pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=x.size).start()

for i in nditer(x):
    for j in nditer(y):
        color_value = (mandelbrotchecker( x[counterx], y[countery]))
        im.putpixel((counterx, countery), (color_value, color_value, color_value))
        countery = countery + 1
        pbar.update(counterx)
    counterx += 1
    countery = 0

pbar.finish()

