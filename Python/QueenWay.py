"""DOcstring"""
def aaaaa(number1):
    """DOcstring"""
    numberx = int(number1[0])
    numbery = int(number1[2])
    mapway = []
    for i in xrange(8):
        mapway.append([' ']*8)
    mapway[numberx][numbery] = 'Q'
    for i in xrange(8):
        setx(0, 1, numberx, numbery, mapway)
        setx(1, 0, numberx, numbery, mapway)
        setx(0, -1, numberx, numbery, mapway)
        setx(-1, 0, numberx, numbery, mapway)
        setx(1, 1, numberx, numbery, mapway)
        setx(-1, 1, numberx, numbery, mapway)
        setx(1, -1, numberx, numbery, mapway)
        setx(-1, -1, numberx, numbery, mapway)
    print "-----------------"
    for i in xrange(8):
        print "|"+"|".join(mapway[i])+"|"
        print "-----------------"

def setx(xxx, yyy, numberx, numbery, mapway):
    """DOcstring"""
    pox = numberx + xxx
    poy = numbery + yyy
    while pox < 8 and poy < 8 and\
          pox >= 0  and poy >= 0:
        mapway[pox][poy] = 'x'
        pox += xxx
        poy += yyy

aaaaa(raw_input())
