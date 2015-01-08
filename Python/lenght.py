'''Check Lenght number'''
#Comment
def check_lenght(number):
    '''check Lenght number'''
    if number < 0:
        return len(str(int(number * -1)))
    elif type(number) == str:
        pass
    else:
        return len(str(int(number)))
print check_lenght(input())