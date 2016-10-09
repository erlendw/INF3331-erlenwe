##"pure" python implementation
##todo set your own range
from PIL import Image
import time
import numpy as np
stattime = time.time()

def mandelbrotchecker_esc(x, y, maxiter):

    c = complex(x, y)
    z = complex(0, 0)

    for x in range(maxiter):
        sum = z * z + c
        if (abs(z) >= 2):
            return x
        z = sum

    return maxiter

def mandelbrotchecker_px(x, y, maxiter):

    c = complex(x, y)
    z = complex(0, 0)

    for x in range(maxiter):
        sum = z * z + c
        if (abs(z) >= 2):
            return x * 10 % 255
        z = sum

    return 255

def compute_mandelbrot(h = 400, w = 400,startx = -2.0,endx = 2.0,starty = -2.0,endy = 2.0, maxiter=1000, plot_filename=None):

    if(startx < -2 or endx > 2 or starty < -2 or endy > 2):
        raise ValueError('A very specific bad thing happened')



    stattime = time.time()

    increment = 0.01

    a = []
    b =[]

    if plot_filename == None:
        data = np.zeros((h, w, 1), dtype=np.uint8)

    if plot_filename != None:
        data = np.zeros((h, w, 3), dtype=np.uint8)

    while startx < endx:
        a.append(startx)
        startx = startx + increment

    while starty < endy:
        b.append(starty)
        starty = starty + increment

    for x in range(len(a)):
        for y in range(len(b)):

            if(plot_filename == None):
                color_value=(mandelbrotchecker_esc(a[x] , a[y], maxiter))
                data[y][x] = color_value
            else:
                color_value=(mandelbrotchecker_px(a[x] , a[y], maxiter))
                data[y][x] = (color_value,color_value,color_value)


    endtime = time.time()

    if plot_filename != None:
        img = Image.fromarray(data, 'RGB')
        img.save(str(plot_filename + ".png"))

    print ("\n total time:")
    print(endtime-stattime)