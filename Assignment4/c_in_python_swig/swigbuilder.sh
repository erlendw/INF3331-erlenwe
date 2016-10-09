echo "starting build"

cmd1="swig -python -module mandelbrot mandelbrot.h"
eval "$cmd1"
echo "swig complete"

cmd2="gcc -fPIC -O2 -c  mandelbrot*.c -I /usr/include/python3.5/"
eval "$cmd2"
echo "C files are compiled"

cmd3="gcc -shared mandelbrot*.o -o _mandelbrot.so"
eval "$cmd3"
echo "shared object created"
