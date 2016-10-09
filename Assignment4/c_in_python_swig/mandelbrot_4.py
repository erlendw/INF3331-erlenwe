import mandelbrot
import numpy as np
from PIL import Image
import time

def createMandelbrot(width = 10000, height=10000,startx = -2.0,endx = 2.0,starty = -2.0,endy = 2.0):
    starttime = time.time()
    data = np.zeros((height, width, 3), dtype=np.uint8) ##this will be the picture
    y = np.linspace(startx,endx,width)
    x = np.linspace(starty,endy,height)

    for i in range(width):
        for j in range(height):
            colorval = mandelbrot.mandelbrotchecker(x[i], y[j])
            data[j][i] = [colorval%10,colorval,colorval%255]

    img = Image.fromarray(data, 'RGB')
    img.save('mandelbrotinCSWIGsd.png')
    endtime = time.time()

    print endtime-starttime




