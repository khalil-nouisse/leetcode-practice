"""
Valid Parentheses
=================

Problem:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Idea:
Use a **Stack**.
- Iterate through the string.
- If it's an opening bracket, push it onto the stack.
- If it's a closing bracket:
  - Check if the stack is empty (invalid).
  - Pop the top element and check if it matches the incomplete pair using a mapping.
- At the end, if the stack is empty, it's valid.

Complexity:
- Time: O(N)
- Space: O(N) (worst case all opening brackets)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Validates parentheses using a stack.
        """
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        
        for c in s:
            # If closing bracket
            if c in pairs:
                # If stack is empty or top doesn't match
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                # If opening bracket
                stack.append(c)
                
        # Valid if stack is empty
        return not stack

if __name__ == "__main__":
    solution = Solution()
    test_cases = ["()", "()[]{}", "(]", "([)]"]
    
    for s in test_cases:
        print(f"'{s}' is valid: {solution.isValid(s)}")