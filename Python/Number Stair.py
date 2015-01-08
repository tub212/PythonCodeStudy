"""Number Stair"""
####Comment
def numstair(floor):
    """Make Number stair"""
    if floor >= 1:
        number, space, spacal = 0, -1, 0
        while number != floor:
            number += 1
            space += 1
            print number,
            if space == spacal:
                space = -1
                spacal += 1
                print
numstair(input())
