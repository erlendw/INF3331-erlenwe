from clint import *
from clint.textui import *
import imp



import mandelbrot_1
import mandelbrot_2
from  c_in_python_cython import mandelbrot_3


def callMandelbrot1():
    mandelbrot_1.createMandelbrot()


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



'''

bahaha

'''

args = Args()
for i in range(len(args)):
    if args[i] == ("--help" or "-help"):
        printTheHelp()




getinput()