"""Quiz2Round1_Median"""
def med(num):
    """Return Median of input
        int -> Float"""
    num_ls, med_cal = [input() for _ in xrange(num)], (num + 1)/2.0
    num_ls.sort()
    return float(num_ls[int(med_cal-1)]) if med_cal == int(med_cal) \
           else (num_ls[int(med_cal-1)] + num_ls[int(med_cal)]) / 2.0
print med(input())



size = input()
def ls(size):
    summation = 0
    for ix in xrange(size):
        summation += input()%10
    return summation

size = input()
def med2(size):
    ax = []
    ix in xrange(size):
        ax.append(input())
    ax.sort()
    if len(ax) % 2:
        print ax[len(ax)/2]*1.0
    else:
        print ax[len(ax)/2]+ax[(len(ax)/2)-1]

