"""Quiz_ChristmasTree"""
def tree(leaf, stem):
    """
    Return ChristmasTree With tall(leaf+stem)
    """
    for i in xrange(leaf):
        print " "*(leaf-i-1) + "*"*(2*i+1)
    for tall in xrange(stem):
        tall = leaf
        print " "*(tall-2)+"-"*3
tree(input(), input())

    
