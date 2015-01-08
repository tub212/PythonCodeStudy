"""PatLand(MEOW MEOW MEOW)"""
def patland(citynumber):
    """Why i don't use IF ELIF ELSE why???????"""
    for icount in xrange(citynumber):
        text = raw_input()
        count = icount
        while text[len(text)-1:] == "y":
            count += 1
            print "Case #"+str(count)+": "+str(text)+" is ruled by nobody."
            break
        while text[len(text)-1:] == "a" or \
              text[len(text)-1:] == "e" or \
              text[len(text)-1:] == "i" or \
              text[len(text)-1:] == "o" or \
              text[len(text)-1:] == "u":
            count += 1
            print "Case #"+str(count)+": "+str(text)+" is ruled by a queen."
            break
        while text[len(text)-1:] != "a" and \
              text[len(text)-1:] != "e" and \
              text[len(text)-1:] != "i" and \
              text[len(text)-1:] != "o" and \
              text[len(text)-1:] != "u" and \
              text[len(text)-1:] != "y":
            count += 1
            print "Case #"+str(count)+": "+str(text)+" is ruled by a king."
            break
patland(input())
