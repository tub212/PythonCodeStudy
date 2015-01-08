"""Lab_Factor"""
def factor(line):
    """
    
    """
    numls = []
    facls = []
    for i in xrange(line):
        num = int(raw_input())
        numls.append(num)
    for j in numls:
        count = 0
        for k in xrange(1, (j**0.5)+1):
            if j % k == 0:
                count += 1
                
