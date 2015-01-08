"""Lab_Roman"""
def roman(string, ans=0):
    """Return Roman TO Decimal number"""
    number = {"I":1 , "V":5 , "X":10 , "L":50 , "C":100 , "D":500 , "M":1000}
    for i in string:
        check = string.index(i)
        if number[i] < number[check + 1]:
            ans += number[check + 1] - number[i]
        else:
            ans += number[i]
    print ans
roman(raw_input())
