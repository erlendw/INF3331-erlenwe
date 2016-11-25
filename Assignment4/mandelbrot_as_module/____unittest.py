import mandelbrot


'''
checks that script is not run with faulty xmin,xmax,ymin,ymax
'''

def test1_mandelbrot():

    try:
        mandelbrot.compute_mandelbrot(startx=3,endx=4,starty=3,endy=4)

    except:
        print("failed")


'''

checks that script does not crash when valid area of mandelbrot set is requested

'''

def test2_mandelbrot():

    try:
        mandelbrot.compute_mandelbrot(startx=-2,endx=2,starty=-2,endy=2)
        print('passed')
    except:
        print("failed")


test1_mandelbrot()
test2_mandelbrot()