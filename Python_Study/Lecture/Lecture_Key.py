"""Lecture_Key"""
def key(ssn):
    """Return last 4 digit of calculate"""
    num = sum(map(int, ssn)) + int(ssn[-3:])*10
    return str(num)[-4:] if num > 1000 else str(num + 1000)[-4:]
print key(raw_input())
