def is_reverse(word1, word2):
	return True if word1[::] == word2[::-1] else False
print is_reverse(raw_input(), raw_input())	