"""HW_DotE"""
from math import factorial
def dote():
    """int -> int
    this programme find a seat for player in team"""
    player = (input() + 1)/2*2
    playerseat = factorial(player)/(factorial(player/2))**2
    print playerseat
dote()
