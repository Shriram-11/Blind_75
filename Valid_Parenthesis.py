class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determines if the input string `s` containing only the characters 
        '(', ')', '{', '}', '[' and ']' is valid. A string is considered 
        valid if the brackets are closed properly and every opening bracket 
        has a corresponding closing bracket in the correct order.

        :type s: str
            The string to be checked for validity.
        :rtype: bool
            Returns True if the string is valid; otherwise, returns False.
        
        Example:
        >>> sol = Solution()
        >>> sol.isValid("()")
        True
        >>> sol.isValid("()[]{}")
        True
        >>> sol.isValid("(]")
        False
        >>> sol.isValid("([)]")
        False
        >>> sol.isValid("{[]}")
        True
        """
        
        # If the length of the string is odd, it cannot be valid (since brackets need to be paired)
        if len(s) % 2 != 0:
            return False
        
        # Stack to keep track of opening brackets
        stk = []
        
        # Dictionaries to map opening brackets to their corresponding closing brackets
        o = {"(": 0, "[": 1, "{": 2}
        c = {")": 0, "]": 1, "}": 2}
        
        # Iterate over each character in the string
        for a in s:
            # If the character is an opening bracket, push its corresponding value onto the stack
            if a in o:
                stk.append(o[a])
            else:
                # If the stack is not empty, pop the top element and check if it matches the current closing bracket
                if stk:
                    b = stk.pop()
                    if b != c[a]:
                        return False
                else:
                    # If the stack is empty but a closing bracket is found, the string is invalid
                    return False
        
        # If the stack is empty, all brackets are matched correctly; otherwise, return False
        return len(stk) == 0
