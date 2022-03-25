def numberOfLeap(year1,year2):
    count = 0
    for i in range(year1,year2+1):
        if leapYear(i):
            count += 1
    return 
