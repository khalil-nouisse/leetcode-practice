"""
Palindrome Number
=================

Problem:
Given an integer x, return true if x is a palindrome, and false otherwise.
Follow up: Could you solve it without converting the integer to a string?

Idea:
1. **Reversing the entire number**:
   - Limit: might overflow if the reversed number exceeds integer limits (though Python handles large integers automatically).
   - Algorithm: Extract last digit (`x % 10`) and build reversed number.

2. **Reversing half the number** (Optimal):
   - To avoid overflow and redundant work.
   - Reverse the second half of the number and compare it with the first half.
   - Example: 1221 -> x=12, reversed=12.
   - Example: 121 -> x=1, reversed=12. (remove last digit of reversed -> 1).

Complexity:
- Time: O(log_10(N)) because we process digits.
- Space: O(1).
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Checks if an integer is a palindrome by reversing half of the number.
        Time: O(log N)
        """
        # Negative numbers are not palindromes (e.g., -121 != 121-)
        # Numbers ending in 0 (except 0 itself) are not palindromes (e.g., 10 -> 01 no)
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
            
        reversed_half = 0
        while x > reversed_half:
            last_digit = x % 10
            reversed_half = (reversed_half * 10) + last_digit
            x = x // 10
            
        # When length is even, x == reversed_half
        # When length is odd, x == reversed_half // 10 (middle digit doesn't matter)
        return x == reversed_half or x == reversed_half // 10

    def isPalindromeFullReverse(self, x: int) -> bool:
        """
        Checks if an integer is a palindrome by reversing the entire number.
        """
        if x < 0:
            return False
            
        original = x
        reversed_num = 0
        while x > 0:
            last_digit = x % 10
            reversed_num = (reversed_num * 10) + last_digit
            x = x // 10
            
        return original == reversed_num

if __name__ == "__main__":
    solution = Solution()
    num = 121
    print(f"Input: {num}")
    print(f"Is Palindrome (Half Reverse): {solution.isPalindrome(num)}")
    print(f"Is Palindrome (Full Reverse): {solution.isPalindromeFullReverse(num)}")
