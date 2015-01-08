"""This is a Cake Not Lie"""
#####Comment
def cake(floor):
    """DOGGGGGGG"""
    if floor > 1:
        spacecal, space = 0, -2
        cakeg, cakepip = 0, 1
        while spacecal != floor:
            spacecal += 1
            space += 1
        print (" " * int(floor + space)) + "( )"
        while space != -floor:
            space -= 1
            cakeg += 2
            cakepip += 2
            print (" " * int(floor + space)) + "_|" * cakeg + "_"
            space -= 1
            print (" " * int(floor + space)) + "| " * cakepip + "|"
        print (" " * int(floor + space)) + "|_" * int(cakeg + 1) + "|"
cake(input())
