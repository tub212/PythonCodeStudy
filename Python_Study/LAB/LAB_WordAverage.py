"""Lab_WordAverage"""
def check_word(word, count=0.00):
    """Return len word"""
    for i in word:
        if i.isalpha() == True:
            count += 1
    return count
def word_avg(word):
    """Return Average of len word"""
    word_ls, check = word.split(), []
    word_ls = [word.strip(".") for word in word_ls]
    for string in word_ls:
        if check_word(string) != 0:
            check.append(check_word(string))
    return format(sum(check)/(len(check)), "0.2f") if len(check) > 0 else "0.00"
print word_avg(raw_input())
