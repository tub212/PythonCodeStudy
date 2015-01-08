"""GamesHow"""
def games(word, roll):
    """Gameshow 555"""
    if roll > len(word):
        roll = roll % len(word)
        print str(word[roll:])+str(word[:roll])
    else:
        print str(word[roll:])+str(word[:roll])
games(raw_input(), input())
