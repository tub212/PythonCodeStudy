def sumall(num):
	ls = map(int, num)
	return sum(ls)

def pro():
	sum_f = input("Day: ") + input("Month: ") + input("Year: ")
	num = sum_f
	while num > 10:
		num_cal = str(num)
		num = sumall(num_cal)
	print  "Answer is: " + str(num)
pro()