"""HW_Caesar v1"""
def caesar(key, string):
    """return Decryted string"""
    transtring = ""
    for i in string:
        char = ord(i)
        if char >= 97 and char <= 122:
            char += key
            while char > 122:
                char -= 26
            while char < 97:
                char += 26
        elif char >= 65 and char <= 90:
            char += key
            while char > 90:
                char -= 26
            while char < 65:
                char += 26
        transtring += chr(char)
    print transtring
caesar(input(), raw_input())
