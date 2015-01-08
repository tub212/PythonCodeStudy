def patland(city):
    """Patland"""
    lscity = [raw_input() for _ in xrange(city)]
    lsqueen = ["a", "e", "i", "o", "u"]
    for i in xrange(city):
        if lscity[i][-1] not in lsqueen and lscity[i][-1] != "y":
            print "Case #"+str(i+1)+": "+lscity[i]+\
                  " is ruled by a king."
        elif lscity[i][-1] in lsqueen:
            print "Case #"+str(i+1)+": "+lscity[i]+\
                  " is ruled by a queen."
        elif lscity[i][-1] == "y":
            print "Case #"+str(i+1)+": "+lscity[i]+\
                  " is ruled by nobody."
patland(input())
