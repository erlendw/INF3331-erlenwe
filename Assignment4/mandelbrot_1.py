##"pure" python implementation
##todo set your own range
from PIL import Image

def mandelbrotchecker(x, y):
    c = complex(x, y)
    z = complex(0, 0)

    arr = []

    for x in range(1001):
        sum = z * z + c
        arr.append(sum)
        if (abs(z) >= 2):
            return x * 10 % 255
        elif (x == 1000):
            return 255
        z = sum


startx = -2.0
endx = 2.0

starty = -2.0
endy = 2.0

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

for x in range(len(a)):
    for y in range(len(b)):
        color_value=(mandelbrotchecker(a[x] , a[y]))
        print( str(x) + " " + str(y) + " " + " " + str(color_value))
        im.putpixel((x, y), (color_value, color_value, color_value))


im.save("mandelbrot.png", "PNG")