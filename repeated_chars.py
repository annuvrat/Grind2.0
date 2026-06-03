s = "abaaa"

def duplicate(s):
    seen = {}
    result = []
    
    for ch in s:
        if ch not in seen:
            seen[ch] = 0
        seen[ch] += 1
    
    for ch, count in seen.items():
        if count > 2:
            result.append(ch)
    
    return result if result else False

print(duplicate(s))  # Output: False (empty list evaluates to False)