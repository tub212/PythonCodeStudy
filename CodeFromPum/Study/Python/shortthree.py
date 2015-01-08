'''SortThree'''
#Comment

def sortthree(time_1, time_2, time_3):
    '''Printing'''
    if time_1 <= time_2 and time_1 <= time_3:
        ans = time_1
        if time_2 <= time_3:
            ans = str(time_1) + " " + str(time_2) + " "+str(time_3)
            return ans
        else:
            ans = str(time_1) + " " + str(time_3) + " "+str(time_2)
            return ans
    elif time_2 <= time_3 and time_2 <= time_1:
        ans = time_2
        if time_1 <= time_3:
            ans = str(time_2) + " " + str(time_1) + " "+str(time_3)
            return ans
        else:
            ans = str(time_2) + " " + str(time_3) + " "+str(time_1)
            return ans
    elif time_3 <= time_2 and time_3 <= time_1:
        ans = time_3
        if time_2 <= time_1:
            ans = str(time_3) + " " + str(time_2) + " "+str(time_1)
            return ans
        else:
            ans = str(time_3) + " " + str(time_1) + " "+str(time_2)
            return ans
print sortthree(input(), input(), input())
