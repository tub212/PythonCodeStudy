def factorial(n):
	if n == 0:
		return 1
	else:
		recurse = factorial(n-1)
		result = n * recurse
		return result

print factorial(input())			
