"""
def longestCommonPrefix(self, strs: list[str]) -> str:
    longest_commun_prefix = ""
    #fiirst find the smallest word 
    min_len , min_elem = find_min(strs)
    #check for the biggest possible commun prefix (the smallest word)
    first_similarity_check = check_similarity(strs, min_elem)
    if first_similarity_check :
        return min_elem
    else :
        while max                

    return " "
    
def find_min(strs: list[str]) :
    min_len = 999999
    for elem in strs :
        if elem.len() < min_len : 
            min_len = elem.len()
            min_elem = elem
    return min_len  , min_elem       

def check_similarity(strs : list , min_elem : str) -> bool:
    similar = True
    for elem in strs : 
        if elem != min_elem :
           similar = False
           break
    return similar
"""
def longestCommonPrefix(strs: list[str]) -> str:
    match = True
    longest_commun_prefix = ""
    min_len , min_elem = find_min(strs)
    for i in range(min_len) :
        for prefix in strs : 
            if min_elem[i] != prefix[i] : 
                match = False
                break
        if match :
            longest_commun_prefix += min_elem[i]
        else : break
    return longest_commun_prefix


def find_min(strs: list[str]) :
    min_len = float('inf')
    min_elem = ""
    for elem in strs :
        if len(elem) < min_len : 
            min_len = len(elem)
            min_elem = elem
    return min_len  , min_elem  


strs = ["amm","bmm","cmm"]
print(longestCommonPrefix(strs))

