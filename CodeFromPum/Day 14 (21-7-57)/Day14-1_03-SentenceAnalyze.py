'''Day14-1_03-SentenceAnalyze'''
#Pumpsama.

def sentenceanalyze(word):
    '''Sort dictionary and print how many of splited words'''
    word = word.split()
    word.sort()
    for loop in range(len(word)):
        if not word[loop] in word[:loop]:
            print word[loop] + ":" + str(word.count(word[loop]))
sentenceanalyze(raw_input())
