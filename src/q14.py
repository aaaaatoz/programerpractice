#!/bin/python

def printMultiplyMatrix():
    for i in xrange(1,10):
        for j in xrange(1,i+1):
            print "%d*%d=%-2d " %(i,j,i*j),
        print ""

if __name__=="__main__":
	printMultiplyMatrix()