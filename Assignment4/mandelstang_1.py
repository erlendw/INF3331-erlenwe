##"pure" python implementation
##todo set your own range
from PIL import Image

def mandelbrotchecker(x, y):
    c = complex(x, y)
    z = complex(0, 0)
    arr = []
    for x in range(1000):
        sum = z * z + c
        arr.append(sum)
        if (abs(z) >= 2):
            return x * 10 % 255
        elif (x == 999):
            return 255
        z = sum


start = -2.0
end = 2.0
increment = 0.01

pixels = int((end/increment)*2)

a = []
b =[]

im = Image.new("RGB",(pixels,pixels))

while start < end:
    a.append(start)
    b.append(start)
    start = start + increment

print(pixels)

for x in range(len(a)):
    for y in range(len(b)):
        color_value=(mandelbrotchecker(a[x] , a[y]))
        print( str(x) + " " + str(y) + " " + " " + str(color_value))
        im.putpixel((x, y), (color_value, color_value, color_value))


im.save("mandelbrot.png", "PNG")