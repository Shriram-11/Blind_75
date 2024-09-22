def merge(intervals):
	"""
	Merges overlapping intervals.

	:param intervals: List[List[int]]
		A list of intervals where each interval is represented as a 
		list of two integers [start, end].

	:rtype: List[List[int]]
		A list of merged intervals.
	"""
	# Sort the intervals based on the starting times
	intervals.sort()
	
	# Initialize the result list with the first interval
	res = [intervals[0]]
	
	# Iterate through the intervals starting from the second one
	for i in range(1, len(intervals)):
		# If the current interval overlaps with the last merged interval
		if res[-1][1] >= intervals[i][0]:
			# Merge the intervals by updating the end time
			res[-1][1] = max(res[-1][1], intervals[i][1])
		else:
			# No overlap, so add the current interval to the result list
			res.append([intervals[i][0], intervals[i][1]])
	
	# Return the list of merged intervals
	return res
