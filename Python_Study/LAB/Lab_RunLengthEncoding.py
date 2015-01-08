"""Lab_RunLengthEncoding"""
def runlength(string):
    """
    return Encypted string
    """
    char = string[0]
    count = 0
    stroutput = ""
    for i in string:
        if i == char:
            count += 1
        else:
            stroutput += str(count) + char
            count = 1
            char = i
    stroutput += str(count) + char
    print stroutput
runlength(raw_input())

            
