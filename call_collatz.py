import collatz_function

try:
	
 	number = input("Please enter number: ")
 	while 1:
	 	integer = collatz(number)
	 	print(ineger)
	 	if integer == 1:
	 		break 
	 	else:
	 		number = integer
except ValueError:
	raise "Didn't write number, try again!!"
