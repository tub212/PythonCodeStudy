n = input()
m = raw_input()
nsum = n
for i in reversed(xrange(1, n, len(m))):
	if i <= 0:
		pass
	else:
		x = i
		print x
		nsum = nsum * abs(x)
print nsum