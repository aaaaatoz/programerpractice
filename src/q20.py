def findTruck():
    for i in xrange(32,100):
        number = str(i * i)
        if (number[0]==number[1] and number[2]==number[3] and number[1] <> number[2]):
            print number

if __name__=="__main__":
    findTruck()