from numpy import *
from PIL import Image
from progressbar import *
import time

##its fucking slower
##https://www.ibm.com/developerworks/community/blogs/jfp/entry/How_To_Compute_Mandelbrodt_Set_Quickly?lang=en

starttime = time.time();

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

presicion = 0.01

x = arange(-2,2, step=presicion)
y = arange(-2,2, step=presicion)

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
print("saving image")
im.save("mandelbrot_2.png", "PNG")
endtime= time.time()

print(endtime-starttime)

