"""HW_Vowel"""
def vowel():
    """delete vowel in string"""
    return raw_input().translate(None, "AEIOUaeiou")
print vowel()
