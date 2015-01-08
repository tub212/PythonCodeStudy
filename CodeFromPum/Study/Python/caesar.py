"""Caesar v1"""
##Comment
def caesar(count, sent):
    """Decode Caesar"""
    transent = ""
    for i in sent:
        letter = ord(i)
        if letter >= 97 and letter <= 122:
            letter += count
            while letter > 122:
                letter -= 26
            while letter < 97:
                letter += 26
        elif letter >= 65 and letter <= 90:
            letter += count
            while letter > 90:
                letter -= 26
            while letter < 65:
                letter += 26
        transent += chr(letter)
    print transent
caesar(input(), raw_input())
