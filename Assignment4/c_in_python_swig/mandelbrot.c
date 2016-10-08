#include "mandelbrot.h"
#include <complex.h>

int mandelbrotchecker(double x, double y)
{

    double complex c = x + y * I;
    double complex z = c;
    int i;

    for( i = 0; i < 1001; i = i + 1 ){


        z = z*z + c;

        if(cabs(z)>=2){

            return i * 10 % 255;

        }
    }

    return 255;
}
