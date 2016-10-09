from numpy import *
from PIL import Image
from progressbar import *
import time

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




def createMandelbrot(startx = -2.0,endx = 2.0,starty = -2.0,endy = 2.0):

    stattime = time.time()

    x = arange(startx,endx, step=.01)
    y = arange(starty,endy, step=.01)

    im = Image.new("RGB", (x.size,y.size))
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
    im.save("mandelbrot_2.png", "PNG")
    endtime = time.time()

    print ("\n total time:")
    print(endtime-stattime)

