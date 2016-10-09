import numpy as np #makes it easier while using ide
cimport cython
cimport numpy as np


cdef int mandelbrotchecker(double x, double y):

    cdef complex c = complex(x, y)
    cdef complex z = c
    cdef complex sum

    for i in range(1001):
        sum = z*z + c
        if (abs(z) >= 2):
            return i * 10 % 255
        elif (i == 1000):
            return 255
        z = sum


cpdef me(int h, int w):

    cdef np.ndarray data = np.zeros((h, w, 3), dtype=np.uint8) ##this will be the picture
    cdef np.ndarray y = np.linspace(-2,2,w)
    cdef np.ndarray x = np.linspace(-2,2,h)

    for i in range(w):
        for j in range(h):
            colorval = mandelbrotchecker(x[i], y[j])
            data[i][j] = [colorval,colorval,colorval]

    return data