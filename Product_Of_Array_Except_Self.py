class Solution(object):
    def productExceptSelf(self, nums):
        """
        Given an integer array nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

        The problem can be solved in O(n) time complexity and O(1) space complexity (excluding the output array).

        :type nums: List[int]  # Input list of integers
        :rtype: List[int]      # Output list of integers where each element is the product of all other elements in the input list
        """
        n = len(nums)  # Length of the input list
        prod = [1] * n  # Initialize the result list with 1s. This will hold the final product values.
        
        # Calculate the prefix product for each index
        p = 1  # Initialize prefix product variable
        for i in range(n):
            prod[i] *= p  # Multiply the current prefix product with the current element
            p *= nums[i]  # Update the prefix product to include the current element
        
        # Calculate the postfix product for each index and update the result list
        p = 1  # Initialize postfix product variable
        for i in range(n-1, -1, -1):
            prod[i] *= p  # Multiply the current postfix product with the current value in the result list
            p *= nums[i]  # Update the postfix product to include the current element
        
        return prod  # Return the final result list
