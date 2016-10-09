from clint import *
from clint.textui import *

import mandelbrot_1
import mandelbrot_2
from  c_in_python_cython import mandelbrot_3
from  c_in_python_swig import mandelbrot_4

def callMandelbrot1():


    sx = input("input start x")
    ex = input("input end x")

    sy = input("input start y")
    ey = input("input end y")



    mandelbrot_1.createMandelbrot(sx,ex,sy,ey)

def callMandelbrot2():


    sx = input("input start x")
    ex = input("input end x")

    sy = input("input start y")
    ey = input("input end y")

    mandelbrot_2.createMandelbrot(sx,ex,sy,ey)


def callMandelbrot3():



    sx = input("input start x")
    ex = input("input end x")

    sy = input("input start y")
    ey = input("input end y")

    mandelbrot_3.createMandelbrot(sx,ex,sy,ey)


def callMandelbrot4():


    sx = input("input start x")
    ex = input("input end x")

    sy = input("input start y")
    ey = input("input end y")

    mandelbrot_4.createMandelbrot(sx,ex,sy,ey)


def printTheHelp():

    puts(" \n \n Here is a list of the available files, all are different implementations of the mandelbrot set: ")

    with indent(4):
        puts(colored.red("mandelbrot_1.py"))
        with indent(4):
            puts(colored.red("Pure python implementation ising regular old lists"))

        puts(colored.yellow("mandelbrot_2.py"))
        with indent(4):
            puts(colored.yellow("Numpy implementations, using numpy arrays / vectors"))

        puts(colored.green("mandelbrot_3.py"))
        with indent(4):
            puts(colored.green("Numpy + cython"))

        puts(colored.magenta("mandelbrot_4.py"))
        with indent(4):
            puts(colored.magenta("SWIG, wrapped C + python"))





def getinput():

    while True:
        theInput = input()

        if(theInput == ("help")):
            printTheHelp()

        if(theInput == ("mandelbrot_1")):
            callMandelbrot1()
            
        if(theInput == ("mandelbrot_2")):
            callMandelbrot2()
        
        if(theInput == ("mandelbrot_3")):
            callMandelbrot3()

        if(theInput == ("mandelbrot_4")):
            callMandelbrot4()



'''

bahaha

'''

args = Args()
for i in range(len(args)):
    if args[i] == ("--help" or "-help"):
        printTheHelp()




getinput()