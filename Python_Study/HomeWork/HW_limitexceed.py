"""Limit Exceed"""
def limitexceed():
    """
    int -> int
    This programme is return sumnumber and stop input if sumnumber > 1024
    """
    sumnumber = 0
    while sumnumber <= 1024:
        number = int(raw_input())
        sumnumber += number
    print sumnumber
limitexceed()
