from clint import *
from clint.textui import *

import mandelbrot_1
import mandelbrot_2
from  c_in_python_cython import mandelbrot_3
from  c_in_python_swig import mandelbrot_4

def callMandelbrot1():
    mandelbrot_1.createMandelbrot()

def callMandelbrot2():
    mandelbrot_2.createMandelbrot()


def callMandelbrot3():
    mandelbrot_3.createMandelbrot()


def callMandelbrot4():
    mandelbrot_4


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
        theInput = raw_input()

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