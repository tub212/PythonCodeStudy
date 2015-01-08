'''Duke Style 3'''
#Pumpsama.

def dukestyle3(word):
    checkloop = 0
    for i in word:
        checkloop += word.count(i)
        if checkloop != len(word):  
            print i + ":" + str(word.count(i))
dukestyle3(raw_input())
