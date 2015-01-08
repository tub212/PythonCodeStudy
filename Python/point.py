'''Graderrrrrrrrrrr'''
#Comment

def grader(point):
    '''
    score >= 80 : A
    score 70-79 : B
    score 60-69 : C
    score 50-59 : D
    score <  50 : F
    '''
    if point >= 80:
        return "A"
    else:
        if point >= 70 and point <= 79:
            return "B"
        else:
            if point >= 60 and point <= 69:
                return "C"
            else:
                if point >= 50 and point <= 59:
                    return "D"
                else:
                    return "F"
print grader(input())
