def isBadDay (year,month,day):
    #assume 1/1/2016 is Friday
    days = ( year - 2016 ) * 365 + (year - 2013) / 4
    isLeapYear = ( year % 4 == 0 )
    monthDict = {1:31, 2:28, 3: 31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    for i in xrange(1,month):
        days += monthDict[i]
    if isLeapYear and month > 2:
        days += 1
    days += (day-1)
    return days % 7 == 0

if __name__=="__main__":
    for year in xrange(2016,2022):
        for month in xrange(1,13):
            if isBadDay(year,month,13):
                print "%d/%d/13 is bad luck day" %(year,month)
