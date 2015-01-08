'''sentenceAnlyze'''
def sentence(string):
    '''DOOGGGGG'''
    string = string.split()
    string.sort()
    time = 0
    while time < len(string):
        if not string[time] in string[:time]:
            count = string.count(string[time])
            print string[time]+':'+str(count)
        time += 1
sentence(raw_input())
