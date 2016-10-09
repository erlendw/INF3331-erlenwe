##"pure" python implementation
##todo set your own range
from PIL import Image
from progressbar import *
import time

stattime = time.time()

def mandelbrotchecker(x, y):

    c = complex(x, y)
    z = complex(0, 0)

    for x in range(1000):
        sum = z * z + c
        if (abs(z) >= 2):
            return x * 10 % 255
        elif (x == 999):
            return 0
        z = sum

def createMandelbrot(startx = -2.0,endx = 2.0,starty = -2.0,endy = 2.0):


    stattime = time.time()

    increment = 0.01

    a = []
    b =[]

    while startx < endx:
        a.append(startx)
        startx = startx + increment

    while starty < endy:
        b.append(starty)
        starty = starty + increment

    im = Image.new("RGB",(len(a),len(b)))

    pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=len(b)).start()
    for x in range(len(a)):
        for y in range(len(b)):
            color_value=(mandelbrotchecker(a[x] , a[y]))
            im.putpixel((x, y), (color_value%10, color_value, color_value%200)) #140 ser bra ut
            pbar.update(x)
    pbar.finish()

    im.save("mandelbrot.png", "PNG")

    endtime = time.time()

    print ("\n total time:")
    print(endtime-stattime)

createMandelbrot()





