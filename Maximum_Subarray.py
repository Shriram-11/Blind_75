class Solution(object):
    def maxSubArray(self, nums):
        """
        Finds the maximum sum of a contiguous subarray within a one-dimensional array of numbers.

        :type nums: List[int]  # Input list of integers
        :rtype: int           # Maximum sum of contiguous subarray
        """
        # Initialize variables
        max_sum = current_sum = nums[0]

        # Iterate through the list starting from the second element
        for num in nums[1:]:
            # Update current_sum to include the current number
            current_sum = max(num, current_sum + num)
            # Update max_sum if current_sum is greater
            max_sum = max(max_sum, current_sum)

        return max_sum
