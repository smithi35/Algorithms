import sys
	
def euclid(first, second) :
	# print("first = " + str(first) + ", second = " + str(second))
	if (first < second) :
		temp = first
		first = second
		second = temp
	# print("first = " + str(first) + ", second = " + str(second))
	
	prev = second
	curr = first % second
	
	while curr > 0 :
		next = prev % curr
		prev = curr
		curr = next
		
	print("gcd(" + str(first) + ", " + str(second) + ") = " + str(prev))
		
if len(sys.argv) == 3:
	euclid(int(sys.argv[1]), int(sys.argv[2]))
else :
	print("Please enter two numbers as command-line arguments")
