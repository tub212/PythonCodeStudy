'''Collatz'''
###comment
def collatz(num_coll):
    print num_coll
    while num_coll != 1:
        if num_coll % 2 != 0:
            num1 = 3*(num_coll)+1
            print num_coll
        else:
            num_coll = num_coll/2
            print num_coll
collatz(input())            
