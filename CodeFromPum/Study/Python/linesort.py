"""Line Sort"""
def sortline(number):
    """SORTED"""
    lsit = []
    for i in xrange(number):
        word = raw_input()
        lsit.append(word)
    lsit.sort(key=len)
    for i in xrange(len(lsit)):
        print lsit[i]
sortline(input())
