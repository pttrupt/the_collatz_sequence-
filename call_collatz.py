from collatz_function import collatz 

try:
	num = int(input("Enter Number: "))
	while True:
		integer = collatz(num)
		print(integer)
		if integer == 1:
			break 
		else:
			num = integer 
except ValueError:
	print("It is not number, try again!!")
