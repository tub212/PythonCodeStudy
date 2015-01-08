"""Check 90 Triangle"""
def triangle(side1, side2, side3):
    if long1 + long2 < long3:
        return "NO"
    elif long1 + long3 < long2:
        return "NO"
    elif long2 + long3 < long1:
        return "NO"
    else:
        return "YES"    
triangle(int(raw_input()), int(raw_input()), int(raw_input()))