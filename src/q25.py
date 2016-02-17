def findSteps(n):
    if n <= 0:
        return 0
    elif n == 1 :
        return 1
    elif n == 2 :
        return 2
    else:
        return findSteps(n-1) + findSteps(n-2)

if __name__=="__main__":
    print findSteps(10)