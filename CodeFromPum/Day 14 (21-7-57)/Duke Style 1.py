'''Duke Style 1'''
#Pumpsama.

def dukestyle1(input1, input2):
    time = 0
    word = ""
    while time != input2:
        word += input1[0::input1]
    print word
dukestyle1(input(), raw_input())
