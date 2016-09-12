
theStack = []

print("Numbers are sperated by spaces, you can input +, * and / to pop the two last numbers and calculate according to"
      " your mathematical operation")

while True:

    print("RPN me below:")
    theInput = input()
    theInputArray = theInput.split()

    for i in range(len(theInputArray)):
        try:
            theResult=int(theInputArray[i])
            theStack.append(theResult)
        except:
            pass

    if(theInput == "+" or theInput == "*" or theInput == "/"):
        if(len(theStack) >= 2):

            x = theStack.pop(len(theStack)-1)
            y = int(theStack.pop(len(theStack)-1))

            if(theInput[0] == "+"):
                res=(x+y)
                print(str(x) + "+" + str(y) + "=" + str(res))

            if(theInput[0] == "*"):
                res=(x*y)
                print(str(x) + "*" + str(y) + "=" + str(res))

            if(theInput[0] == "/"):
                res=(float(x)/float(y))
                print(str(x) + "/" + str(y) + "=" + str(res))

        else:
            print("not eneough numbers in stack, you need at least 2")

    print("Current stack:")
    print(theStack)
