"""BloodType"""
def blood(number):
    """BLOOD"""
    blooddic = {"A": 0, "B" : 0, "O": 0, "AB": 0}
    for word in xrange(number):
        word = raw_input()
        text = word.split(",")
        if text[1] == "A":
            blooddic["A"] += 1
        elif text[1] == "B":
            blooddic["B"] += 1
        elif text[1] == "O":
            blooddic["O"] += 1
        elif text[1] == "AB":
            blooddic["AB"] += 1
    print blooddic["A"]
    print blooddic["B"]
    print blooddic["O"]
    print blooddic["AB"]
blood(input())
