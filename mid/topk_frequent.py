"""
Top K Frequent Elements
=======================

Problem:
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Idea:
Two main approaches:
1. **Bucket Sort (O(N))**:
   - Count frequencies of all elements.
   - Create buckets where index represents frequency.
   - Bucket[i] contains a list of numbers that appear i times.
   - Iterate buckets from end (highest frequency) to beginning.

2. **Heap (O(N log K) or O(N log N))**:
   - Count frequencies.
   - Push to a heap (max heap or min heap of size k).
   - Pop top k elements.

Complexity:
- Time: O(N) for Bucket Sort.
- Space: O(N) to store counts and buckets.
"""

from typing import List
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Finds top K frequent elements using Bucket Sort.
        Time Complexity: O(N)
        """
        # Step 1: Count frequencies
        # Using Counter is more Pythonic than manual counting
        count = Counter(nums)

        # Step 2: Create buckets (index = frequency)
        # Maximum frequency is len(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)

        # Step 3: Gather top K frequent elements
        res = []
        # Iterate backwards from highest frequency
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res

    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        """
        Finds top K frequent elements using Heap.
        Time Complexity: O(N log K) if optimized, or O(N log N) with simple sort/heap.
        """
        count = Counter(nums)
        heap = []
        
        # Method 1 using basic push (O(N log N) effectively if pushing all)
        for val, freq in count.items():
            # Use negative freq for Max Heap behavior with Python's Min Heap
            heapq.heappush(heap, (-freq, val))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        # Alternatively, heapq.nlargest(k, count.keys(), key=count.get) is cleaner
        return res
    
    # helper for manual counting if needed (educational purpose)
    def _manual_counter(self, nums: List[int]) -> dict:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        return count

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(f"Input: {nums}, k={k}")
    print(f"Top K (Bucket Sort): {solution.topKFrequent(nums, k)}")
    print(f"Top K (Heap): {solution.topKFrequentHeap(nums, k)}")





