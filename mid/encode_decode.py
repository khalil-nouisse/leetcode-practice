""" 

class Solution:

    def encode(self, strs: list[str]) -> str:
        #12#neet#4#code#4#love#4#you
        if not strs :
            return ""

        res = ""
        for w in strs : 
            n = len(w)
            res +=  str(n) + '#' + w
        return res 
            
    def decode(self, s: str) -> list[str]:
        if not s :
            return []
        res = []
        i = 0
        #12#neet#4#code#4#love#4#you
        #0#
        while i < len(s) :
            length = ""
            word =""
            if s[i] == "#" :
                i += 1
                continue
            else :
                while s[i] != "#" :
                    length += s[i]
                    i += 1
                i += 1
                length = int(length)
                if length == 0 : 
                    res.append(word)
                    continue
                for j in range(i , i + length) :
                    word += s[j]
                res.append(word)
                i = j + 1
        return res                
"""

# better solution : 

class Solution:

    def encode(self, strs: list[str]) -> str:
        if not strs :
            return ""
        res = ""
        for w in strs : 
            n = len(w)
            res += str(n) + '#' + w
        return res 
            
    def decode(self, s: str) -> list[str]:
        res , i = [] , 0
        if not s :
            return []
        while i < len(s) :
            j = i 
            while s[j] != '#' :
                j += 1
            length = int(s[i:j])
            j += 1
            word = s[j : j + length]
            res.append(word)
            i = j + length
        return res            

a = ["neet" , "code" , "love" , "you"]
s = ["","code"]
f = [""]
sol = Solution()
print("originale : ", s)
print("encode : " ,sol.encode(s))
print("decode : " ,sol.decode(sol.encode(s)))

