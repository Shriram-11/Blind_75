def containsDuplicate(nums):
	"""
	:type nums: List[int]
	:rtype: bool
	"""
	#initialize a set to store the numbers which have been seen
	seen=set()
	#traverse from first number to the last in the list nums
	for a in nums:
		
	#if a number is alredy present in the set return True
		if a in seen:
			return True
	
	#else add the number in the set
		seen.add(a)

	#Finally after traversing entire list we did not find any duplicate hence we can return False
	return False
