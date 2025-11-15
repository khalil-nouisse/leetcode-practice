
'''
from collections import Counter

B = [5,4,3,5,4,1,3,5,5,4]
counter = Counter(B)
print(counter)

k = 2 

res = []
i = 0
for key in counter.keys() :
    if i < k :
        res.append(key)
        i +=1
    else: break
print(res)

'''

# using heapq , complexity of O(n + mlogm) m O(nlogn) worst case , space O(m). (m uniq elements) 
import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        heap = []
        res = [0] * k
        count = self.counter(nums)
        for key , value in count.items() :
            heapq.heappush(heap , (-value , key))
        for i in range(k) :
            res[i] = heapq.heappop(heap)[1]
        return res
            
    def counter(self , nums : list[int]) :
        count = {}
        for num in nums :
            if num not in count :
                count[num] = 1
            else : 
                count[num] += 1
        return count
    
B = [5,4,3,5,4,1,3,5,5,4]
sol = Solution()
res = sol.topKFrequent(B, 2)
print(res)


#using BucketSort : complexity O(n)
'''
1.	Count frequencies of all elements (using a dictionary).
2.	Create buckets:
•	Each index i in the bucket represents frequency i.
•	Bucket i holds all numbers that appear i times.
3.	Traverse the buckets backward (from highest frequency to lowest) and collect elements until you have k.
'''

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Count frequencies
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Step 2: Create buckets (index = frequency)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)

        # Step 3: Gather top K frequent elements
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res  
                



from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for num in nums : 
            if num not in count :
                count[num] = 1
            else :count[num] += 1
        for i in range(k) :
            res[i] = max(count.values())
            del max(count)
        return res