"""Siad Number"""
def saidnum(number):
    """Doc"""
    text = ["zero", "one", "two", "three", "four", "five",
            "six", "seven", "eight", "nine", "ten"]
    for i in number:
        print text[int(i)],
saidnum(raw_input())
