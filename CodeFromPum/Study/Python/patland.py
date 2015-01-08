"""MEOW PAT"""
def patland(number):
    for loo in xrange(1 ,number+1):
        city = raw_input()
        casenum = str(loo)
        text = city[len(city)-1:]
        while True and text != 'a' or text != 'e' or text != 'i' or \
            text != 'o' or text != 'u' or text != 'y':
            print "Case #" + casenum + ": " + city + " is ruled by a king."
            break
        while True and text == 'a' or text == 'e' or text == 'i' or \
            text == 'o' or text == 'u' or text == 'y':
            print "Case #" + casenum + ": " + city + " is ruled by a queen."
            break
        while True and text == 'y':
            print "Case #" + casenum + ": " + city + " is ruled by a nobody."
            break
patland(input())
        
