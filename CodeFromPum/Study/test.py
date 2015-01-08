word = raw_input()
step = input()
index = 0
stri = ""
while index < len(word):
	text = word[index]
	stri += text
	index += step
print stri