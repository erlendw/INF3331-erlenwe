from math import sin
from math import cos
from math import sqrt
theStack = []
possibleArguments = ['+','*','/','P','p','sin','cos','v']
print("Numbers are sperated by spaces, you can input +, *, /, v, cos and sin to pop the two last numbers and calculate according to"
      " your mathematical operation (v==square root)")

while True:

    print("RPN me below:")
    theInput = input()
    theInputArray = theInput.split()

    print(theInputArray)

    #adds integers to stack
    for i in range(len(theInputArray)):
        try:
            theResult=int(theInputArray[i])
            theStack.append(theResult)
        except:
            pass

    for i in range(len(theInputArray)):
        if(len(theStack) >= 2):
            if(theInputArray[i] in possibleArguments):

                x = theStack.pop(len(theStack)-1)
                y = int(theStack.pop(len(theStack)-1))

                if(theInputArray[i] == "+"):
                    res=(x+y)
                    print(str(x) + "+" + str(y) + "=" + str(res))
                    theStack.append(res)

                if(theInputArray[i] == "*"):
                    res=(x*y)
                    print(str(x) + "*" + str(y) + "=" + str(res))
                    theStack.append(res)

                if(theInputArray[i] == "/"):
                    res=(float(x)/float(y))
                    print(str(x) + "/" + str(y) + "=" + str(res))
                    theStack.append(res)

                if(theInputArray[i] == "P" or theInputArray[i] == "p"):
                    print(theStack[len(theStack)-1])

                if(theInputArray[i] == "sin"):
                    res=sin(theStack[len(theStack)-1])
                    print("sine of " + str(theStack[len(theStack)-1]) + " is " + str(res))
                    theStack.append(res)

                if(theInputArray[i] == "cos"):
                    res=cos(theStack[len(theStack)-1])
                    print("cosine of " + str(theStack[len(theStack)-1]) + " is " + str(res))
                    theStack.append(res)

                if(theInputArray[i] == "v"):
                    res=sqrt(theStack[len(theStack)-1])
                    print("Square root of " + str(theStack[len(theStack)-1]) + " is " + str(res))
                    theStack.append(res)


        else:
            print("not eneough numbers in stack, you need at least 2")
            break



    print("Current stack:")
    print(theStack)