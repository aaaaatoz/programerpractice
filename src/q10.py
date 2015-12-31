import math

if __name__=="__main__":
    for i in xrange(3,1000):
        for j in xrange(i,1000):
            if math.sqrt(i*i +j*j).is_integer():
                print "%d,%d,%d" %(i,j,int(math.sqrt(i*i+j*j)))