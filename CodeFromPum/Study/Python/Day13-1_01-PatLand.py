'''Day13-1_01-PatLand'''
#Pumpsama

def patland(citynumbers):
    '''NOT IF ... just doesn't matter!'''
    count = 0
    while citynumbers != count:
        cityname = raw_input()
        while cityname[len(cityname)-1:] == "Y" or \
              cityname[len(cityname)-1:] == "y":
            count += 1
            print "Case #"+str(count)+": "+str(cityname)+" is ruled by nobody."
            break
        while cityname[len(cityname)-1:] == "A" or \
              cityname[len(cityname)-1:] == "a" or \
              cityname[len(cityname)-1:] == "E" or \
              cityname[len(cityname)-1:] == "e" or \
              cityname[len(cityname)-1:] == "I" or \
              cityname[len(cityname)-1:] == "i" or \
              cityname[len(cityname)-1:] == "O" or \
              cityname[len(cityname)-1:] == "o" or \
              cityname[len(cityname)-1:] == "U" or \
              cityname[len(cityname)-1:] == "u":
            count += 1
            print "Case #"+str(count)+": "+str(cityname)+" is ruled by a queen."
            break
        while cityname[len(cityname)-1:] != "A" and \
              cityname[len(cityname)-1:] != "a" and \
              cityname[len(cityname)-1:] != "E" and \
              cityname[len(cityname)-1:] != "e" and \
              cityname[len(cityname)-1:] != "I" and \
              cityname[len(cityname)-1:] != "i" and \
              cityname[len(cityname)-1:] != "O" and \
              cityname[len(cityname)-1:] != "o" and \
              cityname[len(cityname)-1:] != "U" and \
              cityname[len(cityname)-1:] != "u" and \
              cityname[len(cityname)-1:] != "Y" and \
              cityname[len(cityname)-1:] != "y":
            count += 1
            print "Case #"+str(count)+": "+str(cityname)+" is ruled by a king."
            break
    citynumbers += 1
patland(input())
