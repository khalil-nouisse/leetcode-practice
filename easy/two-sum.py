#O(n²) complexity
def two_sum1(nums : list , target : int) :
    for i in range(len(nums)) :
        for j in range(i , len(nums)) :
            if nums[i] + nums[j] == target and i != j :
                return [i ,j]
    
            
tab = [3,3]
target = 6


#O(n) complexity solution using hashmaps (dict)!
def two_sum2(nums: list[int], target: int) -> list[int]:
    seen = {}  
    for i, num in enumerate(nums):  
        complement = target - num  
        if complement in seen:  
            return [seen[complement], i]
        seen[num] = i


r =  two_sum2(tab , target)

print(r)