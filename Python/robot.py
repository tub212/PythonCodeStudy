"""ROBOT"""
def robot(text):
    """DEFFFFFFFF"""
    count_x = 0
    count_y = 0
    for hahaha in text:
        if hahaha == 'N':
            count_y += 1
        if hahaha == 'S':
            count_y -= 1
        if hahaha == 'E':
            count_x += 1
        if hahaha == 'W':
            count_x -= 1
        if hahaha == 'Z':
            count_x = 0
            count_y = 0
    print count_x, count_y
robot(raw_input())
