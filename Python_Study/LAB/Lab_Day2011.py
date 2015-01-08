"""Lab_Day2011"""
def day2011(date, month):
    """
    return day in 2011
    """
    date = (date%7)-7
    dayls = ["Sunday", "Monday", "Tuesday", "Wednesday",
             "Thursday", "Friday", "Saturday"]
    if month == 1 or month == 10:
        print dayls[date+5]
    if month == 2 or month == 3 or month == 11:
        print dayls[date+1]
    if month == 4 or month == 7:
        print dayls[date+4]
    if month == 9 or month == 12:
        print dayls[date+3]
    if month == 5:
        print dayls[date-1]
    if month == 6:
        print dayls[date+2]
    if month == 8:
        print dayls[date]
day2011(int(raw_input()), int(raw_input()))
    
