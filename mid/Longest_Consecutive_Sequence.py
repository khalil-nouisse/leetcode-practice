"""
Longest Consecutive Sequence
============================

Problem:
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
The algorithm should run in O(n) complexity.

Idea:
Use a HashSet to allow O(1) lookups.
1. Insert all numbers into a set.
2. Iterate through the set.
3. If `num - 1` is not in the set, it means `num` is the start of a sequence.
4. Count the length of the sequence starting from `num`.
5. Update the global maximum length.

Complexity:
- Time: O(N) because each number is visited at most twice (once in the loop, once in the while loop).
- Space: O(N) for the set.
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Finds the length of the longest consecutive sequence using a Set.
        Time Complexity: O(N)
        """
        if not nums:
            return 0
            
        set_nums = set(nums)
        longest = 0
        
        for num in set_nums:
            # Check if num is the start of a sequence
            if num - 1 not in set_nums:
                current_num = num
                current_streak = 1
                
                while current_num + 1 in set_nums:
                    current_num += 1
                    current_streak += 1
                
                longest = max(longest, current_streak)
                
        return longest

    def longestConsecutiveSorted(self, nums: List[int]) -> int:
        """
        Alternative approach using Sorting.
        Time Complexity: O(N log N)
        """
        if not nums:
            return 0
            
        nums.sort()
        longest = 1
        current_streak = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    current_streak += 1
                else:
                    longest = max(longest, current_streak)
                    current_streak = 1
        
        return max(longest, current_streak)
            

if __name__ == "__main__":
    solution = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    print(f"Input: {nums}")
    print(f"Longest Consecutive Sequence (O(N)): {solution.longestConsecutive(nums)}")
    
    # Note: Sort effectively modifies the list in place, so reset or use copy if needed for comparison 
    # but here we just run it. 
    nums_copy = [100, 4, 200, 1, 3, 2]
    print(f"Longest Consecutive Sequence (Sorted): {solution.longestConsecutiveSorted(nums_copy)}")