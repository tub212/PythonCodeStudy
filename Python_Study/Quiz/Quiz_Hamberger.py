"""PostQuiz1Round2dot1_Hamburger"""
def hamberger(left, right):
    """
    Return Hamberger with | and *
    """
    print "|"*left + "*"*((left+right)*2) + "|"*right
hamberger(input(), input())
