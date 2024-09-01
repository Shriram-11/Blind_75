class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = []  # Initialize an empty list to store the result triplets
        nums.sort()  # Sort the input list to make it easier to avoid duplicates and use the two-pointer technique
        
        # Iterate through the sorted list
        for i in range(len(nums) - 2):
            # Skip duplicate values for the current element to avoid duplicate triplets in the result
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Initialize two pointers, one just after the current element and one at the end of the list
            j, k = i + 1, len(nums) - 1
            
            # Use a two-pointer technique to find the other two elements that sum with nums[i] to zero
            while j < k:
                # Calculate the sum of the current triplet
                total = nums[i] + nums[j] + nums[k]
                
                if total == 0:
                    # If the sum is zero, add the triplet to the result list
                    l.append([nums[i], nums[j], nums[k]])
                    
                    # Move pointers to skip over duplicates of the second element
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    
                    # Move pointers to skip over duplicates of the third element
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    
                    # Move both pointers inward after finding a valid triplet
                    j += 1
                    k -= 1
                elif total < 0:
                    # If the sum is less than zero, increment the left pointer to get a larger sum
                    j += 1
                else:
                    # If the sum is greater than zero, decrement the right pointer to get a smaller sum
                    k -= 1
        
        return l  # Return the list of triplets that sum to zero
