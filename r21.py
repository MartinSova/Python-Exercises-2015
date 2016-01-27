def successive(S):
	
	"""This functions prints a string such that each letter of the string is printed on a new line,
	and each letter has L spaces preceding it when it is printed."""
	
	L = len(S)-1 
	# L is length of string S minus 1, so that final letter is preceded by 0 spaces

	for letter in S:
	# a 'for' loop prints each letter of string "S" on new line
		
		print(" "*L,letter)
		# prints each letter with L spaces preceding it 

		L = L - 1
		# L decrements by 1 when each letter is printed to evoke the "slant" effect from right to left

successive("slantwise")