from my_unit_testing import UnitTest

def better_addition(a, b, num_rechecks=666):
    """Returns sum of a, b, but double checks answer several times."""
    sum_computations = [a + b for n in range(num_rechecks)]
    print(sum_computations)

    for n in range(num_rechecks):
        #print('\n')
        #print(sum_computations[n])
        #print(sum_computations[n-1])

        if sum_computations[n] != sum_computations[n-1]:
            print("Hang on, let me recheck that")
            return better_addition(a, b, num_rechecks)

    print(sum_computations[0])
    return sum_computations[0]  # if all computations match, return whichever

num_tests = 0
num_passed = 0

for a, b, n, r in [(4, 7, 0, 11),(4, 7, 4, 11),(2, 2, 2, 4)]:

    test = UnitTest(better_addition,[a, b], {"num_rechecks": n}, r)

    num_tests+= 1
    if test():                           # Test has to return bool
        num_passed += 1



print("{}/{} tests passed".format(num_passed, num_tests))

#a is the first number
#b is the second number
#n is the number of rechecks


#itteration 1:
# a= 4 , b=7 n= 0 r=11
# sum_computations = []

#itteration 2:
# a= 4, b=7 n=4 r=11
# sum_computations = [11, 11, 11, 11]

#itteration 3:
# a= 2 , b = 2, n= 2 , r=4
# sum_computations = [4, 4]

#As you can see the problem is that the function will throw an index out of range when trying to accsess sum_computations[0] on an empty array
#The test fails when n = 0