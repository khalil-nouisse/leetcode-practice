class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum())
        table = []
        for i in range(len(s) -1 , -1) :
            table.apppend(s[i])
        table = "".join(table)
        print(table)
        return table == s


sol = Solution()

s = "Was it a car or a cat I saw?"

print(sol.isPalindrome(s))