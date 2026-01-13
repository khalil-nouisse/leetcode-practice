"""
Product of Array Except Self
============================

Problem:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The algorithm must run in O(n) time and without using the division operation.

Idea:
Use Prefix and Postfix products.
1. Create an array `res` initialized to 1s.
2. First pass (Prefix): For each position `i`, `res[i]` will be the product of all numbers to the left of `i`.
3. Second pass (Postfix): Maintain a running product from the right (postfix). Multiply `res[i]` by this postfix product to include all numbers to the right of `i`.

Complexity:
- Time: O(N)
- Space: O(1) (excluding the output array).
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Optimal solution using prefix and suffix products.
        Time: O(n), Space: O(1) extra space.
        """
        n = len(nums) 
        res = [1] * n
        
        # Calculate prefix products
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # Calculate postfix products and multiply with prefix
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res

    def productExceptSelfDivision(self, nums: List[int]) -> List[int]:
        """
        Solution using division.
        Note typically disallowed by the problem statement.
        """
        prod = 1
        zero_count = 0 
        
        for num in nums:
            if num:
                prod *= num
            else:
                zero_count += 1
                
        if zero_count >= 2:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_count == 1:
                if c == 0:
                    res[i] = prod
                else:
                    res[i] = 0
            else:
                res[i] = prod // c
        return res

    # Brute force solution (O(N^2)) - Time Limit Exceeded for large inputs
    # def productExceptSelfBruteForce(self, nums: List[int]) -> List[int]:
    #     res = [1] * len(nums)
    #     for i in range(len(nums)):
    #         for j in range(len(nums)):
    #             if i != j:
    #                 res[i] *= nums[j]
    #     return res


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4]
    print(f"Input: {nums}")
    print(f"Product Except Self (Optimal): {solution.productExceptSelf(nums)}")
    print(f"Product Except Self (Division): {solution.productExceptSelfDivision(nums)}")