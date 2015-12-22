#!/bin/python

def isNarcissisticNumber(number):
    k = len(str(number))
    counter = 0
    for i in str(number):
        counter += int(i) ** 3
    return number == counter

if __name__=="__main__":
    for index in xrange(100,999):
        if isNarcissisticNumber(index): print index
