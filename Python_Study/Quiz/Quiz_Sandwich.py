"""Quiz_Sandwich"""
def sandwich(display, left, right):
    """Return Word left & right side of display"""
    print left + " "*(display-len(left)-len(right)) + right
sandwich(input(), raw_input(), raw_input())
