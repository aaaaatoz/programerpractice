for a1 in xrange(1,10):
    for a2 in xrange(0,10):
        for a3 in xrange(1,10):
            if a1 <> a2 and a2 <> a3 and a1 <> a3 and (100*a1+10*a2+a3)*(100*a3+10*a2+a1) == 280021:
                print a1,a2,a3