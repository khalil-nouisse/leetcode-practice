"""
Encode and Decode Strings
=========================

Problem:
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Idea:
Use length-prefix encoding.
For each string, encode it as `<length>#<string>`.
For example, ["neet", "code"] -> "4#neet4#code".
During decoding, read the integer until '#', then read that many characters as the string.

Complexity:
- Time: O(N) where N is the total number of characters in the list.
- Space: O(N) to store the encoded string/result.
"""

from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.
        Format: length#string
        """
        if not strs:
            return ""
            
        res = ""
        for w in strs:
            # Append length, delimiter, and the word itself
            res += str(len(w)) + '#' + w
        return res 

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string to a list of strings.
        """
        if not s:
            return []
            
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Find the delimiter '#'
            while s[j] != '#':
                j += 1
            
            # length of the next word
            length = int(s[i:j])
            
            # Valid start of word is after '#'
            j += 1
            word = s[j : j + length]
            res.append(word)
            
            # Move pointer to the start of the next encoded segment
            i = j + length
            
        return res

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ["neet", "code", "love", "you"],
        ["", "code"],
        [""],
        []
    ]
    
    for strs in test_cases:
        encoded = solution.encode(strs)
        decoded = solution.decode(encoded)
        print(f"Original: {strs}")
        print(f"Encoded:  {encoded}")
        print(f"Decoded:  {decoded}")
        print("-" * 20)

