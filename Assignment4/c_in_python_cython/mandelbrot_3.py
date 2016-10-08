import m
import time
from PIL import Image

starttime = time.time()


data = m.me(4000,4000)

img = Image.fromarray(data, 'RGB')
img.save('mandelbrotinC.png')
endtime = time.time()

print endtime-starttime