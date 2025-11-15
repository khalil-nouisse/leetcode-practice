class Solution:
    #O(n) space(we stock in a new table) , O(n) time
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(ch for ch in s if ch.isalnum())
        table = []
        for i in range(len(s) -1 , -1, -1) :
            table.append(s[i])
        table = "".join(table)
        print(table)
        return table == s
    #two pointers methode : O(n) tima O(1) space (we dont stock anything !)
    def isPalindrome1(self, s: str) -> bool:
        l , r = 0 , len(s) -1
        while l < r :
            if not s[l].isalnum() :
                l+= 1
            elif not s[r].isalnum() :
                r += 1
            elif s[r].upper() == s[l].upper() : 
                l += 1
                r -= 1
            else : 
                return False
        return True


sol = Solution()

s = "aaa"

print(sol.isPalindrome1(s))