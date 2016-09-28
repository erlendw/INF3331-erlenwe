from numpy import *
from PIL import Image
from progressbar import *
import time

starttime = time.time()

def mandelbrotchecker(x, y):
    c = complex(x, y)
    z = complex(0, 0)
    a = arange(1000)
    counter=0
    for x in nditer(a):
        sum = z * z + c
        if (abs(z) >= 2):
            return x * 10 % 255
        elif (counter == 999):
            return 255
        z = sum
        counter+=1


presicion = 0.1

x = arange(-2,2, step=presicion)
y = arange(-2,2, step=presicion)

data = zeros((x.size, y.size, 3), dtype=uint8)

im = Image.new("RGB", (x.size,y.size))


counterx = 0
countery = 0

pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=x.size).start()

for i in nditer(x):
    for j in nditer(y):
        color_value = (mandelbrotchecker( i, j))
        im.putpixel((counterx, countery), (color_value, color_value, color_value))
        countery = countery + 1
        pbar.update(counterx)
    counterx += 1
    countery = 0

for i,j in ndenumerate(data):
    print(i , j)

pbar.finish()
endtime= time.time()


im.save("mandelbrot_3.png", "PNG")

print(endtime-starttime)

