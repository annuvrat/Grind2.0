s = "listen"
t = "silent"


def isAnagram(s,t):
    counts = {}
    if len(s)!= len(t):
        return False
    
    for char in s:
       if char not in counts:
           counts[char] = 0

       counts[char] +=1

    for ch in t:
        if ch not in counts:
            return False
        
        counts[ch] -= 1 
            

    for count in counts.values():
        if count != 0:
            return False
    return True



print(isAnagram(s,t))