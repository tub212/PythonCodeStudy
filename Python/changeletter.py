"""ChangeLetter"""
###cOMMent
def changelett(string, change, position):
    """Change in a input position"""
    if position > len(string):
        print "Error"
    elif position == 0:
        print "Error"
    else:
        if position == 1:
            print change + string[1:]
        else:
            print string[:position-1] + change + string[position:]
changelett(raw_input(), raw_input(), input())
