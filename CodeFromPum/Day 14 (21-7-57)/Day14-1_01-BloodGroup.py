'''Day14-1_01-BloodGroup'''
#Pumpsama.

def group(times):
    '''When found bloodtype increase number by 1'''
    blood_a, blood_b, blood_o, blood_ab = 0, 0, 0, 0
    for blood in range(times):
        blood = raw_input()
        if "AB" in blood:
            blood_ab += 1
        elif "O" in blood:
            blood_o += 1
        elif "A" in blood:
            blood_a += 1
        elif "B" in blood:
            blood_b += 1
    print blood_a
    print blood_b
    print blood_o
    print blood_ab
group(input())
