"'Hate docstring'"
#i hate docstring
def distance(x1, y1, x2, y2):
	#this function find distance between dot 2 dot 
	dis_x = x2 - x1	
	dis_y = y2 - y1
	disexpo = dis_x**2 + dis_y**2
	disans = disexpo**0.5
	return disans

print distance(input(), input(), input(), input())	