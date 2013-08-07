def while_function(a):
	i = 0
	numbers = []
	while i < a:
		print "At the top i is %d" % i 
		numbers.append(i)

		i = i + 1 
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	return numbers


def print_result(nums):
	print "The numbers: "
	for num in nums:
		print num


print_result(while_function(6))



