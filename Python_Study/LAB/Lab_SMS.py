"""Lab_SMS"""
def sms(word):
    """Return Word with input T9 keypad"""
    str_dic, word_ls = {2:"ABC", 3:"DEF", 4:"GHI", 5:"JKL", 6:"MNO", 7:"PQRS"\
    , 8:"TUV", 9:"WXYZ"}, []
    for _ in xrange(word):
        pad, push = input(), input()
        if not pad == 1:
            pad2 = str_dic[pad]
            word_ls.append(pad2[(push%len(pad2))-1])
        else:
            for _ in xrange(push):
                if len(word_ls) > 0:
                    del word_ls[len(word_ls)-1]
                else:
                    break
    return "".join(word_ls) if len(word_ls) > 0 else "null"
print sms(int(raw_input()))
