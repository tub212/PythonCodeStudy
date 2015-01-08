'''integerORfloat'''
#Comment
def check(value):
    '''Check int of float'''
    if type(value) == int:
        return "integer"
    elif type(value) == float:
        return "float"

print check(input())			