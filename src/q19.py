def average(scoreList):
    if len(scoreList) <= 2:
        return 0
    else:
        return (sum(scoreList) - min(scoreList) - max(scoreList)) * 1.0 / (len(scoreList) - 2)


if __name__ == "__main__":
    scorelist = [1,2,3,4,5,6,7,8,9,10,11,8,9,34]
    print(average(scorelist))
