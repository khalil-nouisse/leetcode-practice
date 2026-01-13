"""
Valid Palindrome
================

Problem:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Idea:
Two main approaches:
1. **Reverse String (O(N) Time, O(N) Space)**:
   - Filter alphanumerics, convert to lowercase, reverse and compare.
   
2. **Two Pointers (O(N) Time, O(1) Space)**:
   - Use two pointers, one at the beginning (l) and one at the end (r).
   - Move pointers inward, skipping non-alphanumerics.
   - Compare characters.

Complexity:
- Time: O(N)
- Space: O(1) for Two Pointers.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Validates if a string is a palindrome using Two Pointers (Optimal).
        Time: O(N), Space: O(1)
        """
        l, r = 0, len(s) - 1
        
        while l < r:
            # Move left pointer forward until an alphanumeric char is found
            while l < r and not self._is_alnum(s[l]):
                l += 1
            # Move right pointer backward until an alphanumeric char is found
            while r > l and not self._is_alnum(s[r]):
                r -= 1
                
            # Compare characters case-insensitively
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
            
        return True

    def _is_alnum(self, c: str) -> bool:
        """
        Helper to check if a character is alphanumeric.
        Own implementation or use c.isalnum()
        """
        return c.isalnum()

    def isPalindromeReverse(self, s: str) -> bool:
        """
        Validates palindrome by creating a reversed filtered string.
        Time: O(N), Space: O(N)
        """
        s = s.lower()
        # Filter alphanumeric characters
        filtered_chars = [ch for ch in s if ch.isalnum()]
        filtered_s = "".join(filtered_chars)
        
        # Compare with reversed
        return filtered_s == filtered_s[::-1]

if __name__ == "__main__":
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    print(f"Input: '{s}'")
    print(f"Is Palindrome (Two Pointers): {solution.isPalindrome(s)}")
    print(f"Is Palindrome (Reverse): {solution.isPalindromeReverse(s)}")