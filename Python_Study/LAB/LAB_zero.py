"""Lab_ZERO"""
def zeronumber():
    """
    int -> int
    input number ans sum all number input not zero
    """
    number = int(raw_input())
    answer = number
    while number < 0 or number > 0:
        sumnumber = int(raw_input())
        number = sumnumber
        answer += sumnumber
    print answer
zeronumber()
