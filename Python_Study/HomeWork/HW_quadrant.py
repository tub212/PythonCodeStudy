"""Quadrant"""
def quadrant(point_x, point_y):
    """int -> quadrant
        this programme find point x,y is in quadrant1 2 3 4,
        on x on y or on origin"""
    if point_x == 0 and point_y == 0:
        print "O
        "
    elif point_x == 0 and (point_y < 0 or point_y > 0):
        print "Y"
    elif point_y == 0 and (point_x < 0 or point_x > 0):
        print "X"
    elif point_x > 0 and point_y > 0:
        print "Q1"
    elif point_x < 0 and point_y > 0:
        print "Q2"
    elif point_x < 0 and point_y < 0:
        print "Q3"
    elif point_x > 0 and point_y < 0:
        print "Q4"
quadrant(int(raw_input()), int(raw_input()))
