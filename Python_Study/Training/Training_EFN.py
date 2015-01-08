"""Training_EFN"""
def efn(num, num_ans=0, num_1=0, num_2=1):
    """Return Sum of num%2 == 0 and not over input"""
    while num_2 <= num:
        if num_2 % 2 == 0:
            num_ans += num_2
        num_1, num_2 = num_2, num_1 + num_2
    return num_ans
print efn(input())
