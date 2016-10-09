from numpy import *
from PIL import Image
import time
from numba import cuda

##its fucking slower
##https://www.ibm.com/developerworks/community/blogs/jfp/entry/How_To_Compute_Mandelbrodt_Set_Quickly?lang=en

height= 400
width= 400

def mandelbrotchecker(c):
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


starttime = time.time()

y,x = ogrid[ -2:2 : height*1j, -2:2:width*1j ]

im = Image.new("RGB", (x.size,y.size))

c = x+y*1j


for i in arange(height):
    print(i)
    for j in arange(width):
        color_value = (mandelbrotchecker(c[i][j]))
        im.putpixel((i, j), (color_value, color_value, color_value))

im.save("mandelbrot_3.png", "PNG")
endtime= time.time()

print(endtime-starttime)

