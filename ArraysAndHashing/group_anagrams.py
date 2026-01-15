"""
Group Anagrams
==============

Problem:
Given a list of strings, group the anagrams together.

Idea:
The core idea is to map the character count (or sorted string) of each word to a list of anagrams.
For example:
- "ate" -> char count [1, 0, 0, ..., 1] -> ["ate"]
- "tea" -> char count [1, 0, 0, ..., 1] -> ["ate", "tea"]

Learnings:
1. `defaultdict(list)`:
   - Used to declare that the default value of the dict is an empty list if the key doesn't exist.
   - Avoids KeyError when accessing new keys.
   
   Example:
   ```python
   from collections import defaultdict
   d = defaultdict(list)
   d["a"].append(1) # Works automatically
   print(d) # defaultdict(<class 'list'>, {'a': [1]})
   ```

2. Lists cannot be dictionary keys:
   - Lists are mutable and unhashable.
   - We convert the list (word_map) to a tuple to use it as a key.

3. `groups[tuple(word_map)].append(word)`:
   - Group words into lists by their "signature" (letter count).
   - If the signature exists, append to that group.
   - If not, `defaultdict` creates a new list.

Complexity:
- Time: O(N * K) where N is the number of strings and K is the maximum length of a string.
- Space: O(N * K) to store the result.
"""

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams using character count mapping.
        """
        # Create a mapping for alphabet positions (a=0, b=1, ...)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        alphabet_map = {letter: i for i, letter in enumerate(alphabet)}
        
        groups = defaultdict(list)

        for word in strs: 
            # Ideally data should be clean, but assuming case-insensitive for robustness based on original code
            # Note: LeetCode usually specifies lowercase English letters.
            word_lower = word.lower()
            
            # Create a character count array (frequency map) for the word
            word_map = [0] * 26
            for letter in word_lower:
                if letter in alphabet_map:
                    word_map[alphabet_map[letter]] += 1
            
            # Use tuple(word_map) as the grouping key because lists are not hashable
            groups[tuple(word_map)].append(word)
        
        return list(groups.values())

# Alternative Approaches (for reference):

# Method 2: Sorting
# Complexity: O(N * K * log K) due to sorting each string
# def groupAnagramsSorted(self, strs: List[str]) -> List[List[str]]:
#     groups = defaultdict(list)
#     for word in strs:
#         key = tuple(sorted(word))
#         groups[key].append(word)
#     return list(groups.values())


# Method 3: Optimized Count (using ord)
# Identical logic to main solution but uses 'ord' instead of manual map
# def groupAnagramsOrd(self, strs: List[str]) -> List[List[str]]:
#     groups = defaultdict(list)
#     for word in strs:
#         count = [0] * 26
#         for c in word:
#             count[ord(c) - ord('a')] += 1
#         groups[tuple(count)].append(word)
#     return list(groups.values())


if __name__ == "__main__":
    solution = Solution()
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    print(f"Input: {strs}")
    print(f"Grouped Anagrams: {solution.groupAnagrams(strs)}")


