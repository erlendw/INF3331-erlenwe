import m
import time
from PIL import Image



def createMandelbrot(startx = -2.0,endx = 2.0,starty = -2.0,endy = 2.0):
    starttime = time.time()
    data = m.me(400,400, startx,endx,starty,endy)
    img = Image.fromarray(data, 'RGB')
    img.save('mandelbrotinC.png')
    endtime = time.time()
    print endtime-starttime

