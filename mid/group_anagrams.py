from typing import List
from collections import defaultdict

"""
the idea :  mapping the char Count to a list of anagrams : [1,0,1,...,1] : ["ate","tea"]

what i learned from my first mid problem : 
1 -  defaultdict(list) : used to decalare that the default value of that dict is empty list
    Normally in Python:
    d = {}
    d["a"].append(1)   # ❌ ERROR: KeyError, because "a" doesn't exist yet

    defaultdict is a special kind of dict from the collections module.
    It automatically creates a default value the first time a new key is used.

    Example:
    from collections import defaultdict

    d = defaultdict(list)   # 👈 list is the "default factory"

    d["a"].append(1)   # works even though "a" didn't exist before
    d["b"].append(2)

    print(d) 
    output : defaultdict(<class 'list'>, {'a': [1], 'b': [2]})

2 - Lists can’t be dictionary keys.
    You’ll need to convert the list (word_map) to a tuple so it can be used as a key.

3 - groups[tuple(word_map)].append(word)
    We want to group words into lists by their “signature” (letter count).
    So for each word:
	•	If tuple(word_map) already exists → append the word to that group.
	•	If it doesn’t exist → defaultdict automatically creates a new [] for that key, so .append(word) works without extra code.

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        alphabet_map = {letter: i for i, letter in enumerate(alphabet)}
        
        groups = defaultdict(list)

        for word in strs: 
            word = word.lower()
            word_map = [0] * 26
            for letter in word:
                if letter in alphabet_map:
                    word_map[alphabet_map[letter]] += 1
            # use tuple(word_map) as the grouping key
            groups[tuple(word_map)].append(word)
        
        return list(groups.values())


# Example usage
strs = ["act","pots","tops","cat","stop","hat"]
solution = Solution()
print(solution.groupAnagrams(strs))


#methode 2 : goood simple methode , bad for long lists 
groups = defaultdict(list)
for word in strs:
    key = tuple(sorted(word))   # same letters → same tuple
    groups[key].append(word)
return list(groups.values())


#methode. 3 : 
groups = defaultdict(list) #mapping the char Count to a list of anagrams : [1,0,1,...,1] : ["ate","tea"]
for word in strs:
    count = [0] * 26
    for c in word:
        count[ord(c) - ord('a')] += 1
    groups[tuple(count)].append(word)
return list(groups.values())
