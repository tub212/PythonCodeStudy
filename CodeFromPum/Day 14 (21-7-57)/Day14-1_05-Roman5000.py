'''Day14-1_05-Roman5000'''
#Pumpsama.

def roman5000(input_number):
    '''Change roman numbers to arabic numbers'''
    roman_dictionary = { "M" : 1000, "CM" : 900, \
    "D" : 500, "CD" : 400, "C" : 100, "XC" : 90, \
    "L" : 50, "XL" : 40, "X" : 10, "IX" : 9, \
    "V" : 5, "IV" : 4, "I" : 1}
    print sum(roman_dictionary.values())
roman5000(raw_input())
