'''Day14-1_02-MajorElement'''
#Pumpsama

def majorelement(value):
    '''Find most many numbers.'''
    value = value.split(",")
    answer = ""
    for loop in xrange(len(value)):
        if not value[loop] in value[:loop]:
            if value.count(value[loop]) > len(value)/2.0:
                answer = value[loop]
                break
            else:
                answer = "None"
    return answer
print majorelement(raw_input())
