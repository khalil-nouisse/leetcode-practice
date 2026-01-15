"""
Longest Common Prefix
=====================

Problem:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Idea:
1. **Vertical Scanning** (Current Approach):
   - Find the shortest string (optimization to avoid out of bounds).
   - Iterate through each character index of the shortest string.
   - For each index, check if all strings have the same character.
   - If match, append to result. If mismatch, break and return.

2. **Sorting**:
   - Sort the strings.
   - Compare only the first and last string (they are the most different).
   - The common prefix of first and last is the common prefix of all.

Complexity (Vertical Scanning):
- Time: O(S) where S is the sum of all characters in all strings.
- Space: O(1).
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Finds strings longest common prefix using Vertical Scanning.
        """
        if not strs:
            return ""
            
        # Optimization: The prefix cannot be longer than the shortest string
        # Pythonic way to find shortest string
        min_elem = min(strs, key=len)
        min_len = len(min_elem)
        
        longest_prefix = ""
        
        for i in range(min_len):
            current_char = min_elem[i]
            for s in strs:
                if s[i] != current_char:
                    return longest_prefix
            longest_prefix += current_char
            
        return longest_prefix

    def longestCommonPrefixSorting(self, strs: List[str]) -> str:
        """
        Alternative: Sorting approach.
        Time: O(N log N * M) where M is length of strings (due to sorting).
        """
        if not strs:
            return ""
        
        strs.sort()
        s1 = strs[0]
        s2 = strs[-1]
        idx = 0
        while idx < len(s1) and idx < len(s2):
            if s1[idx] == s2[idx]:
                idx += 1
            else:
                break
        return s1[:idx]

if __name__ == "__main__":
    solution = Solution()
    strs = ["flower", "flow", "flight"]
    print(f"Input: {strs}")
    print(f"Longest Common Prefix (Vertical): '{solution.longestCommonPrefix(strs)}'")
    print(f"Longest Common Prefix (Sorting): '{solution.longestCommonPrefixSorting(strs)}'")

