s = "the sky is blue"



def reverseSen(s):
    words=s.split()
    print(words)
    left =0
    right = len(words)-1

    while left<right:
        words[left],words[right]=words[right],words[left]

        left+=1
        right-=1

    return " ".join(words)
        
print(reverseSen(s))