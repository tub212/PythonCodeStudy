"""Training_CollatzConjecture"""
memo = dict()
def collatz(num):
    """Return Number of max length of collatz"""
    if num < 2:
        return num
    for i in xrange(len(memo) + 1, num + 1):
        if not i in memo:
            memo[i] = len(collatz_sequence(i))
    return max(memo.values())
def collatz_sequence(num):
    """Return length of collatz_sequence number"""
    seq = [num]
    while seq[-1] > 1:
        seq.append(num / 2) if num % 2 == 0 else seq.append((3 * num) + 1)
        num = seq[-1]
    return seq
print collatz(input())
