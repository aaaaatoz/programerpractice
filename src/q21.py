import time
def deliveryCandle(list):
    time.sleep(1)
    resultlist = [0 for x in range(10)]
    for i in xrange(9):
        resultlist[i] = (list[i] + 1) / 2 + (list[i+1] + 1) / 2
    resultlist[9] = (list[9] + 1) / 2 + (list[0] + 1) / 2
    print resultlist
    for i in xrange(9):
        if resultlist[i] <> resultlist[i+1]:
            return False, resultlist
    return True, resultlist

if __name__=="__main__":
    count = 1
    initialList = [10,-2,8,876,16,4,78,6,14,20]
    result,resultList =  deliveryCandle(initialList)
    while not result:
        count += 1
        result,resultList =  deliveryCandle(resultList)