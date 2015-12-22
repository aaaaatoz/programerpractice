#!/bin/python

if __name__=="__main__":
    count = 0
    for index1 in xrange(1,10):
        for index2 in xrange(0,10):
            if index2 == index1 : continue
            for index3 in xrange(0,10):
                if index3 == index1 or index3 == index2: continue
                print index1, index2, index3
                count += 1
    print count