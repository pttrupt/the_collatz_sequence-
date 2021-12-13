
def collatz(number):

	if number%2 == 0:
		return number//2    # '//' gives integer result 
	else:
		return 3*number + 1