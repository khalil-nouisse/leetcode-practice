# methode 1 : reverse digits
def isPalindrome(x: int) -> bool:
    if x<0 :
        return False
    elif x == 0 :
        return True
    else : #case where x is positive
        rev_num = get_reversed(x)
        print(rev_num)
        if rev_num == x :
            return True
        return False

def get_reversed(n: int) : 
    rev_num = 0
    print(n)
    while n > 0 :
        last_digit = n % 10
        rev_num = (rev_num * 10) + last_digit
        n = n // 10
        print(n,rev_num)
    return rev_num



#methode 2 , half reverse the integer
def get_half_reversed(x :int) :
    if x < 0 or (x != 0 and x % 10 == 0) : 
        return False
    half_reversed = 0
    while x > half_reversed :
        last_digit = x % 10
        half_reversed = (half_reversed * 10 ) + last_digit
        x = x // 10
    
    return x == half_reversed or x == half_reversed // 10

print(get_half_reversed(112))
