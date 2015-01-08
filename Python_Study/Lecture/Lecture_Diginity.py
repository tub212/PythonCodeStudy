"""Lecture_Diginity"""
def cal(number):
    """Calculayre num to len == 1"""
    return int(number) if len(number) == 1 else cal(str(sum(map(int, number))))
def diginity(member):
    """Return Encypted Data"""
    while member != 0:
        print cal(str(member))
        member = input()
diginity(raw_input())

