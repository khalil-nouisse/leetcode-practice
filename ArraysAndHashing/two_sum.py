"""
Two Sum
=======

Problem:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Idea:
1. **Hash Map (One Pass) - Optimal**:
   - Iterate through the array.
   - For each number `x`, check if `target - x` exists in the hash map.
   - If yes, return the current index and the index of `target - x`.
   - If no, store `x` and its index in the hash map.
   
2. **Brute Force**:
   - Nested loops checking every pair.

Complexity:
- Time: O(N) for Hash Map approach.
- Space: O(N) for Hash Map.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds indices of two numbers that add up to target using a Hash Map.
        Time: O(N), Space: O(N)
        """
        seen = {}  # Map value -> index
        
        for i, num in enumerate(nums):  
            complement = target - num  
            if complement in seen:  
                return [seen[complement], i]
            seen[num] = i
        return []

    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        """
        Brute force approach.
        Time: O(N^2)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(f"Input: nums={nums}, target={target}")
    print(f"Indices (Hash Map): {solution.twoSum(nums, target)}")
    print(f"Indices (Brute Force): {solution.twoSumBruteForce(nums, target)}")