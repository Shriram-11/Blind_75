def groupAnagrams(strs):
	"""
	Groups anagrams from a list of strings.

	:param strs: List[str]
		A list of strings to be grouped into anagrams.

	:rtype: List[List[str]]
		A list of lists, where each sublist contains words that are anagrams of each other.
	"""
	# Initialize an empty dictionary to hold groups of anagrams
	d = dict()
	
	# Iterate over each string in the input list
	for a in strs:
		# Sort the string and convert it back to a string to use as a key
		v = str(sorted(a))
		
		# If the sorted string is already a key in the dictionary
		if v in d:
			# Append the original string to the corresponding list
			d[v].append(a)
		else:
			# Otherwise, create a new entry in the dictionary
			d[v] = [a]
	
	# Return the values of the dictionary as a list of lists
	return d.values()
