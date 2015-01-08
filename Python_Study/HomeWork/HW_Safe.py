"""HW_SAFE"""
def safe(word, enword):
    """Return minimun number chiper"""
    count = 0
    for i in xrange(len(word)):
        num1, num2 = ord(word[i]), ord(enword[i])
        if num1 < num2:
            if abs(num1 - num2) < abs((num1 + 26) - num2):
                count += abs(num1 - num2)
            else:
                count += abs((num1 + 26) - num2)
        else:
            if abs(num1 - num2) > abs(num1 - (num2 + 26)):
                count += abs(num1 - (num2 + 26))
            else:
                count += abs(num1 - num2)
    print count
safe(raw_input(), raw_input())
