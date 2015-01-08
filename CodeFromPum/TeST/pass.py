"""PASSWORD"""
def password(word):
    """PASS"""
    upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    countupp = 0
    countnum = 0
    for i in word:
        if i in upp:
            countupp += 1
        if i in num:
            countnum += 1
        else:
            pass
    if len(word) < 10:
        print "*" * len(word) + " is bad password."
    else:
        if countupp >= 1 and countnum >= 1:
            print "*" * len(word) + " is good password."
        else:
            print "*" * len(word) + " is bad password."
password(raw_input())
