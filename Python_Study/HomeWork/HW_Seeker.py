"""HW_Seeker"""
def seek(text, string="", number=list()):
    """return sum of number in $text"""
    for char in text:
        if char in "0123456789":
            string += char
        elif string != "":
            number.append(int(string))
            string = ""
    if string != "":
        number.append(int(string))
    return sum(number)
print seek(raw_input())
