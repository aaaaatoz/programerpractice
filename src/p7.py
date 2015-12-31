import math

def isPerfectNumber(number):
    mylist = []
    maxnumber = number/2
    index = 1
    while index <= maxnumber:
        if number % index == 0 : mylist.append(index)
        index += 1
    return number == sum(mylist)


if __name__=="__main__":
    for index in xrange(1,10000):
        if isPerfectNumber(index): print index