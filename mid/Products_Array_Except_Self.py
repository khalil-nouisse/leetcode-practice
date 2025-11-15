from typing import List

class Solution:
    #brute force solution O(n**2) O(n) space for the output array and O(1) extra space
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(len(nums)) :
            for j in range(len(nums)) :
                if i == j : 
                    continue
                else :
                    res[i] = res[i] * nums[j]
        return res
    
    #using division O(n) time  ,O(n) space for the output array and O(1) extra space
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0  
        # If 2 or more zeros: → All outputs are 0. , 	
        #→ All other positions are 0.

        for num in nums :
            if num : 
                prod *= num
            else : 
                zero_count += 1 
        if zero_count >= 2 : return [0] * len(nums)

        res = [0] * len(nums)
        for i , c in enumerate(nums) :
            # If exactly 1 zero: Only the position of the zero gets the product of non-zero numbers.
            if zero_count == 1 : 
                if c == 0 : 
                    res[i] = prod
                else : 
                    res[i] = 0
            #•	If no zeros: Each result is prod // nums[i].
            else : 
                res[i] = prod//nums[i]
        return res
        #optimal solution using prefix and suffix O(n) time , O(n) space for output array , O(1) extra space
        def productExceptSelf3(self, nums: List[int]) -> List[int]:
            n = len(nums) 
            prefix = 1
            postfix = 1
            res = [1] * n
            for i in range(n) :
                res[i] *= prefix
                prefix *= nums[i]
            for j in range(n - 1 , - 1 , -1) :
                res[j] *= postfix
                postfix *= nums[j]
            return res
       

sol = Solution()
nums=[1,2,4,6]
print(sol.productExceptSelf1(nums))