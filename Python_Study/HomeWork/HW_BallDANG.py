"""HW_BallDANG"""
def ball(tall, count=0):
    """Return number of ball bounce on floor"""
    while tall >= 1:
        tall, count = tall * 3.0/5.0, count + 1
    return count - 1 if count > 0 else count
print ball(input()*100)
