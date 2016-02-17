def chickenProblem():
    for cock in xrange(1,20):
        for hen in xrange(34-cock):
            if (100 - cock - hen) % 3 == 0 and cock * 5 + hen * 3 + (100 - cock - hen) / 3 == 100:
                print "%d cocks, %d hens, %d chicken" %(cock,hen, 100-cock-hen)

if __name__=="__main__":
    chickenProblem()