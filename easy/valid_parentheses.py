
#methode 1
def isValid(s: str) -> bool:
    stack = []
    for i , parenthese in enumerate(s) :
        if parenthese == "(" or parenthese == "[" or parenthese == "{" :
            stack.append(parenthese)
        elif parenthese == ")" or parenthese == "]" or parenthese == "}" :
            for close in range(i,len(s)):
                if not stack : break
                #print(close)
                #print(parenthese_closer_converted(stack[-1]) == s[close] )
                #print(stack)
                if parenthese_closer_converted(stack[-1]) == s[close] : 
                    stack.pop()
                else:
                    return False
    if not stack : return True
    else : False

def parenthese_closer_converted(parenthese :str ) -> str :
    match parenthese :
        case "(": 
            return ")"
        case "{":
            return "}"
        case "[":
            return "]"
        
print(isValid("]"))


#methode 2 :
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for parenthese in s : 
            if parenthese == "(" or parenthese == "[" or parenthese == "{" :
                stack.append(parenthese)
            elif parenthese == ")" or parenthese == "]" or parenthese == "}" :
                if not stack : return False
                if self.parenthese_closer_converted(stack[-1]) == parenthese:
                    stack.pop()
                else: return False
            else :return False
        return not stack
    def parenthese_closer_converted(self,parenthese :str ) -> str :
        match parenthese :
            case "(": 
                return ")"
            case "{":
                return "}"
            case "[":
                return "]"


solver = Solution()

# 2. Call the method on the instance.
#print(f"'([)]' is valid: {solver.isValid('([)]')}")
#print(f"'()[]{{}}' is valid: {solver.isValid('()[]{}')}")
#print(f"']' is valid: {solver.isValid('(')}")


#methode 3 : best 
class Solution1:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        
        for c in s:
            if c in "([{":
                stack.append(c)
            elif c in ")]}":
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                return False
        return not stack
    
solver1 = Solution1()

# 2. Call the method on the instance.
print(f"'([)]' is valid: {solver1.isValid('([)]')}")
print(f"'()[]{{}}' is valid: {solver1.isValid('()[]{}')}")
print(f"']' is valid: {solver1.isValid('(')}")