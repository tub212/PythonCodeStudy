"""ReverseWord"""
###Comment
def reverse(word):
    """Print Reversed Word"""
    wordlist = word.split()
    for i in reversed(wordlist):
        print i,
reverse(raw_input())
