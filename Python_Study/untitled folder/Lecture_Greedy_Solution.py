"""Lecture_Greedy_Solution"""
def coin_greedy(num):
    """return number coin of cash"""
    coins = [25, 10, 5, 1]
    ans = 0
    for coin in coins:
        ans = ans + (num/coin)
        num = num % coin
    return ans
print coin_greedy(input())
