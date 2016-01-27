from sys import argv

if len(argv) < 2:
    print("No data file given")
    exit(1)

script, filename = argv

def read_data(filename):
	"""This function reads data from a file in argv[1]. The cost (or credit) is defined as the 
	integer of the number displayed on the first line. The prizes (the rest of the lines) are
	appended to the list "prizeslist", also as integers. The "cost" value and the "prizeslist"
	list is then returned so it can be used in the "prize" function."""
	with open(filename, 'r') as f:
	    first = f.readline()
	    cost = int(first)
	    prizeslist = []
	    for prize in f:
	    	prizeslist.append(int(prize))
	return cost, prizeslist


def prize(C, prizes):

	"""This function prints out the costs of pairs of prizes that add up to credit "C" exactly,
	the amount of credit you are given. If there is more than one combination of these prizes whose, 
	cost add up to your credit, all possible combinations are printed. If no combinations of prize
	add up to the credit, "Hard luck" is returned and printed."""

	possibleprizes = []
	# A list to which I will append pairs of prizes that add up to my credit 'C'

	for item in range(0,len(prizes)):
	# 'for' loop to find the difference credit and each item in the prize list 

		difference = C - prizes[item] 

		for item2 in range(item+1,len(prizes)):
			# a nested 'for' loop to compare difference with other items
			
			if prizes[item2] == difference and item != item2:
			# checks if difference is equal to another prize, and that item and item2 are not the same items
			# if cost of item2 = difference, then item and item2 are appended because they add up exactly ot credit 'C'

					possibleprizes.append((prizes[item],prizes[item2]))
	
	if possibleprizes == []:
		# If 'possibleprizes' list is empty (there are no two prizes that add up to my credit), "Hard luck" is printed
		return("Hard luck") 
	else: 
		return(possibleprizes)

cost, prizeslist = read_data(filename)

print(prize(cost, prizeslist)) # I print the output of prize function when it is called for "cost" and "prizeslist"