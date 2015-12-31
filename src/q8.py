
def getAmicablePair(number):
    mylist = []
    maxnumber = number/2
    index = 1
    while index <= maxnumber:
        if number % index == 0 : mylist.append(index)
        index += 1
    return sum(mylist)

if __name__=="__main__":
    amicablePair = {}
    for index in xrange(1,10000):
        amicablePair[index] = getAmicablePair(index)
    vlist = set([v for v in amicablePair.itervalues() if v < 10000 and v >= 1])
    for i in vlist:
        if amicablePair.get(amicablePair[i],0) == i and amicablePair[i] <> i:
            print (amicablePair[i],i)