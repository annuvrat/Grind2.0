s ="madama"

splitted = s.split()
s = s.lower().replace(" ", "")
print(s)

# fruits = s.split(",")
# print(fruits)

# joined = ",".join(fruits)

# print(joined)

# words = s.split()  # Default: split by whitespace
# print(words)


# reversed = s[::-1]

# print(reversed)


def palindrome(s):
    # s = s.lower().replace(" ", "")
    
    left = 0
    right = len(s)-1


    while left<right:
        if s[left]!= s[right]:
            return False
        left +=1
        right-=1
        




    return True
     
print(palindrome(s))
