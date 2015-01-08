def backward():
    """Return backward list with out loop"""
    word = raw_input()
    if word == "NULL":
        lsword.sort(reverse=True)
        return lsword
    else:
        lsword.append(word)
        backward()
print backward()
