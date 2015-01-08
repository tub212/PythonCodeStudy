"""What is Docstirng"""
#Comment
def lonesum(num1, num2, num3):
    """Doc"""
    if num1 != num2 and num1 != num3 and num3 != num2:
        return num1 + num2 + num3
    elif num1 == num2 and num1 == num3 and num3 == num2:
        return "0"
    elif num1 == num3:
        return num2
    elif num2 == num3:
        return num1
    elif num1 == num2:
        return num3
print lonesum(input(), input(), input())
