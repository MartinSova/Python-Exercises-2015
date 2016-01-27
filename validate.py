def is_valid(creditnumber):
	creditint = int(creditnumber)
	creditlist = list(creditnumber)

	if creditint < 0 or creditint%1 != 0:
		# I check whether the credit card number is negative or a decimal
		
		return False
	else:
		listnumber = []
		for i in creditlist:
			listnumber.append(int(i))
			# creditlist is converted to a list of integers, so that calculations can be made

		listnumber.reverse()
		counter = 0
		sumall = 0
		for digit in listnumber:
			if counter%2 == 0: 
				# values in listnumber for which modulo of counter == 0 are not doubled

				sumall += digit
			else:
				doubled = digit*2
				if doubled >= 10:
					# if doubled digit is greater than 10, its digits are added together using modulo of number + 1
					
					sumall += (doubled % 10 + 1)
				else:
					sumall += doubled
			counter += 1
		if sumall % 10 == 0:
			return True
		else:
			return False

creditnumber = "492X818708805X89"

credlist = list(creditnumber)

result = []
for x,i in enumerate(credlist):
	if i == "X":
		result.append(x)

# positions of "X"s are appended into a list 'result'

if len(result) == 1:
	# if length of results ==1, there is one "X"
	position = result[0]
	for m in range(9):
		credlist[position] = m
		# "X" is replaced with integers in range(9)
		# need to convert the elements to a string, and join the list of strings to a string for being able to call is_valid function
		
		if is_valid(''.join(str(e) for e in credlist)) == True:
			print(m) 

if len(result) == 2:
	position1 = result[0]
	position2 = result[1]
	for m in range(9):
		credlist[position1] = m
		for n in range(9):
			# 'for' loop is nested so all possible combinations of integers replacing both 'X's are checked

			credlist[position2] = n
			# need to convert the elements to a string, and join the list of strings to a string for being able to call is_valid function
		
			if is_valid(''.join(str(e) for e in credlist)) == True:
				print(m,n)

