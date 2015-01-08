def count(word):
	for i in word:
		print  i + ":" + str(word.count(i))
count(raw_input())