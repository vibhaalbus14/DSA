def non_repeating_char(str):
    #write code here
    string=str
    hash={}
    for  char in string:
        if char in hash:
            hash[char]+=1
        else:
            hash[char]=1
    for key,value in hash.items():
        if value==1:
            return string.index(key)
    return None
print(non_repeating_char("aaAABbbbhjb"))
            
        