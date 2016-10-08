from numpy import *
from PIL import Image
import time

##its fucking slower
##https://www.ibm.com/developerworks/community/blogs/jfp/entry/How_To_Compute_Mandelbrodt_Set_Quickly?lang=en

height= 400
width= 400

def mandelbrotchecker(c):
    z=c

    for i in range(1000):
        multiply(z,z,z)
        z =add(z,c,z)
        
        print(z)



starttime = time.time()

y,x = ogrid[ -2:2 : height*1j, -2:2:width*1j ]

im = Image.new("RGB", (x.size,y.size))

c = x+y*1j

mandelbrotchecker(c)

del y
del x
'''
for i,j in ndenumerate(c):
    #print(str(i) + "  " +str(j))
    color_value = mandelbrotchecker(c[i])
    im.putpixel((i), (color_value, color_value, color_value))
    #print(color_value)

for i in arange(height):
    for j in arange(width):
        color_value = (mandelbrotchecker(c[i][j]))
        im.putpixel((i, j), (color_value, color_value, color_value))
'''
im.save("mandelbrot_3.png", "PNG")
endtime= time.time()

print(endtime-starttime)

