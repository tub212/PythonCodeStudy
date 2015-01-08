"""This function make a bridge"""
def makebridge(brick_s, brick_b, longbridge):
    """
    int -> int
    return number of small brick and return -1 if can't make a bridge
    """
    if (brick_s*1)+(brick_b*5) < longbridge:
        print "-1"
    else:
        goal = longbridge % 5
        bridge5 = brick_b*5
        if brick_s < goal:
            print "-1"
        elif bridge5 < longbridge:
            bricksmall = longbridge - bridge5
            print bricksmall
        else:
            print goal
makebridge(input(), input(), input())
