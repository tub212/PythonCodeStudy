"""LeapYear"""
def leapyear(year):
    """int -> Bool
        Check the input year is a leapyear"""
    year = year - 543
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False
print leapyear(int(raw_input()))
