"""Lab_Bigram"""
def bigram(string):
    """Return bigram of input string"""
    char, time, lis_char = "", 0, dict()
    for i in xrange(len(string) - 1):
        key = string[i] + string[i + 1]
        lis_char[key] = lis_char.get(key, 0) + 1
        if lis_char[key] > time:
            time, char = lis_char[key], key
    print char , "\n", time
bigram(raw_input())
