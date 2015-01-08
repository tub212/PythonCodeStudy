'''HW_ScaledMatrix'''
def function():
    '''return matix scaled in range 0-1'''
    line = input()
    coll = input()
    mini = 99999999
    maxi = -99999999
    mtrx = []
    for i in range(line):
        i = []
        for j in range(coll):
            j = float(input())
            i.append(j)
            if j > maxi:
                maxi = j
            if j < mini:
                mini = j
        mtrx.append(i)
    for i in range(line):
        for j in range(coll):
            mtrx[i][j] = (mtrx[i][j]-mini)/(maxi-mini)
    for i in range(line):
        for j in range(coll):
            print str(mtrx[i][j]+0.005)[:4],
        print ''
function()    
