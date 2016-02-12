def printTriangle(line):
    matrix = [[0 for col in xrange(0,line+1)] for row in xrange(0,line+1)]
    for row in xrange(1,line+1):
        for col in xrange(1,row+1):
            if col == 1:
                matrix[row][col] = 1
            else:
                matrix[row][col] = matrix[row-1][col-1] + matrix[row-1][col]
            print matrix[row][col],
        print ""



if __name__=="__main__":
    printTriangle(10)
