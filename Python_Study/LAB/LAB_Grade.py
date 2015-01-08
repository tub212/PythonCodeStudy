"""Lab_grade"""
def grade(point):
    """int -> str
        this programme is return grade A - F"""
    if point < 70:
        print "F"
    elif point >= 70 and point < 75:
        print "D"
    elif point >= 75 and point < 80:
        print "D+"
    elif point >= 80 and point < 85:
        print "C"
    elif point >= 85 and point < 90:
        print "C+"
    elif point >= 90 and point < 95:
        print "B"
    elif point >= 95 and point < 100:
        print "B+"
    elif point >= 100 and point <= 120:
        print "A"
grade(int(raw_input()))
