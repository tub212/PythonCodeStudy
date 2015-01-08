"""Nokia Legends 3310"""
def sms3310(number):
    """Change word to a phone number clicker."""
    nokia = {"a" : "2", "d" : "3", "g" : "4","j" : "5", "m" : "6",  \
     "p" : "7",  "t" : "8", "w" : "9",  " " : "0"}
    nokia2 = {"b" : "22", "e" : "33", "h" : "44", "k" : "55", \
    "n" : "66", "q" : "77", "u" : "88", "x" : "99"}
    nokia3 = {"c" : "222", "f" : "333", "i" : "444", \
    "l" : "555", "o" : "666", "r" : "777", "v" : "888",}
    nokia4 = {"s" : "7777", "z" : "9999"}
    result = ""
    for loop in number:
        text = number[loop]
        if loop + 1 < len(number) and text + number[loop+1] in nokia2:
            
        result += nokia[loop]
    return result
print sms3310(raw_input())
