'''v_v'''
def counter(word):
    '''T_T'''
    lister = ''
    for lap in xrange(len(word)):
        if not word[lap] in word[:lap]:
            #pass
        #else:
            count = 0
            count = word.count(word[lap])
            print word[lap],':',count
            lister += word[lap]
    lip = [0]*len(lister)
    for lap in xrange(len(lister)):
        lip[lap] = word.count(lister[lap])
    print 'max :', lister[(lip.index(max(lip)))]
    print 'min :', lister[(lip.index(min(lip)))]
counter(raw_input())
                          
