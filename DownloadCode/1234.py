""" This program find number of battery that need to charge"""
def volt_check(n_batt, v_target):
    """ int -> int """
    i = 1
    volt = []
    vbatt = input()
    while i<= n_batt :
        volt.append(input())
        i = i+1
    print volt
    total = 0
    for x in xrange(1,len(volt)):
        if volt[x] < volt[0] :
            total = total+1
    print total

n_robot = input()
j = 0
while j< n_robot :
    volt_check(input(), input())
    j = j+1
