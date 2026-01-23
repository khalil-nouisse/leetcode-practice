"""
the idea behind thisproblem is to fix one element "i"  and use TwoSum two pointer solution on the rest
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i ,v in enumerate(nums) : 
            if v > 0 : 
                break
            l , r = i +1 , len(nums)- 1

            if i > 0 and v == nums[i - 1]:
                continue

            while l < r : 
                threeSum = v + nums[l] + nums[r]
                if threeSum < 0 :
                    l += 1
                elif threeSum > 0 :
                    r -= 1 
                else :
                    res.append([v ,nums[l], nums[r]])
                    l += 1
                    r-= 1
                    while nums[l-1] == nums[l] and l < r : 
                        l+= 1
        return res