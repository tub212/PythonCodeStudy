"""Lab_Day2011"""
def weekdays(day, month):
    """return weekday of day/month/2011"""
    return ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', \
    'Saturday'][(day + int('033614625035'[month-1]) + 11 + 2 + 6) % 7]
print weekdays(input(), input())
