"""1TO1 """
###comment
def ntoone(number):
    """ int -> int(a lot)
        This function print number 1 to 1
    """
    if number == 0:
        print "1" "\n" "0" "\n" "1"
    elif number >= 1:
        for i in xrange(1, number+1):
            print i
        for j in reversed(xrange(1, number)):
            print j
    elif number <= -1:
        print "1" "\n" "0"
        for k in  xrange(1, abs(number)+1):
            print -k
        for j in reversed(xrange(1, abs(number))):
            print -j
        print "0" "\n" "1"
ntoone(int(raw_input()))
