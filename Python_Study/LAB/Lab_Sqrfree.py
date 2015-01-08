"""how many sqrfree"""
def issqrfree(num):
    '''input int out amout of sqrnum'''
    count=0
    for j in range(num+1):
        for check in range(2,int(j**0.5)):
            if(j%(check**2)==0):
                count+=1
            break
    print num-count
issqrfree(input())
