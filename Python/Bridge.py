'''Bridge'''
#Comment
def bridge(brick1, brick2, goal):
    '''Docstring'''
    if 5 * brick2 > goal:
        if goal % 5 == 0:
            return "0"
        else:
            if goal % 5 > brick1:
                return "-1"
            else:
                return goal % 5
    elif brick1 + (5 * brick2) < goal:
        return "-1"
    else:
        return goal - (5 * brick2)
print bridge(input(), input(), input())
