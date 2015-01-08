"""SimpleSort"""
###Comment
def sort(word):
    """Print sort number"""
    wordlist = map(float, word.split())
    wordlist.sort()
    for i in wordlist:
        print "%.3f" % i,
sort(raw_input())
