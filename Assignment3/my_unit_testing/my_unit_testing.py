import sys

class UnitTest(object):
    globalId = 0

    def __init__(self, func, args, kwargs, res):    # make test

        UnitTest.globalId +=1 #global count is used to identify wich of the tries that failed

        self.args = args
        self.func = func
        self.kwargs = kwargs
        self.res = res

    def __call__(self):                             # run test
        hasPassed = False
        reportText = ""

        try:
            print("This is try #" + str(UnitTest.globalId))
            hasPassed = self.func(self.args[0],self.args[1],self.kwargs['num_rechecks'])

        except:
            print("Failed when n = " + str(self.kwargs['num_rechecks']) + " this was try #" + str(UnitTest.globalId))

            reportText = self.func.__name__ + " produced exeption type " + str(sys.exc_info()[0]) + "\n\n"
            reportText += "Exeption string: " + str(sys.exc_info()[1]) + "\n\n"
            reportText += "At line #: " + str(sys.exc_info()[-1].tb_lineno) + "\n\n"
            reportText += "Test failed at try #" + str(UnitTest.globalId)

            with open("report.txt", "w") as report:
                print(reportText, file=report)

        if(hasPassed  == self.res):
            return True
        else:
            return False
