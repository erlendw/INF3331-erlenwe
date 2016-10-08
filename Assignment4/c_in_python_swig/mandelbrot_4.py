import mandelbrot
import numpy as np
from PIL import Image
import time

def generateMandelBrot(w, h):

    data = np.zeros((h, w, 3), dtype=np.uint8) ##this will be the picture
    y = np.linspace(-2,2,w)
    x = np.linspace(-2,2,h)

    for i in range(w):
        for j in range(h):
            colorval = mandelbrot.mandelbrotchecker(x[i], y[j])
            data[j][i] = [colorval,colorval,colorval]

    return data

starttime = time.time()

data = generateMandelBrot(400,400)
img = Image.fromarray(data, 'RGB')
img.save('mandelbrotinCSWIGsd.png')
endtime = time.time()

print endtime-starttime