'''Time Converter'''
#Comment
def check(value):
    '''Time Converter Function'''
    mintime = (value % 3600) / 60
    sectime = value % 60
    hourtime = value / 3600
    ho1 = " hours, "
    min1 = " minutes, "
    sec1 = " seconds."
    return str(hourtime) + ho1 + str(mintime) + min1 + str(sectime) + sec1
print check(input())