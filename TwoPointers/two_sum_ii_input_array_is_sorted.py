"""
Two Sum II - Input Array Is Sorted
==================================

Problem:
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
Return the indices of the two numbers, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

Idea:
1. **Two Pointers (Optimal)**:
   - Since the array is sorted, we can use two pointers.
   - Initialize `left` at start, `right` at end.
   - If `sum > target`, move `right` pointer down (to decrease sum).
   - If `sum < target`, move `left` pointer up (to increase sum).
   - If `sum == target`, return indices.

Complexity:
- Time: O(N)
- Space: O(1)
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Finds indices of two numbers that add up to target using Two Pointers.
        Assumes input array is sorted.
        Time: O(N), Space: O(1)
        """
        l, r = 0, len(numbers) - 1
        
        while l < r:
            current_sum = numbers[l] + numbers[r]
            
            if current_sum == target:
                return [l + 1, r + 1]
            elif current_sum > target:
                r -= 1
            else:
                l += 1
                
        return []

    def twoSumHashMap(self, numbers: List[int], target: int) -> List[int]:
        """
        Alternative: using Hash Map.
        Time: O(N), Space: O(N)
        """
        mapp = {}
        for i, num in enumerate(numbers):
            need = target - num
            if need in mapp:
                return [mapp[need] + 1, i + 1]
            mapp[num] = i
        return []

    def twoSumBruteForce(self, numbers: List[int], target: int) -> List[int]:
        """
        Alternative: Brute Force.
        Time: O(N^2)
        """
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []

if __name__ == "__main__":
    solution = Solution()
    numbers = [-5, -3, 0, 2, 4, 6, 8]
    target = 5
    
    print(f"Input: numbers={numbers}, target={target}")
    print(f"Indices (Two Pointers): {solution.twoSum(numbers, target)}")
    print(f"Indices (Hash Map): {solution.twoSumHashMap(numbers, target)}")
    print(f"Indices (Brute Force): {solution.twoSumBruteForce(numbers, target)}")


