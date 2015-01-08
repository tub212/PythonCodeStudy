x1 = input()
y1 = input()
r1 = input()
x2 = input()
y2 = input()
r2 = input()
ra = r1 + r2
compar = ((x1 - x2)**2 + (y1 + y2)**2)**0.5

if compar <= ra:
	print "overlapping"
elif compar > ra:
	print "no overlapping"	