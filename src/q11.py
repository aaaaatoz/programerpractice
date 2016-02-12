#!/bin/python


def isAutomorphicNumber(n):
    return (((n * n) - n) % (10 ** len(str(n))) == 0)

if __name__=="__main__":
    for i in xrange(1,10000):
        if isAutomorphicNumber(i):
            print i
